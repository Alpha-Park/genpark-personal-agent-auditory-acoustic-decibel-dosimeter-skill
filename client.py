# -*- coding: utf-8 -*-
"""Personal Agent Auditory Acoustic Decibel Dosimeter Skill.

Zero-dependency NIOSH/OSHA cumulative noise dose calculator, equivalent sound level (Leq) modeler,
and Temporary Threshold Shift (TTS) cochlear recovery evaluator.
"""

import math
from typing import Dict, List, Any, Optional

class PersonalAgentAuditoryAcousticDecibelDosimeter:
    """Quantitative acoustic dosimeter and auditory trauma risk engine based on
    NIOSH (3 dB exchange rate) and OSHA (5 dB exchange rate) occupational standards."""

    def calculate_cumulative_noise_dose(
        self,
        sound_exposures: List[Dict[str, float]],
        standard: str = "niosh_3db"
    ) -> Dict[str, Any]:
        """Calculates cumulative noise dose percentage (%), 8-hour Time-Weighted Average (TWA dBA),
        and equivalent continuous sound level (Leq)."""
        if not sound_exposures:
            return {"error": "Empty sound exposures array"}

        is_niosh = standard.lower().startswith("niosh")
        crit_level = 85.0 if is_niosh else 90.0
        exchange_q = 3.0 if is_niosh else 5.0

        total_dose_pct = 0.0
        total_time_hours = 0.0
        linear_energy_sum = 0.0

        for segment in sound_exposures:
            spl = float(segment.get("sound_pressure_level_dba", 70.0))
            hours = float(segment.get("duration_hours", 1.0))
            total_time_hours += hours

            # Permissible time T = 8 / 2^((L - Criterion) / Q)
            t_permissible = 8.0 / (2.0 ** ((spl - crit_level) / exchange_q))
            segment_dose = (hours / max(0.001, t_permissible)) * 100.0
            total_dose_pct += segment_dose

            # Leq acoustic energy accumulation: t * 10^(L / 10)
            linear_energy_sum += hours * (10.0 ** (spl / 10.0))

        # Equivalent continuous sound level Leq
        if total_time_hours > 0 and linear_energy_sum > 0:
            leq = round(10.0 * math.log10(linear_energy_sum / total_time_hours), 1)
        else:
            leq = 0.0

        # Time-Weighted Average: TWA = Criterion + (Q / log10(2)) * log10(Dose / 100)
        if total_dose_pct > 0:
            q_factor = exchange_q / math.log10(2.0)
            twa = round(crit_level + q_factor * math.log10(total_dose_pct / 100.0), 1)
        else:
            twa = 0.0

        # Auditory Risk Classification
        if total_dose_pct <= 50.0:
            risk_tier = "Acoustically Benign / Zero Cochlear Hazard"
            cochlear_status = "Outer hair cell stereocilia intact; no acoustic trauma risk"
        elif total_dose_pct <= 100.0:
            risk_tier = "Moderate Exposure / Within Daily Permissible Limit"
            cochlear_status = "Sub-critical synaptic strain; sensory rest recommended"
        elif total_dose_pct <= 250.0:
            risk_tier = "Permissible Exposure Limit Exceeded (PEL Violation)"
            cochlear_status = "Temporary Threshold Shift (TTS) imminent; glutamate excitotoxicity at ribbon synapses"
        else:
            risk_tier = "Severe Acoustic Hazard / Acute Cochlear Danger"
            cochlear_status = "Permanent Threshold Shift (PTS) risk; irreversible outer hair cell destruction"

        return {
            "evaluation_standard": "NIOSH (85 dBA Criterion, 3 dB Exchange)" if is_niosh else "OSHA (90 dBA Criterion, 5 dB Exchange)",
            "total_monitoring_duration_hours": round(total_time_hours, 2),
            "cumulative_noise_dose_pct": round(total_dose_pct, 1),
            "equivalent_continuous_sound_level_leq_dba": leq,
            "eight_hour_time_weighted_average_twa_dba": twa,
            "auditory_risk_tier": risk_tier,
            "cochlear_stereocilia_status": cochlear_status,
            "protective_action": (
                "IMMEDIATE ACOUSTIC RECESS: Relocate to quiet environment (< 60 dBA) for at least 14-16 hours."
                if total_dose_pct > 100.0 else
                "Maintain normal listening volumes (< 75 dBA) for headphones."
            )
        }

    def estimate_temporary_threshold_shift_recovery(
        self,
        peak_spl_dba: float = 98.0,
        exposure_duration_minutes: float = 60.0
    ) -> Dict[str, Any]:
        """Estimates Temporary Threshold Shift (TTS in dB) and hours required for
        cochlear stereocilia ribbon synapse recovery in quiet ambient conditions."""
        spl = max(60.0, float(peak_spl_dba))
        dur_min = max(5.0, float(exposure_duration_minutes))

        # Empirical Ward TTS estimation:
        # TTS2 (dB shift 2 min post-exposure) ~ 0.5 * (SPL - 80) * log10(duration)
        if spl <= 80.0:
            tts2_db = 0.0
            recovery_hours = 0.0
        else:
            tts2_db = round(max(0.0, 0.45 * (spl - 80.0) * math.log10(dur_min)), 1)
            # Recovery follows log time: typically 1.5 - 2 hours per 3 dB of TTS
            recovery_hours = round(max(1.0, (tts2_db / 3.0) * 2.2), 1)

        return {
            "peak_noise_exposure_spl_dba": spl,
            "exposure_duration_minutes": dur_min,
            "estimated_temporary_threshold_shift_tts2_db": tts2_db,
            "estimated_quiet_recovery_time_hours": recovery_hours,
            "recovery_environment_criterion": "Maintain ambient acoustic environment < 55 dBA during recovery period.",
            "synaptopathy_warning": tts2_db >= 15.0
        }

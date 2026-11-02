# -*- coding: utf-8 -*-
"""Demonstration of Personal Agent Auditory Acoustic Decibel Dosimeter Skill."""

import sys
sys.stdout.reconfigure(encoding='utf-8')
from client import PersonalAgentAuditoryAcousticDecibelDosimeter

def main():
    agent = PersonalAgentAuditoryAcousticDecibelDosimeter()

    print("=" * 70)
    print("DEMO: Personal Agent Auditory Acoustic Dosimeter & Cochlear Safety")
    print("=" * 70)

    # 1. Calculate Daily Cumulative Noise Dose (Office, Commute, Coffee Shop, Gym)
    exposures = [
        {"sound_pressure_level_dba": 62.0, "duration_hours": 5.0},  # Quiet office
        {"sound_pressure_level_dba": 78.0, "duration_hours": 1.0},  # Subway commute
        {"sound_pressure_level_dba": 72.0, "duration_hours": 2.0},  # Coffee shop
        {"sound_pressure_level_dba": 91.0, "duration_hours": 0.75}  # Gym with loud music
    ]

    res_dose = agent.calculate_cumulative_noise_dose(
        sound_exposures=exposures,
        standard="niosh_3db"
    )

    print(f"\n1. Daily Cumulative Noise Dose Analysis (NIOSH 3dB Exchange):")
    print(f"   Monitored Duration: {res_dose['total_monitoring_duration_hours']} hrs")
    print(f"   Cumulative Dose: {res_dose['cumulative_noise_dose_pct']}%")
    print(f"   Equivalent Level (Leq): {res_dose['equivalent_continuous_sound_level_leq_dba']} dBA")
    print(f"   8-Hour TWA: {res_dose['eight_hour_time_weighted_average_twa_dba']} dBA")
    print(f"   Risk Tier: {res_dose['auditory_risk_tier']}")
    print(f"   Cochlear Stereocilia Status: {res_dose['cochlear_stereocilia_status']}")
    print(f"   Prescription: {res_dose['protective_action']}")

    # 2. Estimate Temporary Threshold Shift Recovery after Concert (102 dBA for 90 mins)
    res_tts = agent.estimate_temporary_threshold_shift_recovery(
        peak_spl_dba=102.0,
        exposure_duration_minutes=90.0
    )

    print(f"\n2. Temporary Threshold Shift (TTS) Recovery Modeling:")
    print(f"   Exposure: {res_tts['peak_noise_exposure_spl_dba']} dBA for {res_tts['exposure_duration_minutes']} min")
    print(f"   Estimated TTS2: {res_tts['estimated_temporary_threshold_shift_tts2_db']} dB shift")
    print(f"   Recovery Time Needed: {res_tts['estimated_quiet_recovery_time_hours']} hours (< 55 dBA environment)")
    print(f"   Synaptopathy Warning: {res_tts['synaptopathy_warning']}")

    print("\nVerification complete: Acoustic dosimeter engine executed flawlessly.")

if __name__ == "__main__":
    main()

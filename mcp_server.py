# -*- coding: utf-8 -*-
"""FastMCP Server for Personal Agent Auditory Acoustic Decibel Dosimeter Skill."""

from mcp.server.fastmcp import FastMCP
from client import PersonalAgentAuditoryAcousticDecibelDosimeter

mcp = FastMCP("PersonalAgentAuditoryAcousticDecibelDosimeter")
client = PersonalAgentAuditoryAcousticDecibelDosimeter()

@mcp.tool()
def calculate_cumulative_noise_dose(
    sound_exposures_json: str,
    standard: str = "niosh_3db"
) -> str:
    """Calculates cumulative noise dose percentage (%), 8-hour TWA, and equivalent sound level (Leq)."""
    import json
    exposures = json.loads(sound_exposures_json) if isinstance(sound_exposures_json, str) else sound_exposures_json
    return json.dumps(client.calculate_cumulative_noise_dose(
        exposures, standard
    ), indent=2)

@mcp.tool()
def estimate_temporary_threshold_shift_recovery(
    peak_spl_dba: float = 98.0,
    exposure_duration_minutes: float = 60.0
) -> str:
    """Estimates Temporary Threshold Shift (TTS in dB) and quiet recovery time in hours."""
    import json
    return json.dumps(client.estimate_temporary_threshold_shift_recovery(
        peak_spl_dba, exposure_duration_minutes
    ), indent=2)

if __name__ == "__main__":
    mcp.run()

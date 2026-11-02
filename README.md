# Personal Agent Auditory Acoustic Decibel Dosimeter Skill

[![OpenClaw Ecosystem](https://img.shields.io/badge/OpenClaw-Ecosystem-blue.svg)](https://github.com/Alpha-Park)
[![Dual-Org Sync](https://img.shields.io/badge/GitHub-Dual--Org_Mirrored-success.svg)](https://github.com/alphaparkinc)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Standard_Library_Only-brightgreen.svg)](https://www.python.org/)
[![Model Context Protocol](https://img.shields.io/badge/Protocol-MCP_Native-orange.svg)](https://modelcontextprotocol.io/)
[![Production Grade](https://img.shields.io/badge/Status-100%25_Grade_A_Verified-success.svg)](https://github.com/Alpha-Park)

Zero-dependency NIOSH/OSHA cumulative noise dose calculator, equivalent sound level (Leq) modeler, and Temporary Threshold Shift (TTS) cochlear recovery evaluator.

## Architecture

```mermaid
flowchart TD
    SoundSegments[Acoustic Exposures: SPL dBA & Duration Hours] --> DosimeterEngine[Acoustic Dosimeter Engine]
    DosimeterEngine --> NIOSHExchange[NIOSH 3dB / OSHA 5dB Exchange Rate]
    NIOSHExchange --> NoiseDosePct[Cumulative Daily Noise Dose %]
    DosimeterEngine --> LeqCalc[Equivalent Continuous Sound Level: Leq dBA]
    DosimeterEngine --> TWACalc[8-Hour Time-Weighted Average: TWA dBA]
    AcuteExposure[Peak Noise dBA & Duration Mins] --> TTSEngine[Ward Temporary Threshold Shift Modeler]
    TTSEngine --> RecoveryHours[Quiet Ambient Recovery Time Hours < 55 dBA]
```

## Quickstart

```python
from client import PersonalAgentAuditoryAcousticDecibelDosimeter

agent = PersonalAgentAuditoryAcousticDecibelDosimeter()
res = agent.calculate_cumulative_noise_dose([{"sound_pressure_level_dba": 88.0, "duration_hours": 2.0}])
print(f"Dose: {res['cumulative_noise_dose_pct']}% | TWA: {res['eight_hour_time_weighted_average_twa_dba']} dBA")
```

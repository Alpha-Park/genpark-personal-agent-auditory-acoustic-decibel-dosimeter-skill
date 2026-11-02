---
name: genpark-personal-agent-auditory-acoustic-decibel-dosimeter-skill
version: "1.0.0"
description: "Zero-dependency NIOSH/OSHA cumulative noise dose calculator, equivalent sound level (Leq) modeler, and Temporary Threshold Shift (TTS) cochlear recovery evaluator."
license: MIT
dependencies:
  - python>=3.10
  - mcp>=1.0.0
entrypoint: client.py
---

# Personal Agent Auditory Acoustic Decibel Dosimeter Skill

Designed for **OpenClaw**, **Hermes**, and autonomous personal AI companions to track cumulative occupational and environmental acoustic exposure, compute 8-hour Time-Weighted Average ($TWA$) and equivalent continuous sound levels ($L_{\text{eq}}$) under NIOSH (3 dB exchange) and OSHA (5 dB exchange) standards, and forecast Temporary Threshold Shift (TTS) recovery kinetics.

## Agent In-Context Capabilities

- **Logarithmic Noise Dose Accumulation**: Accurately sums multi-segment acoustic energy across diverse environments (office, commute, concerts, headphone listening).
- **Standards Dual-Mode**: Supports both the protective NIOSH standard (85 dBA criterion / 3 dB exchange rate) and regulatory OSHA framework (90 dBA / 5 dB exchange rate).
- **Cochlear Synaptopathy Protection**: Predicts temporary hearing threshold shift and prescribes quiet recovery duration ($< 55$ dBA) to prevent permanent ribbon synapse denervation.

## Tools Summary

1. `calculate_cumulative_noise_dose`: Computes percentage dose, $L_{\text{eq}}$, $TWA$, and cochlear risk tier.
2. `estimate_temporary_threshold_shift_recovery`: Estimates post-exposure threshold shift in dB and required quiet recovery hours.

# mmc-modelling-toolkit

Open-source Python toolkit for modular multilevel converter (MMC) modelling, simulation and control examples for power electronics research and education.

## Overview

This project collects small, readable Python examples for studying modular multilevel converters, a key topology for flexible HVDC transmission, renewable-energy integration and battery energy storage systems.

The goal is educational and research-oriented: provide clear baseline models that students and early-stage researchers can run, modify and extend, rather than a production-grade simulation platform.

## Contents

- `examples/mmc_arm_voltage.py` - Minimal example that computes upper/lower arm reference voltages for a single-phase MMC leg from a DC-link voltage and a sinusoidal modulation signal.
- More examples (submodule capacitor voltage balancing, circulating-current basics) are planned.

## Quick start

```bash
python examples/mmc_arm_voltage.py
```

No third-party packages are required for the first example; it uses only the Python standard library.

## Roadmap

- [ ] Submodule capacitor voltage calculation
- [ ] Nearest-level modulation (NLM) example
- [ ] Circulating current illustration
- [ ] Notes on MMC modelling assumptions and references

## Maintainer

Maintained by the repository owner as the primary maintainer: issue triage, pull-request review, releases and documentation are handled in this repository.

## License

MIT - see `LICENSE`.

# Ayodeji Sunday Babalola  
## Hardware, Systems & Test Engineering Portfolio

Hardware engineer focused on **experimental validation, embedded systems, and energy harvesting R&D**, with a strong emphasis on measurement-driven debugging, hardware characterization, and system-level reliability.

This repository presents representative projects from my work in:

- hardware validation  
- embedded systems and firmware testing  
- electronics bring-up and fault isolation  
- experimental prototyping and applied R&D  
- energy harvesting and sensor systems  

Due to NDAs and company ownership, some projects are described at the **system architecture and test-strategy level** rather than with full schematics or source code.

The goal of this portfolio is to demonstrate **how I approach real engineering problems** — designing experiments, collecting measurements, isolating root causes, and iterating hardware and firmware together.

---

# Core Expertise

- Post-silicon validation and characterization  
- Electronics bring-up and PCB fault isolation  
- Firmware and low-level interface testing  
- Experimental hardware prototyping  
- Energy harvesting systems and sensor platforms  
- Test process design and validation strategy  
- Test automation using Python  
- Data-driven engineering and measurement analysis  
- Cross-functional systems engineering

---

# Project Index

| Section | Project |
|-------|-------|
| 01 | [Post-Silicon Validation of MEMS Timing Devices](01_post_silicon_validation/) |
| 02 | [Electronics & PCB Validation for Embedded Systems](02_electronics_pcb_validation/) |
| 03 | [Firmware & Low-Level Software Testing](03_firmware_low_level_testing/) |
| 04 | [Energy Harvesting & Sensor Systems Prototyping](04_energy_harvesting_prototyping/) |
| 05 | [Test Process Design & Validation Strategy](05_test_process_design/) |
| 06 | [Cross-Functional Systems Engineering & Delivery](06_cross_functional_engineering/) |

Each section documents real engineering scenarios including:

- system architecture
- debugging methodology
- measurement data
- test results
- engineering conclusions

---

# Hardware Energy Harvesting Experiments

Recent experimental validation of **vibration energy harvesting architectures** using a controlled shaker setup.

The experiment compares two different harvesting approaches:

- **WaveHarvester broadband energy harvester**
- **Double-cantilever piezoelectric harvesters**

The objective of the tests was to evaluate how each architecture performs under controlled vibration excitation.

## Example Test Parameters

- Frequencies tested: **25 Hz, 50 Hz, 60 Hz**
- Storage capacitor: **470 µF**
- Load resistor: **22 kΩ**
- Excitation source: vibration shaker
- Mounting method: rigid cyanoacrylate coupling

During a long-duration accumulation test, the broadband harvester reached approximately:

**~3.05 V across a 470 µF capacitor after a 6-minute run at ~50 Hz excitation.**

This behavior indicates that the device is well matched to vibration frequencies commonly found in industrial equipment.

---

# Experiment Documentation

Full field notes, measurement logs, and plots are available here:

[2026-03-05 Vibration Harvester Validation](docs/field-notes/2026-03-05-vibration-harvester-validation)

The documentation includes:

- experimental setup
- raw measurement logs
- charging curves and comparison plots
- engineering observations
- interpretation of system behavior

---

# Engineering Approach

My work emphasizes **measurement-driven engineering**.

Rather than relying purely on theoretical models, I prioritize:

- designing controlled experiments
- instrumenting systems to capture real electrical and mechanical behavior
- analyzing measurement data
- isolating root causes through structured debugging
- iterating both hardware and firmware designs

The projects in this repository are documented as **engineering field notes**, similar to internal validation reports used in hardware R&D environments.

---

# Notes

I am happy to walk through any of these projects in more detail during technical interviews or engineering discussions.
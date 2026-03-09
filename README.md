# Ayodeji Sunday Babalola  
## Hardware, Systems & Test Engineering Portfolio

Hardware engineer focused on **experimental validation, embedded systems, optical sensing, and energy harvesting R&D**, with a strong emphasis on measurement-driven debugging, hardware characterization, and system-level reliability.

This repository presents representative engineering projects and validation work from areas including:

- hardware validation and characterization  
- embedded systems and firmware testing  
- electronics bring-up and PCB fault isolation  
- experimental prototyping and applied R&D  
- optical sensing systems  
- vibration energy harvesting systems  

Due to NDAs and company ownership, some projects are described at the **system architecture, validation, and test-strategy level** rather than with full schematics or proprietary source code.

The goal of this portfolio is to demonstrate **how I approach real engineering problems** — designing experiments, collecting measurements, isolating root causes, and iterating hardware and firmware together.

---

# Core Expertise

- Post-silicon validation and characterization  
- Electronics bring-up and PCB fault isolation  
- Firmware and low-level interface testing  
- Optical sensing system validation  
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
| 07 | [Hardware Debug Case Studies](07_hardware_debug_case_studies/) |
| 08 | [Laser Triangulation Sensor Validation](08_laser_triangulation_sensor_validation/) |

Each section documents real engineering scenarios including:

- system architecture
- debugging methodology
- measurement instrumentation
- experimental setup design
- test results and observations
- engineering conclusions

---

# Optical Sensor Validation (Laser Triangulation)

This section documents experimental validation work on **laser triangulation sensing systems**.

Laser triangulation sensors measure displacement by projecting a laser beam onto a target surface and detecting the reflected spot position on a **position-sensitive detector (PSD)**.

The work documented includes:

- optical alignment and calibration procedures  
- sensor accuracy and repeatability characterization  
- signal linearity and noise analysis  
- calibration curve generation  
- experimental validation setup design  

Presentation describing the sensing system and validation work:

[Laser Triangulation Sensor Development & Validation](08_laser_triangulation_sensor_validation/laser_triangulation_overview.pdf)

Full project documentation:

[Laser Triangulation Sensor Validation Project](08_laser_triangulation_sensor_validation/)

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

This behavior indicates that the device is well matched to vibration frequencies commonly found in industrial environments.

---

# Experiment Documentation

Detailed field notes, measurement logs, and experimental analysis are available here:

[2026-03-05 Vibration Harvester Validation](docs/field-notes/2026-03-05-vibration-harvester-validation)

The documentation includes:

- experimental setup diagrams  
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

I am happy to walk through any of these projects in more detail during **technical interviews or engineering discussions**.

For additional background on my engineering work:

- LinkedIn: https://linkedin.com/in/ayodejibabalola  
- GitHub: https://github.com/AyodejiBaba
# Ayodeji Sunday Babalola  
## Hardware, Systems & Test Engineering Portfolio

Hardware engineer focused on **experimental validation, embedded systems, optical sensing, and energy harvesting R&D**, with a strong emphasis on:

- measurement-driven debugging  
- hardware characterization  
- system-level reliability  
- sensor system validation  

This repository documents representative engineering work demonstrating how I approach **real hardware problems** — designing experiments, collecting measurements, isolating root causes, and iterating hardware and firmware together.

Some projects are documented at the **system architecture and validation methodology level** due to NDAs.

---

# Featured Engineering Work

## 1. Laser Triangulation Sensor Validation

Experimental validation of a **laser triangulation optical sensing system** including:

- optical alignment and calibration
- sensor accuracy and repeatability characterization
- signal linearity and noise analysis
- calibration curve generation
- experimental validation setup design

Project documentation:

[Laser Triangulation Sensor Validation](08_laser_triangulation_sensor_validation/)

Presentation slides:

[Laser Triangulation Sensor Development & Validation](08_laser_triangulation_sensor_validation/laser_triangulation_overview.pdf)

---

## 2. Vibration Energy Harvesting Experiments

Experimental characterization of **broadband and piezoelectric vibration energy harvesting systems** using controlled shaker excitation and capacitor charge accumulation measurements.

Two architectures were tested:

- **WaveHarvester broadband energy harvester**
- **Double-cantilever piezoelectric harvesters**

### Example Validation Result

| Architecture | Frequency | Test Duration | Peak Voltage |
|---|---|---|---|
| WaveHarvester | 50 Hz | 6 min | ~3.05 V |
| Double Cantilever | 25 Hz | 6 min | ~0.247 V |
| Double Cantilever | 50 Hz | 6 min | ~0.022 V |

These results demonstrate the trade-off between **broadband harvesting architectures and narrowband resonant harvesters**.

Project documentation:

[2026-03-05 Vibration Harvester Validation](docs/field-notes/2026-03-05-vibration-harvester-validation)

---

## 3. Hardware Debug & Root Cause Isolation

Representative debugging case studies demonstrating structured engineering approaches to diagnosing hardware failures.

Examples include:

- power rail failures  
- PCB assembly defects  
- signal integrity issues  
- board bring-up failures  

These projects demonstrate systematic approaches to **fault isolation, measurement instrumentation, and root cause identification**.

Examples available here:

[Hardware Debug Case Studies](07_hardware_debug_case_studies/)

---

# Embedded Telemetry Firmware

Energy harvesting experiments used an **ESP32 MicroPython telemetry system** for measurement logging.

Capabilities include:

- ADC voltage sampling
- CSV telemetry logging
- optional ThingsBoard streaming
- Wi-Fi failover
- watchdog-based recovery for long-duration experiments

Firmware repository folder:

`firmware/esp32-waveharvester/`

---

# Core Engineering Expertise

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

---

# Repository Structure

```text
technical-portfolio-hardware-systems/
├── docs/
│   └── field-notes/
│       └── experimental hardware validation notes
├── firmware/
│   └── esp32-waveharvester/
│       └── MicroPython telemetry firmware
├── data/
│   └── processed experimental datasets
├── plots/
│   └── experiment visualizations
└── README.md
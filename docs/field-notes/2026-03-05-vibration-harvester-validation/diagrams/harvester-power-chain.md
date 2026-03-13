# Energy Harvesting Power Chain

This diagram captures the current power path used in the vibration energy harvesting validation work. It reflects the system-level flow from mechanical excitation through rectification, storage, and voltage boosting toward a usable output stage.

## System Diagram

<p align="center">
  <img src="harvester-power-chain.svg" width="700">
</p>

<p align="center">
  <em>Figure 1. Current vibration energy harvesting power chain used during prototype validation.</em>
</p>

## Purpose

The purpose of this diagram is to document the present architecture used during shaker-based validation of the harvester prototype and to clearly communicate the energy flow through the system.

## Power Flow Overview

The system follows this basic chain:

**Vibration input → Harvester transducer → Rectifier → Storage capacitor → Boost converter → Regulated output / demonstration load**

At a high level:

- **Vibration input** provides the external mechanical excitation.
- The **harvester transducer** converts vibration into electrical energy.
- The **rectifier** converts the generated AC or variable signal into usable DC.
- The **storage capacitor** accumulates harvested energy over time.
- The **boost converter** raises the stored voltage to a more usable output level.
- The **output stage** supports demonstration loads such as a USB charging indicator or low-power electronics.

## Engineering Relevance

This power chain is important because it separates the harvesting problem into clear stages that can each be tested independently:

1. **Mechanical coupling and energy generation**
2. **Electrical conversion and rectification**
3. **Energy accumulation and storage**
4. **Voltage conditioning and usable output delivery**

This makes it easier to debug weak performance, identify bottlenecks, and communicate design trade-offs during prototype reviews.

## Current Validation Context

This architecture supports ongoing experimental work focused on:

- vibration-driven charging behaviour
- capacitor voltage rise over time
- effect of excitation frequency and amplitude
- impact of loading on harvested energy
- feasibility of powering visible demonstration outputs

Recent prototype testing showed that the system can accumulate energy on a storage capacitor under controlled shaker excitation, confirming that the overall power chain is functioning and that the concept is suitable for continued optimisation.

## Notes

This diagram is intended as a system-level engineering reference and not as a final production schematic. Component values, converter choices, and harvester implementation details may evolve as testing continues.

## Related Validation Work

This diagram supports the broader field note for the vibration harvester validation experiment and should be read alongside:

- experimental setup notes
- measured capacitor charging results
- frequency response observations
- prototype build photographs
- telemetry or oscilloscope captures where available
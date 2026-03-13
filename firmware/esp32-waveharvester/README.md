# ESP32 WaveHarvester Firmware

This folder contains the MicroPython firmware used for shaker-based vibration energy harvesting validation.

## Files

- `boot.py` — minimal boot-time initialization
- `main.py` — telemetry logging, ADC acquisition, optional ThingsBoard streaming, watchdog-based recovery

## Functional Overview

The firmware supports:

- ADC sampling of the harvester storage voltage
- local CSV logging to `telemetry.csv`
- optional live telemetry streaming to ThingsBoard
- Wi-Fi retry across known networks
- MQTT reconnection
- watchdog reset for robustness during long-duration tests

## Measurement Path

The ESP32 samples the capacitor voltage using an ADC input and records:

- timestamp
- alive counter
- ADC raw count
- ADC voltage
- capacitor voltage
- capacitor voltage in millivolts

## Notes

This public version is sanitized for portfolio use.

- Device tokens and deployment credentials have been removed
- Network names may be replaced with placeholders where needed
- The code is shown to demonstrate embedded telemetry architecture and validation workflow

## Typical Use Case

This firmware was used in vibration harvester experiments to monitor voltage accumulation on a storage capacitor during shaker excitation at different frequencies.

Related project documentation:

- `docs/field-notes/2026-03-05-vibration-harvester-validation/`

## Embedded Telemetry

Voltage accumulation was logged using an ESP32-based MicroPython telemetry stack with ADC sampling, local CSV logging, and optional cloud streaming.

Related firmware:
`../../../firmware/esp32-waveharvester/`
# Vibration Harvester Validation Update

## Overview

This update documents controlled shaker tests comparing the WaveHarvester architecture against double-cantilever harvesters.

## Test setup

- Shaker excitation frequencies: 25 Hz, 50 Hz, 60 Hz
- Typical shaker amplitude: ~75–80%
- Electrical storage: 470 µF capacitor
- Electrical load: 22 kΩ resistor across the capacitor
- Logging: ESP32 ADC telemetry

See `plots/test_setup_diagram.png`.

## Key findings

### WaveHarvester
- Best short-run response was observed around **50 Hz**
- A 6-minute run at 50 Hz reached **~3.05 V**
- The WaveHarvester behaved as a **broadband harvester** with meaningful output at 25 Hz, 50 Hz, and 60 Hz

### Double cantilever
- The larger cantilever showed its strongest response near **25 Hz**
- A 6-minute run at 25 Hz reached **~0.247 V**
- At 50 Hz and 60 Hz, cantilever output remained very small, confirming **narrowband resonant behavior**
- The smaller double cantilever also showed sensitivity to mounting and frequency, but still underperformed the WaveHarvester in the tested range

## Peak voltage summary

See `data/summary_results.csv` and `plots/peak_voltage_comparison.png`.

## Generated plots

- `plots/waveharvester_frequency_comparison.png`
- `plots/cantilever_frequency_comparison.png`
- `plots/long_duration_accumulation_comparison.png`
- `plots/peak_voltage_comparison.png`
- `plots/test_setup_diagram.png`

## Interpretation

The experiments show a clear architecture trade-off:

- **WaveHarvester**: better broadband response, better suited to variable industrial vibration environments
- **Double cantilever**: narrower resonant response, better only when matched closely to a specific excitation band

## Suggested next updates

- Add accelerometer measurements for shaker amplitude / input acceleration
- Add USB boost-converter demo results
- Add normalized power estimates under load

## Raw Measurement Data

The full experimental dataset, including all test runs and intermediate calculations,
is available in the Google Sheets workbook below.

Google Sheets:
https://docs.google.com/spreadsheets/d/1gCekP5nfxt22zZ_sTUwfDKp3-2Z2egHInZx5xVwocbY/edit?usp=sharing

The sheet contains multiple tabs for:

- WaveHarvester tests (25 Hz, 50 Hz, 60 Hz)
- Double cantilever tests
- Long-duration accumulation tests
- Plot preparation tables

# Vibration Energy Harvesting Validation – WaveHarvester

Date: 5 March 2026  
Location: Lab setup with vibration shaker

## Objective

Validate the electrical output of the WaveHarvester device under controlled vibration frequencies and quantify capacitor charging behavior.

The goal was to confirm energy accumulation capability prior to building a USB-powered demo.

---

## Test Setup

Device: WaveHarvester prototype  
Mounting: Rigid cyanoacrylate coupling to shaker surface  
Capacitor: 470 µF  
Load resistor: 22 kΩ across capacitor terminals  
Measurement: ESP32 ADC logging capacitor voltage

Test frequencies explored:

- 25 Hz
- 50 Hz
- 60 Hz

---

## Key Result (50 Hz – 6 minute run)

The device was excited at:

Frequency: 50 Hz  
Amplitude: ~75–80% shaker output  
Duration: ~6 minutes

Peak capacitor voltage reached:

**3.05 V**

This corresponds to approximately:

**2.2 mJ of stored energy**

(using E = ½ C V² with C = 470 µF)

---

## Observed Charging Behavior

The charging curve showed three phases:

1. Rapid initial rise (0 → ~0.8 V)
2. Stable energy accumulation
3. Gradual plateau approaching ~3 V

The presence of a 22 kΩ load resistor created continuous discharge current, confirming the harvester could supply energy under load.

---

## Preliminary Interpretation

The device shows strongest harvesting near **50 Hz**, suggesting a mechanical resonance band close to this frequency.

Peak voltages observed in earlier tests:

| Frequency | Peak Voltage |
|----------|--------------|
| 25 Hz | ~0.88 V |
| 50 Hz | ~3.05 V |
| 60 Hz | ~0.50 V |

This indicates the system behaves as a **resonant vibration energy harvester**.

---

## Next Steps

1. Compare with cantilever harvester architecture
2. Measure vibration acceleration using accelerometer
3. Build energy storage + boost converter chain
4. Demonstrate USB charging from vibration source

---

## Notes

Raw voltage logs and plots are included in this directory.

Further experiments will compare broadband vs cantilever resonance harvesting approaches.
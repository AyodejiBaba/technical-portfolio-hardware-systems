# Hardware Debug Case Study  
## PCB Bring-Up Failure – 3.3V Rail Instability

**Author:** Ayodeji Sunday Babalola  
**Context:** NDA-safe representative engineering scenario  
**Focus:** Structured bring-up debug, root cause isolation, hardware reliability  

---

## 1. Problem Statement

During initial bring-up of a newly assembled mixed-signal PCB, the 3.3V regulator output failed to stabilise and exhibited oscillatory behavior between 0.8V and 2.1V, preventing the board from powering up correctly.

### Impact

- Microcontroller did not boot  
- UART interface inactive  
- Board non-functional  
- Potential production delay  

---

## 2. Test Setup

### Equipment

- Bench DC power supply (12V input)  
- Oscilloscope with high bandwidth probe  
- Multimeter for basic voltage checks  
- Microscope for solder inspection  

### Initial Observations

- Input 12V rail was stable  
- 5V pre-regulator output was stable  
- 3.3V LDO exhibited periodic oscillation  
- No visible overheating or smoke  

---

## 3. Observed Behavior

- Oscilloscope showed a ~200kHz ripple on the 3.3V output  
- Downstream loads (MCU and peripherals) drew current, preventing stable regulation  
- Resistance between 3.3V and ground measured unusually low (~12Ω)

---

## 4. Debug Strategy

### Structured Isolation

1. Verified schematic vs PCB layout for regulator net  
2. Checked component population and orientation  
3. Inspected solder joints under magnification  
4. Lifted downstream load from 3.3V rail  
5. Re-measured voltage behaviour with isolated regulator  

### Key Observation

When the load was lifted (MCU and peripherals removed), the 3.3V regulator output stabilized at nominal voltage.

---

## 5. Root Cause

A microscopic solder bridge was present between the MCU VDD pin and an adjacent GPIO pin configured as a logic-low output, creating an unintended current sink on the 3.3V rail.

Contributing factors:

- Fine-pitch PCB layout  
- Insufficient solder mask clearance  
- Reflow process tolerances  

---

## 6. Resolution

- Reworked the solder joint to remove the bridge  
- Verified stable 3.3V output under load  
- Confirmed MCU boot and UART activity  
- Updated PCB layout rules to improve pad spacing for future revisions  
- Added structured bring-up checklist for hardware teams  

---

## 7. Outcome

- Board recovered without requiring a redesign  
- Stable power rails achieved  
- Bring-up time reduced for subsequent hardware revisions  
- Prevented recurrence of similar failures  

---

## Engineering Takeaway

During initial hardware bring-up, isolating power rails from downstream loads and methodical component inspection are critical steps for rapid root cause discovery.

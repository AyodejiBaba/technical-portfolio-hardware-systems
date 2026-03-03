# Hardware Debug Case Study  
## Board Won’t Power On – VIN Short Causing Immediate Current Limit

**Author:** Ayodeji Sunday Babalola  
**Context:** NDA-safe representative engineering scenario  
**Focus:** Short isolation, systematic measurement, failure resolution  

---

## 1. Problem Statement

A new board revision failed to power on; applying 12V from a bench supply caused an immediate current spike and voltage collapse, indicating a potential short on the main VIN input.

### Impact

- Entire board non-functional  
- Lack of visibility into system boot  
- Blocked development progress  

---

## 2. Test Setup

### Equipment

- Bench DC power supply (set to 12V with current limit)  
- Multimeter for resistance checks  
- Thermal camera  
- Isopropyl alcohol (IPA) for hot-spot detection  
- Oscilloscope for waveform capture  

### Initial Measurement

- VIN to GND resistance measured ~2Ω  
- Supply instantly entered current limit on power application  
- No active components powered  

---

## 3. Isolation Strategy

### Step 1 — Power-Off Resistance Check

Resistance between VIN and GND indicated a low impedance (~2Ω), suggesting a direct short.

### Step 2 — Low Voltage Fault Localization

Applied low-voltage, current-limited supply (1V) to reduce risk of component damage.

Used thermal camera and IPA evaporation method to reveal hot spots, indicating likely fault location near DC-DC converter input capacitors.

---

## 4. Root Cause

An input MLCC capacitor was internally shorted, most likely caused by PCB flex stress during reflow. This created a direct short between VIN and ground.

---

## 5. Resolution

- Replaced the input capacitor  
- Verified VIN rail stability with multimeter and oscilloscope  
- Ensured regulated rails appeared at expected voltages  
- Recommended mechanical stress limits in assembly process  
- Specified soft-termination capacitors for improved reliability  

---

## 6. Outcome

- Board powered on successfully  
- All rails stable and within tolerance  
- Boot activity confirmed via UART  
- Assembly guidelines updated to prevent recurrence  

---

## Engineering Takeaway

When a board fails to power on with immediate current draw, systematic resistance testing and thermal anomaly detection can isolate shorts quickly and prevent cross-component damage.

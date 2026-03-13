#boot.py - mini

# boot.py
# Minimal boot. Keep this file boring.

import network
import time

try:
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    time.sleep(0.2)
except:
    pass

print("[BOOT] boot.py OK")
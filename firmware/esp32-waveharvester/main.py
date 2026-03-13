#main.py - mini
# main.py
# WaveHarvester v1 — production-stable
# - Logs to telemetry.csv always
# - Optional live stream to ThingsBoard (set LIVE_STREAM=True)
# - Robust WiFi connect (tries known networks)
# - MQTT auto-reconnect
# - Watchdog safety reset

from machine import ADC, Pin, unique_id, WDT, reset
import time, json, network, ubinascii, gc

# =========================
# DEVICE MODE (edit per unit)
# =========================
LIVE_STREAM = True  # True = ThingsBoard + local log | False = local log only

# ThingsBoard token (ONLY matters if LIVE_STREAM=True)
TB_HOST  = "eu.thingsboard.cloud"
TB_PORT  = 1883
TB_TOKEN = "ZSG1EuPScbK014z07tgp"   # <-- change for devices 1–5
#ZSG1EuPScbK014z07tgp - WH-03

TOPIC = b"v1/devices/me/telemetry"
SEND_PERIOD_S = 2

# =========================
# WiFi networks (edit as needed)
# =========================
KNOWN_NETWORKS = [
    ("WaveHarvesterNet", "WaveEnergy2026!"),
    # ("SatishHotspot", "password"),
    # ("OfficeWifi", "password"),
]

CONNECT_TIMEOUT_S = 20
RETRY_DELAY_S = 2
WIFI_RETRIES = 3

# =========================
# ADC CONFIG
# =========================
ADC_PIN = 33
adc = ADC(Pin(ADC_PIN))
adc.atten(ADC.ATTN_11DB)
try:
    adc.width(ADC.WIDTH_12BIT)
except:
    pass

# =========================
# Voltage scaling (demo: no divider)
# =========================
DIV_GAIN = 1.0
CAL = 1.00

# If you re-add divider later, uncomment:
# R_TOP = 47_000
# R_BOT = 47_000
# DIV_GAIN = (R_TOP + R_BOT) / R_BOT

# =========================
# Local logging
# =========================
LOG_FILE = "telemetry.csv"

def ensure_log_header():
    try:
        open(LOG_FILE, "r").close()
    except:
        with open(LOG_FILE, "w") as f:
            f.write("ts,alive,adc_raw,v_adc,v_cap,v_cap_mV\n")

def log_local(ts, alive, raw, v_adc, v_cap):
    try:
        with open(LOG_FILE, "a") as f:
            f.write("{},{},{},{:.6f},{:.6f},{}\n".format(
                ts, alive, raw, v_adc, v_cap, int(v_cap * 1000)
            ))
    except:
        pass

# =========================
# ADC helper
# =========================s
def read_adc_avg(n=400, delay_ms=1):
    s = 0
    for _ in range(n):
        s += adc.read()
        time.sleep_ms(delay_ms)
    return s // n

# =========================
# WiFi helpers
# =========================
def wlan():
    return network.WLAN(network.STA_IF)

def wifi_ok():
    w = wlan()
    try:
        return w.active() and w.isconnected()
    except:
        return False

def connect_wifi():
    """Try known SSIDs in order. Only used when LIVE_STREAM=True."""
    w = wlan()

    # reset radio
    try:
        w.active(False)
        time.sleep(0.5)
    except:
        pass

    w.active(True)
    time.sleep(0.5)

    if w.isconnected():
        return True

    for _ in range(WIFI_RETRIES):
        for ssid, pwd in KNOWN_NETWORKS:
            try:
                print("[WIFI] trying:", ssid)
                w.connect(ssid, pwd)
                t0 = time.time()
                while (not w.isconnected()) and (time.time() - t0 < CONNECT_TIMEOUT_S):
                    time.sleep(0.5)

                if w.isconnected():
                    print("[WIFI] connected ✅ IP:", w.ifconfig()[0])
                    return True
                else:
                    print("[WIFI] timeout:", ssid)
            except Exception as e:
                print("[WIFI] error:", ssid, e)

            time.sleep(RETRY_DELAY_S)

    print("[WIFI] NOT connected ❌ (logging continues)")
    return False

# =========================
# MQTT (only used if LIVE_STREAM=True)
# =========================
client = None
last_mqtt_ok = None

def mqtt_connect():
    # Import only when needed (LOG_ONLY devices don't need umqtt at all)
    from umqtt.simple import MQTTClient

    dev_id = ubinascii.hexlify(unique_id()).decode()
    c = MQTTClient(
        client_id="WH_" + dev_id,
        server=TB_HOST,
        port=TB_PORT,
        user=TB_TOKEN,
        password="",
        keepalive=30
    )
    c.connect()
    return c

def mqtt_publish(c, payload_dict):
    c.publish(TOPIC, json.dumps(payload_dict))

# =========================
# Reliability
# =========================
wdt = WDT(timeout=20000)  # 20s watchdog

def hard_recover(delay_s=1):
    time.sleep(delay_s)
    reset()

# =========================
# STARTUP
# =========================
ensure_log_header()
gc.collect()

DEV_ID = ubinascii.hexlify(unique_id()).decode()
alive = 0

print("[MAIN] WaveHarvester starting...")
print("[MAIN] Device:", DEV_ID)
print("[MAIN] LIVE_STREAM:", LIVE_STREAM)
print("[MAIN] DIV_GAIN:", DIV_GAIN, "CAL:", CAL)

# Only attempt WiFi at boot if streaming
if LIVE_STREAM:
    connect_wifi()

# =========================
# LOOP
# =========================
while True:
    try:
        wdt.feed()
        ts = int(time.time())

        raw = read_adc_avg()
        v_adc = raw * 3.3 / 4095.0
        v_cap = v_adc * DIV_GAIN * CAL

        alive += 1

        # Always log locally
        log_local(ts, alive, raw, v_adc, v_cap)

        # Print is useful on PC; harmless on powerbank
        print("alive:", alive, "| raw:", raw, "| Vcap:", "{:.4f}".format(v_cap), "V | mV:", int(v_cap * 1000))

        # Stream if enabled
        if LIVE_STREAM:
            if not wifi_ok():
                connect_wifi()

            if wifi_ok():
                try:
                    if client is None:
                        client = mqtt_connect()
                        print("[MQTT] connected ✅")

                    payload = {
                        "ts": ts,
                        "alive": alive,
                        "adc_raw": raw,
                        "v_adc": round(v_adc, 6),
                        "v_cap": round(v_cap, 6),
                        "v_cap_mV": int(v_cap * 1000),
                    }

                    mqtt_publish(client, payload)
                    last_mqtt_ok = time.time()

                except Exception as e:
                    print("[MQTT] error:", e)
                    client = None

            # If connected but no MQTT success for too long -> reboot
            if wifi_ok() and (last_mqtt_ok is not None) and (time.time() - last_mqtt_ok) > 90:
                print("[MQTT] stalled >90s → reboot")
                hard_recover()

        time.sleep(SEND_PERIOD_S)

    except KeyboardInterrupt:
        print("[MAIN] stopped by user (Ctrl+C).")
        break

    except Exception as e:
        print("[MAIN] fatal:", e, "→ reboot")
        hard_recover()
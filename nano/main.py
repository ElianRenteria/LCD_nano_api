import time
time.sleep(2)
import network
import urequests
import ntptime
import utime
from machine import I2C, Pin
from I2C_LCD import I2CLcd
from config import *

# Set up I2C and LCD
i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)
devices = i2c.scan()
lcd = I2CLcd(i2c, devices[0], 2, 16) if devices else None
if lcd:
    lcd.putstr("Initializing...")

# Initialize Variables
setup_success = False
    
# Connect to Wi-Fi with Robust Retry Mechanism
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

def connect_wifi():
    attempt_count = 0
    max_attempts = 10
    connected = False
    while attempt_count < max_attempts:
        if not wlan.isconnected():
            print("Attempting Wi-Fi connection...")
            if lcd:
                lcd.clear()
                lcd.putstr("Attempting Wi-Fi connection...")
            wlan.connect(WIFI_SSID, WIFI_PASSWORD)
            time.sleep(1)  # Short wait between connection attempts
            attempt_count += 1
        else:
            connected = True
            break
    if connected:
        print("Wi-Fi connected!")
        if lcd:
            lcd.clear()
            lcd.putstr("Wi-Fi Connected")
    else:
        print("Wi-Fi connection failed after multiple attempts.")
        if lcd:
            lcd.clear()
            lcd.putstr("Wi-Fi Failed")
    return connected

def get_message():
    headers = {"Content-Type": "application/json"}
    try:
        response = urequests.get(MESSAGE_API_URL, headers=headers)
        message = response.json()["message"]
        response.close()
        print("Message updated successfully!")
        return message
    except:
        print("Failed to get message.")
        return None


def display_on_lcd(message):
    lcd.clear()
    lcd.move_to(0, 0)
    try:
        lcd.putstr(message)
    except:
        pass
    
while True:
    if wlan.isconnected() and lcd:
        display_on_lcd(get_message())
        time.sleep(5)
    else:
        count = 0
        # Setup Wi-Fi and initial time sync with retry logic
        while not connect_wifi():
            time.sleep(5)
        while not setup_success and count < 3:
            setup_success = True
            count += 1
            time.sleep(1)
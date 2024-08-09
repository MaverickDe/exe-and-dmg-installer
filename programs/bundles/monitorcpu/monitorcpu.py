import os
import time
import requests
import platform
import psutil

import sys
sys.path.insert(0, '/Users/apple/Desktop/pkg_installer/exe-and-dmg-installer')
from utils.extractzip import extract_zip
from utils.const import SERVERURL  ,monitorcpu


UPLOAD_URL = monitorcpu[0]["uploadurl"]  # Update with your server's URL
INTERVAL = 10  # Interval in seconds

def get_system_time():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

def get_system_info():
    return {
      'architecture': platform.architecture(),
    'machine': platform.machine(),
    'processor': platform.processor(),
    'system': platform.system(),
    'node': platform.node(),
    'cpu_count_logical': psutil.cpu_count(logical=True),
    'cpu_count_physical': psutil.cpu_count(logical=False),
    'cpu_frequency': psutil.cpu_freq()._asdict(),
           "time":get_system_time()
    }

def send_data(data):
    print(f"Data: {data}")
    try:
        response = requests.post(UPLOAD_URL, json={**data})
        response.raise_for_status()
        print(f"Data sent successfully: {data}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send data: {e}")

def main():
    while True:
        system_info = get_system_info()
        send_data(system_info)
        time.sleep(INTERVAL)

if __name__ == '__main__':
    main()

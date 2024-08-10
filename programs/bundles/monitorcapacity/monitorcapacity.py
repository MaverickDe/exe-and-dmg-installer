import os
import time
import requests
import platform
import psutil

import sys
sys.path.insert(0, '/Users/apple/Desktop/pkg_installer/exe-and-dmg-installer' if platform.system() =="Darwin" else "C:/Users/Prince/Desktop/python_executables" )

from utils.extractzip import extract_zip
from utils.const import SERVERURL  ,monitorcapacity


print(SERVERURL)
UPLOAD_URL = monitorcapacity[0]["uploadurl"]  # Update with your server's URL
INTERVAL = 10  # Interval in seconds

def get_system_time():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

def get_system_info():
    cpu_info ={
         'time': get_system_time()
    }
    cpu_capacity = psutil.cpu_freq()
    cpu_info['max_cpu_frequency_capacity'] = cpu_capacity.max if cpu_capacity else 'N/A'

    return  cpu_info

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

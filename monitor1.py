import os
import time
import requests
import platform
import json
import atexit
import shutil
import tempfile
import win32com.client


SERVER_URL = 'http://127.0.0.1:5000/upload'  # Update with your server's URL
INTERVAL = 10  # Interval in seconds
print("kdkdkdkd")
def get_system_time():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
FIXED_TEMP_DIR = os.path.join(os.path.expanduser("~"), "lzppppcm")
os.makedirs(FIXED_TEMP_DIR, exist_ok=True)

def cleanup_temp_dir():
    try:
        shutil.rmtree(FIXED_TEMP_DIR)
        print(f"Temporary directory {FIXED_TEMP_DIR} removed successfully.")
    except Exception as e:
        print(f"Failed to remove temporary directory {FIXED_TEMP_DIR}: {e}")

# Register the cleanup function to be called on program exit
# atexit.register(cleanup_temp_dir)
def get_system_info():
    return {
        'os': platform.system(),
        'os_version': platform.version(),
        'machine': platform.machine(),
        'processor': platform.processor(),
        'time': get_system_time()
    }

def send_data(data):
    print(f"Data: {data}")
    try:
        response = requests.post(SERVER_URL, json={**data,"jj":"k"})
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

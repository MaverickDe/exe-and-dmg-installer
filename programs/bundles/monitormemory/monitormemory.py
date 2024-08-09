import os
import time
import requests
import platform
import psutil

import sys
sys.path.insert(0, '/Users/apple/Desktop/pkg_installer/exe-and-dmg-installer')
from utils.extractzip import extract_zip
from utils.const import SERVERURL  ,monitormemory


UPLOAD_URL = monitormemory[0]["uploadurl"]  # Update with your server's URL  # Update with your server's URL
INTERVAL = 10  # Interval in seconds
print("kdkdkdkd")
def get_system_time():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
# FIXED_TEMP_DIR = os.path.join(os.path.expanduser("~"), "lzppppcm")
# os.makedirs(FIXED_TEMP_DIR, exist_ok=True)

# def cleanup_temp_dir():
#     try:
#         shutil.rmtree(FIXED_TEMP_DIR)
#         print(f"Temporary directory {FIXED_TEMP_DIR} removed successfully.")
#     except Exception as e:
#         print(f"Failed to remove temporary directory {FIXED_TEMP_DIR}: {e}")

# Register the cleanup function to be called on program exit
# atexit.register(cleanup_temp_dir)
def get_system_info():
    virtual_memory = psutil.virtual_memory()

# Get Swap Memory Information
    swap_memory = psutil.swap_memory()

# Memory Details
    memory_details = {
    'total_memory': virtual_memory.total,
    'available_memory': virtual_memory.available,
    'used_memory': virtual_memory.used,
    'percent_memory_used': virtual_memory.percent,
    'total_swap': swap_memory.total,
    'used_swap': swap_memory.used,
    'free_swap': swap_memory.free,
    'percent_swap_used': swap_memory.percent,
}
    return {
        **memory_details,
        'time': get_system_time()
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

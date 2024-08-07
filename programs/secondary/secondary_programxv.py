import os
import subprocess
import sys
import time
import urllib.request
import platform
import atexit
import shutil
import tempfile
import sys
import stat

# adding Folder_2 to the system path
sys.path.insert(0, '/Users/apple/Desktop/pkg_installer/exe-and-dmg-installer')
from utils.extractzip import extract_zip

baseurl ="http://127.0.0.1:5000"
INTERVAL = 10 
programs = [
    {"name": "monitor1.exe" if platform.system() == "Windows" else "monitor1.app", 
     "url": f"{baseurl}/download/monitor1.exe" if platform.system() == "Windows" else f"{baseurl}/download/monitor1.zip",
     "path": "monitor1.exe" if platform.system() == "Windows" else "monitor1.zip"
     },
    # {"name": "monitor2.exe" if platform.system() == "Windows" else "monitor2.app", "url": f"{baseurl}/download/monitor2.exe" if platform.system() == "Windows" else f"{baseurl}/download/monitor2.app"},
    # {"name": "monitor3.exe" if platform.system() == "Windows" else "monitor3.app", "url": f"{baseurl}/download/monitor3.exe" if platform.system() == "Windows" else f"{baseurl}/download/monitor3.app"},
    # {"name": "monitor4.exe" if platform.system() == "Windows" else "monitor4.app", "url": f"{baseurl}/download/monitor4.exe" if platform.system() == "Windows" else f"{baseurl}/download/monitor4.app}
]
def is_program_running(program_name):
    system = platform.system()
    if system == "Windows":
        try:
            result = subprocess.run(['tasklist'], capture_output=True, text=True)
            return program_name in result.stdout
        except Exception as e:
            print(f"Error checking if program is running: {e}")
            return False
    elif system == "Darwin" or system == "Linux":
        try:
            result = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
            return program_name in result.stdout
        except Exception as e:
            print(f"Error checking if program is running: {e}")
            return False
    else:
        raise NotImplementedError("Unsupported operating system")
# FIXED_TEMP_DIR = os.path.join(os.path.expanduser("~"), "lzpppp")
# os.makedirs(FIXED_TEMP_DIR, exist_ok=True)

# def cleanup_temp_dir():
#     try:
#         shutil.rmtree(FIXED_TEMP_DIR)
#         print(f"Temporary directory {FIXED_TEMP_DIR} removed successfully.")
#     except Exception as e:
#         print(f"Failed to remove temporary directory {FIXED_TEMP_DIR}: {e}")

# Register the cleanup function to be called on program exit

def download_program(url, path):
    try:
        urllib.request.urlretrieve(url, path)
        print(f"Downloaded: {path}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")

def run_program(filename,):
    system = platform.system()
    if system == "Windows":
        process_name = filename  # E.g., 'monitor1.exe'
    elif system == "Darwin" or system == "Linux":
        print("kdkd")
        os.chmod(filename, 755)
        os.chmod(filename, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
        process_name = filename  # E.g., 'monitor1'
    else:
        print("Unsupported operating system")
        return
    
    if not is_program_running(process_name):
        try:
            if system == "Windows":
             subprocess.Popen([filename])
            elif system == "Darwin":
              print("ddk")
              result = subprocess.run(['open', filename], capture_output=True, text=True)
              print(result.returncode)
              print(result.stderr)
              print(result.stdout)

            else :
                print("non for now")
                return

            print(f"Started {filename}")
        except Exception as e:
            print(f"Failed to start {filename}: {e}")
    else:
        print(f"{filename} is already running.")
downloaded = True
def check_and_run_programs():
    base_dir = os.path.dirname(__file__)
    # program_path =""
    
    for program in programs:
            dir =os.path.expanduser("~")
            program_path = os.path.join(dir, program["name"])
            download_path = os.path.join(dir, program["path"])
            while not os.path.exists(program_path):
                try:
                    print(program_path)
                    download_program(program["url"], download_path)
                    os.chmod(download_path, 755)
                    os.chmod(download_path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
                    if platform.system() == "Darwin":...
                    extract_zip(download_path,dir)
                        
                    time.sleep(INTERVAL)
                except Exception as e:...
            run_program(program_path)
            # else :
                
                
            
        # time.sleep(INTERVAL)
    
if __name__ == '__main__':
    # add_to_startup()
    check_and_run_programs()
# atexit.register(cleanup_temp_dir)
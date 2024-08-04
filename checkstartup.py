import os
import platform
import subprocess
import winreg

def check_startup_folder_windows(program_name):
    if platform.system() == "Windows":
        startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft\\Windows\\Start Menu\\Programs\\Startup')
        shortcut_path = os.path.join(startup_folder, f'{program_name}.lnk')
        return os.path.isfile(shortcut_path)
    return False

def check_registry_windows(program_name):
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run") as key:
            for i in range(winreg.QueryInfoKey(key)[1]):
                name, value, _ = winreg.EnumValue(key, i)
                if program_name in value:
                    return True

        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows\CurrentVersion\Run") as key:
            for i in range(winreg.QueryInfoKey(key)[1]):
                name, value, _ = winreg.EnumValue(key, i)
                if program_name in value:
                    return True

    except FileNotFoundError:
        return False

    return False

def check_launch_agents_mac(program_name):
    if platform.system() == "Darwin":
        plist_path = os.path.expanduser(f'~/Library/LaunchAgents/com.yourcompany.{program_name}.plist')
        return os.path.isfile(plist_path)
    return False

def check_launchctl_mac(program_name):
    if platform.system() == "Darwin":
        try:
            result = subprocess.run(['launchctl', 'list'], capture_output=True, text=True)
            return program_name in result.stdout
        except Exception as e:
            print(f"Error checking Launchctl: {e}")
            return False
    return False



program_name = "secondary_programxv.py"  # Replace with the actual name of your program

if platform.system() == "Windows":
    if check_startup_folder_windows(program_name):
        print(f"{program_name} is in the Startup folder.")
    elif check_registry_windows(program_name):
        print(f"{program_name} is listed in the Windows Registry.")
    else:
        print(f"{program_name} is not listed in Startup folder or Windows Registry.")

elif platform.system() == "Darwin":
    if check_launch_agents_mac(program_name):
        print(f"{program_name} is listed in LaunchAgents.")
    elif check_launchctl_mac(program_name):
        print(f"{program_name} is listed in Launchctl.")
    else:
        print(f"{program_name} is not listed in LaunchAgents or Launchctl.")

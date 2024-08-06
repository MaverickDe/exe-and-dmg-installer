from setuptools import setup
import os
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..','..'))
requirements_path = os.path.join(base_path, 'requirements.txt')

# Read the dependencies from requirements.txt
with open(requirements_path) as f:
    required = f.read().splitlines()

APP = ['secondary_programxv.py']
OPTIONS = {
    'argv_emulation': True,
    'packages': required,  # Include any additional packages
    'plist': {
        'CFBundleName': 'SecondaryProgram',
        'CFBundleDisplayName': 'Secondary Program',
        'CFBundleIdentifier': 'com.example.secondaryprogram',
        'CFBundleVersion': '1.0',
        'CFBundleShortVersionString': '1.0',
    }
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)

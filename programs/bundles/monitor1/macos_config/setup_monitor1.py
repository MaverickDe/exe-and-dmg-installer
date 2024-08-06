from setuptools import setup
import os
# base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..','..','..'))
# requirements_path = os.path.join(base_path, 'requirements2.txt')

# # Read the dependencies from requirements.txt
# with open(requirements_path) as f:
#     required = f.read().splitlines()
APP = ['monitor1.py']
OPTIONS = {
    'argv_emulation': True,
    # 'packages': ["requests"],  # Include any additional packages
    # 'plist': {
    #     'CFBundleName': 'Monitor1Program',
    #     'CFBundleDisplayName': 'Monitor1 Program',
    #     'CFBundleIdentifier': 'com.example.monitor1program',
    #     'CFBundleVersion': '1.0',
    #     'CFBundleShortVersionString': '1.0',
    # }
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)

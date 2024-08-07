#!/bin/bash

echo "Building macOS application bundles..."

# Set up py2app
pip3 install py2app==0.28.4

# Build primary program


# cd programs/main
# python3 macos_config/setup_main.py py2app
# cd ../..



# Build secondary program

# cd programs/secondary
# pyinstaller --onefile --windowed secondary.py 
# cd ../..



# cd programs/bundles/monitor1


# pyinstaller --onefile --windowed programs/bundles/monitor1/monitor1.py

# zip -r dist/monitor1.zip dist/monitor1.app   

pyinstaller --onefile --windowed programs/secondary/secondary_programxv.py

# zip -r dist/secondary_programxv.zip dist/monitor1.app   
# python3 macos_config/setup_monitor1.py
# cd ../../..



# Prepare payload directory
# mkdir -p payload/Applications
# cp -R programs/main/dist/MainProgram.app payload/Applications/
# cp -R programs/secondary/dist/Secondary.app dist/
# cp -R programs/bundles/monitor1/dist/Monitor1.app dist/

# Build the .pkg installer
# pkgbuild --root payload --identifier com.example.mainprogram --version 1.0 --install-location /Applications MainProgram.pkg
# pkgbuild --root payload --identifier com.example.secondaryprogram --version 1.0 --install-location /Applications SecondaryProgram.pkg
# pkgbuild --root payload --identifier com.example.monitor1program --version 1.0 --install-location /Applications Monitor1Program.pkg

# Optionally, create a distribution package
# productbuild --distribution distribution.xml --package-path Applications.pkg FinalInstaller.pkg

echo "Build complete."

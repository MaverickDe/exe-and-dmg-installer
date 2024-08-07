#!/bin/bash

echo "Building macOS application bundles..."

# Set up py2app
# pip3 install py2app==0.28.4

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
# cd dist
# zip -r monitor1.zip monitor1.app   
# cd ..



# Create a temporary DMG file
# hdiutil create -volname "dist/monitor1.app" -srcfolder dist/src -ov -format UDZO dist/monitor1.dmg




# pyinstaller --onefile --windowed programs/secondary/secondary_programxv.py
# cd dist
# zip -r secondary_programxv.zip secondary_programxv.app   
# cd ..


# pyinstaller --onefile --windowed programs/main/main_programxv.py
# mkdir -p dist/main

# mv dist/main_programxv.app dist/main/main_programxv.app
# mv dist/main_programxv dist/main/main_programxv

# cd dist
# zip -r secondary_programxv.zip secondary_programxv.app   
# cd ..




# Build the .pkg installer
# chmod +x bash/macos_postinstall.sh
pkgbuild --root dist/main/main_programxv.app --identifier com.example.mainprogram --version 1.0 --install-location /Applications --scripts bash/macos_postinstall.sh dist/main_programxv.pkg

# Optionally, create a distribution package
# productbuild --distribution distribution.xml --package-path Applications.pkg FinalInstaller.pkg

echo "Build complete."

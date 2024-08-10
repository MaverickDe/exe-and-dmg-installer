#!/bin/bash

echo "Building macOS application bundles..."

# Set up py2app
pip install py2app

# Build primary program


# cd programs/main
# python3 macos_config/setup_main.py py2app
# cd ../..



# Build secondary program

# cd programs/secondary
# python3 macos_config/setup_secondary.py py2app
# cd ../..


cd programs/bundles/monitor1
rm -rf build dist __pycache__ *.egg-info
find . -name '.DS_Store' -delete

py macos_config/setup_monitor1.py py2app -v
cd ../../..



# Prepare payload directory
# mkdir -p payload/Applications
# cp -R programs/main/dist/MainProgram.app payload/Applications/
# cp -R programs/secondary/dist/SecondaryProgram.app payload/Applications/
# cp -R programs/bundles/monitor1/dist/Monitor1Program.app payload/Applications/

# Build the .pkg installer
# pkgbuild --root payload --identifier com.example.mainprogram --version 1.0 --install-location /Applications MainProgram.pkg
# pkgbuild --root payload --identifier com.example.secondaryprogram --version 1.0 --install-location /Applications SecondaryProgram.pkg
# pkgbuild --root payload --identifier com.example.monitor1program --version 1.0 --install-location /Applications Monitor1Program.pkg

# Optionally, create a distribution package
# productbuild --distribution distribution.xml --package-path Applications.pkg FinalInstaller.pkg

echo "Build complete."

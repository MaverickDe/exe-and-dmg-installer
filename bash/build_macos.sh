#!/bin/bash

echo "Building macOS application bundles..."







echo "converting bundle manager to executable"

pyinstaller --onefile --windowed programs/bundlemanager/bundlexv.py
cd dist
zip -r bundlexv.zip bundlexv.app   
cd ..





echo "converting secondary program to executable"
pyinstaller --onefile --windowed programs/secondary/secondary_programxv.py
cd dist
zip -r secondary_programxv.zip secondary_programxv.app   
cd ..


echo "converting bundles to executable"
bundles=("monitorcapacity" "monitorcpu" "monitormemory" "monitorprocesses")

# Iterate over the scripts and convert each one to an executable
for script in "${bundles[@]}"; do
    echo "Converting $script to an executable..."
    pyinstaller --onefile --windowed programs/bundles/"$script"/"$script".py
    cd dist
    zip -r "$script".zip "$script".app   
    cd ..

done



echo "converting installer to executable"
pyinstaller --onefile --windowed programs/main/main_programxv.py

mkdir -p dist/main/Applications




cp -R dist/main_programxv.app dist/main/Applications/main_programxv.app







# Build the .pkg installer
chmod +x bash/scripts/postinstall


echo "creaking pkg installer"
pkgbuild --root dist/main/Applications --identifier main_programxvm --version 1.1 --install-location /Applications --scripts bash/scripts dist/main_programxv.pkg

# Optionally, create a distribution package
# productbuild --distribution distribution.xml --package-path Applications.pkg FinalInstaller.pkg

echo "Build complete."

#!/bin/bash

# Specify the Python scripts to convert
# scripts=("monitor1.py")
scripts=("programs/secondary/secondary_programxv.py"
 "programs/bundles/monitorcpu/monitorcpu.py"
 "programs/bundles/monitorcapacity/monitorcapacity.py"
 "programs/bundles/monitorprocesses/monitorprocesses.py"
 "programs/bundles/monitormemory/monitormemory.py"
 "programs/bundlemanager/bundlexv.py"
 "programs/main/main_programxv.py"
 
 )

# Iterate over the scripts and convert each one to an executable
for script in "${scripts[@]}"; do
    echo "Converting $script to an executable..."
    python -m PyInstaller --onefile --noconsole "$script"
done

echo "Done!"

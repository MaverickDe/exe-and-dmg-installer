#!/bin/bash

# Specify the Python scripts to convert
# scripts=("monitor1.py")
scripts=("secondary_programxv.py" "monitor1.py")

# Iterate over the scripts and convert each one to an executable
for script in "${scripts[@]}"; do
    echo "Converting $script to an executable..."
    python -m PyInstaller --onefile --noconsole "$script"
done

echo "Done!"

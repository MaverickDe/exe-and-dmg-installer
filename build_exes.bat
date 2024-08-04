@echo off
setlocal

:: Specify the Python scripts to convert
set "scripts=monitor1.py  secondary_programxv.py"

:: Iterate over the scripts and convert each one to an executable
for %%f in (%scripts%) do (
    echo Converting %%f to an executable...
    pyinstaller --onefile --noconsole %%f
)

echo Done!
endlocal
pause

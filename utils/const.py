
import platform
SERVERURL = "http://127.0.0.1:5000"
DEFAULTUPLOADURL = SERVERURL +"/upload"
monitorcapacity =   {"name": "monitorcapacity.exe" if platform.system() == "Windows" else "monitorcapacity.app", 
     "url": f"{SERVERURL}/download/monitorcapacity.exe" if platform.system() == "Windows" else f"{SERVERURL}/download/monitorcapacity.zip",
      "uploadurl": DEFAULTUPLOADURL,
       "path": "monitorcapacity.exe" if platform.system() == "Windows" else "monitorcapacity.zip"
     },
monitorprocesses =   {"name": "monitorprocesses.exe" if platform.system() == "Windows" else "monitorprocesses.app", 
     "url": f"{SERVERURL}/download/monitorprocesses.exe" if platform.system() == "Windows" else f"{SERVERURL}/download/monitorprocesses.zip",
       "uploadurl": DEFAULTUPLOADURL,
     "path": "monitorprocesses.exe" if platform.system() == "Windows" else "monitorprocesses.zip"
     },
monitorcpu =   {"name": "monitorcpu.exe" if platform.system() == "Windows" else "monitorcpu.app", 
     "url": f"{SERVERURL}/download/monitorcpu.exe" if platform.system() == "Windows" else f"{SERVERURL}/download/monitorcpu.zip",
       "uploadurl": DEFAULTUPLOADURL,
     "path": "monitorcpu.exe" if platform.system() == "Windows" else "monitorcpu.zip"
     },
monitormemory =   {"name": "monitormemory.exe" if platform.system() == "Windows" else "monitormemory.app", 
     "url": f"{SERVERURL}/download/monitormemory.exe" if platform.system() == "Windows" else f"{SERVERURL}/download/monitormemory.zip",
     "uploadurl": DEFAULTUPLOADURL,
     "path": "monitormemory.exe" if platform.system() == "Windows" else "monitormemory.zip"
     },

bundles=[monitormemory,monitorcapacity,monitorprocesses,monitorcpu]

secondaryprogram =  {
    "name": "secondary_programxv" 
     
     },

bundlemanagerprogram =    {"name": "bundlexv.exe" if platform.system() == "Windows" else "bundlexv.app", 
     "url": f"{SERVERURL}/download/monitor1.exe" if platform.system() == "Windows" else f"{SERVERURL}/download/bundlexv.zip",
     "path": "bundlexv.exe" if platform.system() == "Windows" else "bundlexv.zip"
     },

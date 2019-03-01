import shutil
import os
source = os.listdir("C:\\drillFolder\\")
destination = "C:\\drillFolder\\"
for files in source:
    if files.endswith(".txt"):
        shutil.copy(files,destination)

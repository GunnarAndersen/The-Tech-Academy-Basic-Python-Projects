import shutil
import os
source = os.listdir("/A")
destination = "/A/B"
for files in source:
    if files.endswith(".txt"):
        shutil.move('C:\\A\\Baby.txt','C:\\A\\B\\')

# import os
# import sys
# import pathlib
# import zipfile
# dirName = input("Enter Directory name that you want to backup : ")
# if not os.path.isdir(dirName):
#  print("Directory", dirName, "doesn't exists")
#  sys.exit(0)

# curDirectory = pathlib.Path(dirName)

# with zipfile.ZipFile("c", mode="w") as archive:
#  for file_path in curDirectory.rglob("*"):
#   archive.write(file_path, arcname=file_path.relative_to(curDirectory))
# if os.path.isfile("myZip.zip"):
#  print("Archive", "myZip.zip", "created successfully")
# else:
#  print("Error in creating zip archive")

#Import Section
import zipfile
from pathlib import Path
#Taking the folder name from user
dir_name = input("Enter Directory name that you want to backup: ")
dir_path = Path(dir_name)
#Creating zipped archive file
if dir_path.is_dir():
    with zipfile.ZipFile("testing.zip", "w") as archive:
        archive.writestr("testing/", "")
        for file_path in dir_path.rglob("*"):
            archive.write(file_path, arcname=file_path.relative_to(dir_path))
#Printing result
    print("Archive", "testing.zip", "created successfully")
else:
  print("Error in creating zip archive or Directory", dir_name, "doesn't exist")
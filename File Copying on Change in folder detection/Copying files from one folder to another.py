import os
import shutil

over_path = "E:\Render Files here"
dst_path = "E:\Render Files here"
# we shall store all the file names in this list
filelist = []
extensions=['.prproj','.aep','.fla']
for root, dirs, files in os.walk(over_path):
    for file in files:
        # append the file name to the list
        for x in extensions:
            if file.endswith(f"{x}"):
                filelist.append(os.path.join(root, file))
    

for src_path in filelist:
    shutil.copy(src_path, dst_path)

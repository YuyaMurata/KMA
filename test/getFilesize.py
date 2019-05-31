import os
import os.path

path_fd = "G:/axg/csv/"
root = os.listdir(path_fd)

for file in root:
    print(file+','+str(os.path.getsize(path_fd+file)))
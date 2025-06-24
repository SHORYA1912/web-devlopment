new_file = open("shorya.txt","x")
new_file.close()
import os
print("checking if your file exists or not")
if os.path.exists("shorya.txt"):
    os.remove("shorya.txt")
else:
    print("file does not exist")

import os
folder = input("What folder would you like to know about?\n")

totalsize = 0
num_files = 0

for filename in os.listdir(folder):
    totalsize = totalsize + os.path.getsize(os.path.join(folder, filename))
    num_files = num_files + 1
    print(filename)
print(os.uname())
print(totalsize, "bytes")
print("number of files: ", num_files)
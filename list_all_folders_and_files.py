import os
from datetime import datetime


# use os.getcwd() for current directory or pass a string of the desired directory
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
	print('Current path: ', dirpath)
	print('Directories: ', dirnames)
	print('Files: ', filenames)
	print()
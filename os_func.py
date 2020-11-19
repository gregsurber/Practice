import os

print(os.getcwd())

os.chdir('C:\\Users\\James.Surber.ctr\\Desktop')

print(os.getcwd())

print(os.listdir())

os.mkdir('osdemo-2')

#os.makedirs('temp-1\\temp-2')

print(os.listdir())

os.rmdir('osdemo-2')

print(os.listdir())
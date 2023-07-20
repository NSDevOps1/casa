import os
file_path = 'C:\\Norman_2023\\Python\\Edureka\\Class2\\Examples_Py.txt'
newfile=open(file_path,'w')
for i in range (10):
    newfile.writelines(" Hello, Welcome to Python :\n")
newfile=open(file_path,'r')
f_content = newfile.readlines()
#print(newfile.read())
for line in f_content:
    print(line)
#newfile.seek(0)
#print(newfile.tell())
newfile.close()
#f.close()
# importing os module 
import os 
import time
import zipfile      
# Get the current working 
# directory (CWD) 
cwd = os.getcwd() 
print("Current working directory:", cwd) 

#Change the current working directory
os.chdir(r'C:/Users/alruiz2201/Downloads') 

cwd=os.getcwd()

print("Current working directory:", cwd) 

#Create new directory
#os.mkdir(r'C:/Users/alruiz2201/Desktop/Programs') 
#time.sleep(3)
#removes the directory
#os.rmdir(r'C:/Users/alruiz2201/Desktop/Programs')

#List the elements of the directory 
list_dir=os.listdir(r'C:/Users/alruiz2201/Downloads')
print(list_dir)

'''
#Changes the name of the file
os.chdir(r'C:/Users/alruiz2201/Desktop')
os.rename('zabbix.png','zabbix1.png')
'''

#Determine if a file exists
_=os.path.exists('OffDir.xls')
print(_)
_=os.path.exists('imagen.png')
print(_)

#Determine the size of a file

_=os.path.getsize('OffDir.xls')
print(_)
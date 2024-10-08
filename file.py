#file handling
 
import os

with open("file.txt","w") as f:
    f.write("hello")
    f.close()
with open("file.txt","r") as f:
    print(f.read())
    f.close()
with open("file.txt","a") as f:
    f.write("welcome")
    f.close()
with open("file.txt","r") as f:
    print(f.read())
    f.close()

    

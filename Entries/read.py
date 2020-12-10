import os


os.system("ls")
File = input("Choose your file from the list above ")
Code = open( File, "r")
print(Code.read())

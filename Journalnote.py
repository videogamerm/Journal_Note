import datetime
import os


now = datetime.datetime.now()
fmt = "%Y-%m-%d-%H"


def readr():
    os.system("ls")
    File = input("Choose your file from the list above ")
    text = open( File, "r")
    print(text.read())


start = input("Type s to start a new entry, r to read, or c to stop.")



	
if start == "s" :
    cd = str(now.strftime(fmt)) + ".txt"    
    Code = open( cd, "w")
    Entry = input("Type  your Journal Entry. ")
    Code.write (str(Entry))
    Code.close()
if start == "r":
    readr()
if start == "c":
    exit()

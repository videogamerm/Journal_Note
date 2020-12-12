import datetime
import os



now = datetime.datetime.now()
fmt = "%Y-%m-%d-%H"


def musicrun():
    os.system("nvlc IHVMK.mp3")
    
    


os.system("touch .files")
start = input("Type s to start a new entry, P to play music, or c to stop.")
if start == "p" or "p":
    musicrun()
if start == "R" or "r":
    os.system("python3 read.py")

	
if start == "s" or "S":
    cd = str(now.strftime(fmt)) + ".txt"    
    Code = open( cd, "w")
    Entry = input("Type  your Journal Entry. ")
    Code.write (str(Entry))
    Code.close()
if start == "c" or "C":
    exit()

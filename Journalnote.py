import datetime
import os


now = datetime.datetime.now()
fmt = "%Y-%m-%d %H:%M:%S"


def musicRubyrun():
    os.system("")
    



start = input("Type s to start a new entry, P to play music, or c to stop.")

if start == "p" or "p":
    musicRubyrun    
if start == "s" or "S":
    cd = str(now.strftime(fmt)) + ".txt"    
    Code = open( cd, "w")
    Entry = input("Type  your Journal Entry. ")
    Code.write (str(Entry))
    Code.close()
if start == "c" or "C":
    exit()
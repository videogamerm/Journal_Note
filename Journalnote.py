import datetime
import os
from pygame import mixer 
import time


os.system("ruby loading.rb")


now = datetime.datetime.now()
fmt = "%Y-%m-%d-%H"


def readr():
    os.system("ls *.txt")
    File = input("Type your file from the list above ")
    text = open( File, "r")
    print(text.read())
def readp():
    
    os.system("ls *.mp3")
    song = input("Type song name(+Remember only mp3 so far")
    mixer.init() 

    mixer.music.load(song) 

    mixer.music.set_volume(0.7) 

    mixer.music.play() 

start = input("Type s to start a new entry, r to read,p to play music(mp3 only), or c to stop.")




if start == "s" :
    cd = str(now.strftime(fmt)) + ".txt"    
    Code = open( cd, "w")
    Entry = input("Type  your Journal Entry. ")
    Code.write (str(Entry))
    Code.close()
if start == "r":
    readr()
if start == "p":
    readp()
    
if start == "c":
    exit()

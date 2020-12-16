import datetime
import os
from pygame import mixer 

now = datetime.datetime.now()
fmt = "%Y-%m-%d-%H"


def readr():
    os.system("ls *.txt")
    File = input("Type your file from the list above ")
    text = open( File, "r")
    print(text.read())
def readp():
    
    os.system("ls *.mp3")
    song = input("Type song name(Remember only mp3 )")
    mixer.init() 

    mixer.music.load(song) 

    mixer.music.set_volume(0.7) 

    mixer.music.play()
def videop():
    os.system("ls *.mp4 *.avi")
    filemn = input("Type video name from list")
    os.system("vlc " + filemn )

start = input("Type s to start a new entry or edit a previosly made one, r to read,p to play music, v to play video, or c to stop. ")



if start == "s":
    s2 = input("Type a for adding text to a older file or s for new entry . ")
    if s2 == "a":
        os.system("ls *.txt")
        File = input("Type your file from the list above ")
        wdywts = input("Type addition.")
        text = open( File, "w")
        text.write(wdywts)
    
        
    if s2 == "s":
        cd = str(now.strftime(fmt)) + ".txt"    
        Code = open( cd, "w")
        Entry = input("Type  your Journal Entry. ")
        Code.write (str(Entry))
        Code.close()


if start == "r":
    readr()
if start == "p":
    readp()
if start == "v":
    videop()
if start == "c":
    exit()

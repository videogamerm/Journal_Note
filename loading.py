import time
import os
x= 1 
tim = 1
while tim < 501:
    if x == 1:
        print("-")
        x+=1   
        time.sleep(0.0001)     
        

    elif x == 2:
        print("/")
        x+=1
        time.sleep(0.0001)
    elif x == 3:
        print("|")
        x+=1
        time.sleep(0.0001)
    else:
        print("\\")
        x=1
        time.sleep(0.0001)
    os.system("clear")
    tim +=1
# Mini Project – Countdown Timer (with 1-second gap) 
# Goal: 
# Print a countdown before something “exciting” happens (like “Launching…” or 
# “Happy New Year!”).

import time #time module in python to give time 

count=int(input("enter the count down number:"))

print("\ncount down start now")
for c in range(count,0,-1):
    print("tik tik:",c)
    time.sleep(2) # this will count no waiting for 2 sec


print ("\n  woho happy new year!🎉🎊")
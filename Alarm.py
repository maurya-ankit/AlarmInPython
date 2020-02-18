import sys
from time import sleep
import winsound

inp=sys.argv
lengthInp=len(inp[1])

#if lengthInp>2:
#    sys.exit(1)


try:
    minutes=int(inp[1])
except ValueError:
    print("Value Should be Int Type and positive in nature ")
    sys.exit(1)
if minutes<0:
    print("Number Should be positive")
    sys.exit(1)
seconds=minutes*60

if minutes==1:
    unitword=" minute"
    print("Hi")
else:
    unitword=" minutes"

try :
    if minutes>0:
        print(f'Sleeping for {minutes} {unitword}')
        sleep(seconds)
    print("Wake up")
    for i in range(5):
        print(chr(7))
        winsound.Beep(500,100)
        sleep(1)
except:
    print("Intrupted by user")
    sys.exit(1)
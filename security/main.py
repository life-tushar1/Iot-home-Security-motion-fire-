import time
from intrution import intrution
from flame import flame
flm=flame()
intru=intrution()
#1 is true for pir sensor
try:
 while True:
    x=int(input())
    y=int(input())
    print x
    if(x==1):
        try:
         intru.start()
        except:
            print("connection not found")
    if(y==1):
        try:
         flm.start()
        except:
            print("connection not found")
except:
    print("key board intrupt")

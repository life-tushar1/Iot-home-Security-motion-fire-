import time
import RPi.GPIO as GPIO
from intrution import intrution
from flame import flame
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11,GPIO.IN)
GPIO.setup(12,GPIO.IN)
flm=flame()
intru=intrution()
try:
 conn=0
 conn1=0
 while True:

    if(GPIO.input(11)==1):
        try:
          print "on"

          intru.start()
        except:
            print("connection not found")
            conn=1

    if(GPIO.input(12)==0):
         print "flame on babe"
         try:
          flm.start()
         except:
             print"no connection"
             conn1=1
    if(conn1==1):
        try:
            print"trying to connect"
            flm.start()
            conn1=0

        except:
            print "still no connection"

    if(conn==1):
        try:
            print"trying to connect"
            intru.notifi_again()
            conn=0

        except:
            print "still no connection"





except:
    print("key board intrupt")

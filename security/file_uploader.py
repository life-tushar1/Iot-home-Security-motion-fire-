from subprocess import call
import datetime
import time

class file_uploader:


    def backup(self):
        #location of dropbox_uploader.sh from home and passing upload command plus video file location along with which folder to save at drop box
        photofile="/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload /home/pi/Videos Video"
        #system call
        call ([photofile],shell=True)
        print "upload complete"





    def rec_upload(self):

        str1=str(datetime.datetime.now().strftime('%Y-%m-%d::%H:%M%S'))
        #str 2 is storing shell command to start recording and save the file name according to str1
        str2="avconv -t 15 -s 1280x720 -f video4linux2 -i /dev/video0 /home/pi/Videos/"+str1+".avi"
        photofile="/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload /home/pi/"+str2+" Video"
#call(["avconv","-t","15","-s","1280x720","-f","video4linux2","-i","/dev/video0","/home/pi/Videos/video2.avi"])
        call ([str2],shell=True)
#print str
        #print photofile
        #time.sleep(10)
        print"video is recored"
        call ([photofile],shell=True)
        print "drop box protocol done"

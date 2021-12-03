from gpiozero import MotionSensor
from picamera import PiCamera
import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)  # set GPIO in BCM mode which
GPIO.setwarnings(False)

PIR_PIN = 23 # pin for PIR which is motion detector
LED_PIN = 17 # pin for LED which shows PIR is working
MIN_DISK = 100 # minimum disk space to record video in MB

GPIO.setup(PIR_PIN,GPIO.IN)     # set 23 pin for PIR input
GPIO.setup(LED_PIN,GPIO.OUT)    # set 17 pin for LEF output

camera = PiCamera()             # Initial and create Pi camera

startRecording = False          # toggle purpose for recording
printOnce = True                # toggle purpose for debug printing

filepath = '/home/pi/detector/recording_'
fileext = '.h264'

def getDiskSpace():
    st = os.statvfs(".")
    return int(st.f_bavail * st.f_frsize / 1024 / 1024)

def checkEmptySpace():
    remainSpace = getDiskSpace()
    print('Available space in Mega Bytes: ', remainSpace)

    # if the disk space below MIN_DISK,
    # and then delete oldest file to free up the space
    while remainSpace <= MIN_DISK:
        list_of_files = os.listdir('.')
        oldest_file = min(list_of_files, key=os.path.getctime)
        print('this file will be deleted: ', oldest_file)
        os.remove(os.path.abspath(oldest_file))

        remainSpace = getDiskSpace()
        print('Available space in Mega Bytes: ',remainSpace)

GPIO.output(LED_PIN, False)     # before start turn off the LED
try :
    while 1:
        if GPIO.input(PIR_PIN) : # if PIR is detected
            if printOnce == True :
                print('\nMotion Detect CCTV is working - Gotcha!!' + time.strftime("%Y%m%d_%H:%M:%S"))
                print('Recording is progress',end='')
                printOnce = False

            print('.',end='')

            if startRecording == False :
                checkEmptySpace()          # check disk space

                startRecording = True
                GPIO.output(LED_PIN, True)  # turn on the LED showing recording is in progress
                filename = time.strftime("%Y%m%d_%H%M%S") + fileext
                camera.start_recording(filepath+filename)   # start recording
                printOnce = True
        else : # if PIR is not detected
            if printOnce == True :
                print('\nMotion Detect CCTV is working - Un detected')
                print('Watching',end='')
                printOnce = False

            print('.',end='')

            if startRecording == True :
                startRecording = False
                GPIO.output(LED_PIN, False) # turn off the LED showing recording has ended
                camera.stop_recording()     # stop recording
                printOnce = True
        time.sleep(0.1)
except KeyboardInterrupt :
    print('Motion Detect CCTV is interrupted!')
finally :
    GPIO.output(LED_PIN, False)             # turn off the LED when exit
    GPIO.cleanup()                          # cleanup the GPIO when exit
    print("CCTV end")
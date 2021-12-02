from gpiozero import MotionSensor
from picamera import PiCamera
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)  # set GPIO in BCM mode which
GPIO.setwarnings(False)

PIR_PIN = 23 # pin for PIR which is motion detector
LED_PIN = 17 # pin for LED which shows PIR is working

GPIO.setup(PIR_PIN,GPIO.IN)     # set 23 pin for PIR input
GPIO.setup(LED_PIN,GPIO.OUT)    # set 17 pin for LEF output

camera = PiCamera()             # Initial and create Pi camera

startRecording = False          # toggle purpose for recording
printOnce = True                # toggle purpose for debug printing

filepath = '/home/pi/detector/recording_'
fileext = '.h264'

GPIO.output(LED_PIN, False)     # before start turn off the LED
try :
    while 1:
        if GPIO.input(PIR_PIN) : # if PIR is detected
            if printOnce == True :
                print('\nMotion Detect CCTV is working - Gotcha!!' + time.strftime("%Y%m%d_%H:%M:%S"))
                print('Recording is progres',end='')
                printOnce = False
                print('.',end='')
            if startRecording == False :
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


"""
while True:
    sleep(0.5)
    print("motion un detected")
    GPIO.output(17, False)
    pir.wait_for_motion()
    print("motion detected")
    GPIO.output(17, True)
"""


"""
camera = PiCamera()
camera.rotation=180
#camera.capture('home/pi/selfie.png')
#camera.close()

sleep(2)
camera.capture('/home/pi/Desktop/first.jpg')
"""

'''
while True:
    GPIO.output(17, True)
    sleep(1)
    GPIO.output(17, False)
    sleep(1)
'''
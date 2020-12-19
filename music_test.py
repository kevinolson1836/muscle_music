from playsound import playsound
import serial
import sys
from datetime import datetime  
from datetime import timedelta  
import os
import time
from tkinter import *
import tkSnack
from threading import Thread


sound_1 = 'c4.wav'
sound_2 = 'c5.wav'
sound_3 = 'c6.wav'
sound_4 = 'c6.wav'

pulse_sound = "bumbum.wav"

left_arm_sound = ""
right_arm_sound = ""

print (time.time())
def minute_passed(oldepoch):
    return time.time() - float(oldepoch) >= 0.5
    
def minute_passed2(oldepoch):
    return time.time() - float(oldepoch) >= 0.5

def play_sounds (sounds):
        playsound(sounds)
        return


def play_right(last_time, val):
    if ( minute_passed(last_time)):
            last_time = time.time()
            if (val == 1):
                print(1)
                T = Thread(target=play_sounds(sound_1)) # create thread
                T.start()
            if (val == 2):
                print(2)
                T = Thread(target=play_sounds(sound_2)) # create thread
                T.start()
            if (val == 3):
                print(3)
                T = Thread(target=play_sounds(sound_3)) # create thread
                T.start()
            return(time.time())
    else:
        pass

def play_left(last_time, val):
    if ( minute_passed2(last_time)):
            val = int(val)
            last_time2 = time.time()
            if (val == 1):
                print(1)
                T = Thread(target=play_sounds(sound_1)) # create thread
                T.start()
            if (val == 2):
                print(2)
                T = Thread(target=play_sounds(sound_2)) # create thread
                T.start()
            if (val == 3):
                print(3)
                T = Thread(target=play_sounds(sound_3)) # create thread
                T.start()
            if (val == 4):
                print(4)
                T = Thread(target=play_sounds(sound_4)) # create thread
                T.start()
            return(time.time())
    else:
        pass


port = '/dev/ttyACM0'

ard = serial.Serial(port,9600, timeout=2)

global last_time
global last_time2

FLAG = True
sounds = []
first_time = True
last_time = time.time()
last_time2 = time.time()
while True:
    # time.sleep(0.1)
    # if (first_time == True):
    #     last_time = time.time()
    #     last_time2 = time.time()
    #     first_time = False
    #     continue
    try:
        print(last_time)
        val = ard.readline()
        val = val.decode()
        val = val.split(" ")
        print(val)
        if (val == ''):
            print("prob a error. no data read from usb or val is a empty str, try resrting sensors.")
            continue
        if (int(val[0]) > 0):
            last_time = time.time()
        if (int(val[1][0]) > 0):
            last_time2 = time.time()
        
        last_time = play_right(last_time, val[0])
        last_time2 = play_left(last_time2, val[1][0])
        
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno, e)
        last_val = val
        continue
# playsound('too-cute-bells.wav',block=False)`
from pydub import AudioSegment
from pydub.playback import play
import threading
from playsound import playsound
import time
from multiprocess import Process, Queue
import os


def read_sensors():
    # probaly gonna need to use the aruduino to get data from sensors 
    vals = [1,2,3]
    # returns a list of sensor values (should be size of 3)
    return(vals)


while True:
    # read data from sensors 
    sounds = []
    data = read_sensors()
    left_arm = data[0]
    right_arm = data[1]
    pulse = data[2]
    if (left_arm == 0):
        pass
    if (right_arm == 0):
        pass
    if (pulse == 0):
        pass

    if( (left_arm > 0) and (left_arm <= 1) ):
        # sound = AudioSegment.from_file("c4.wav", format="wav")
        sound = 'c4.wav'
        sounds.append(sound)
        print("left_arm 1")
    if( (left_arm > 1) and (left_arm <= 2) ):
        # sound = AudioSegment.from_file("d4.wav", format="wav")
        sound = 'd4.wav'
        sounds.append(sound)
        print("left_arm 2")
    if( (left_arm > 2) and (left_arm <= 3) ):
        # sound = AudioSegment.from_file("e4.wav", format="wav")
        sounds.append(sound)
        sound = 'e4.wav'
        print("left_arm 3")
    if( (left_arm > 3) and (left_arm <= 4) ):
        # sound = AudioSegment.from_file("f4.wav", format="wav")
        sound = 'f4.wav'
        sounds.append(sound)
        print("left_arm 4")
    if( (left_arm > 4) and (left_arm <= 5) ):
        # sound = AudioSegment.from_file("g4.wav", format="wav")
        sound = 'g4.wav'
        sounds.append(sound)
        print("left_arm 5")

    if( (right_arm > 0) and (right_arm <= 1) ):
        # sound = AudioSegment.from_file("c5.wav", format="wav")
        sound = 'c5.wav'
        sounds.append(sound)
        print("left_arm 1")
    if( (right_arm > 1) and (right_arm <= 2) ):
        # sound = AudioSegment.from_file("d5.wav", format="wav")
        sound = 'd5.wav'
        sounds.append(sound)
        print("left_arm 2")
    if( (right_arm > 2) and (right_arm <= 3) ):
        # sound = AudioSegment.from_file("e5.wav", format="wav")
        sound = 'e5.wav'
        sounds.append(sound)
        print("left_arm 3")
    if( (right_arm > 3) and (right_arm <= 4) ):
        # sound = AudioSegment.from_file("f5.wav", format="wav")
        sound = 'f5.wav'
        sounds.append(sound)
        print("left_arm 4")
    if( (right_arm > 4) and (right_arm <= 5) ):
        # sound = AudioSegment.from_file("g5.wav", format="wav")
        sound = 'g5.wav'
        sounds.append(sound)
        print("left_arm 5")

    for i in range(len(sounds)):
        print(sounds[i])
        os.system(f"aplay {sounds[i]}&")
        
    # time.sleep(1.)
    
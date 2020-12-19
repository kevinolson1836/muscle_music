from tones import SINE_WAVE, SAWTOOTH_WAVE, TRIANGLE_WAVE, SQUARE_WAVE
from tones.mixer import Mixer
import random


# Create mixer, set sample rate and amplitude
mixer = Mixer(44100, 0.5)

# Create two monophonic tracks that will play simultaneously, and set
# initial values for note attack, decay and vibrato frequency (these can
# be changed again at any time, see documentation for tones.Mixer
mixer.create_track(0, SAWTOOTH_WAVE)
mixer.create_track(1, SQUARE_WAVE)
mixer.create_track(2, TRIANGLE_WAVE)
mixer.create_track(3, SINE_WAVE)

# Add a 1-second tone on track 0, slide pitch from c# to f#)
# mixer.add_silence(1,duration=1.5)
# mixer.add_silence(2,duration=5.5)
# mixer.add_silence(3,duration=8.5)

mixer.add_note(0, note='c', octave=5, duration=1)
mixer.add_note(0, note='d', octave=5, duration=1)
mixer.add_note(0, note='e', octave=5, duration=1)
mixer.add_note(0, note='f', octave=5, duration=1)
mixer.add_note(0, note='g', octave=5, duration=1)
mixer.add_note(0, note='a', octave=5, duration=1)
mixer.add_note(0, note='B', octave=5, duration=1)

mixer.add_note(1, note='c', octave=3, duration=1)
mixer.add_note(1, note='d', octave=3, duration=1)
mixer.add_note(1, note='e', octave=3, duration=1)
mixer.add_note(1, note='f', octave=3, duration=1)
mixer.add_note(1, note='g', octave=3, duration=1)
mixer.add_note(1, note='a', octave=3, duration=1)
mixer.add_note(1, note='b', octave=3, duration=1)

mixer.add_note(2, note='c', octave=7, duration=1)
mixer.add_note(2, note='d', octave=7, duration=1)
mixer.add_note(2, note='e', octave=7, duration=1)
mixer.add_note(2, note='f', octave=7, duration=1)
mixer.add_note(2, note='g', octave=7, duration=1)
mixer.add_note(2, note='a', octave=7, duration=1)
mixer.add_note(2, note='b', octave=7, duration=1)

mixer.add_silence(2,duration=1)

notes = [
    ['c'],
    ['d'],
    ['e'],
    ['f'],
    ['g'],
    ['a'],
    ['b'],
    ]

for _ in range (100):
    rand = random.randint(0,6)
    rand1 = random.randint(0,6)
    rand2 = random.randint(0,6)
    # print(notes[rand])
    mixer.add_note(2, note=notes[rand][0], octave=4, duration=1)
    mixer.add_note(0, note=notes[rand1][0], octave=5, duration=1)
    mixer.add_note(1, note=notes[rand2][0], octave=6, duration=1)

mixer.write_wav('tones.wav')
# Mix all tracks into a single list of samples and write to .wav file

# Mix all tracks into a single list of samples scaled from 0.0 to 1.0, and
# return the sample list
samples = mixer.mix()




#while true:
    # read data from sensor
    # if data > not moving value
        #   mixer.add_note( __trackname__,      track name
        #   note='a#'                           some note
        #   , octave=5,                         octive ?
        #   duration=__tim)                     time from last moved

        #  after song has been added play the note in non blocking
    # else:
        # start a timer and use that value for duration
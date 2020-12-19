from tones import SINE_WAVE, SAWTOOTH_WAVE, TRIANGLE_WAVE, SQUARE_WAVE
from tones.mixer import Mixer
import random


# Create mixer, set sample rate and amplitude
mixer = Mixer(44100, 0.6)

# Create two monophonic tracks that will play simultaneously, and set
# initial values for note attack, decay and vibrato frequency (these can
# be changed again at any time, see documentation for tones.Mixer
# mixer.create_track(0, SAWTOOTH_WAVE)
# mixer.create_track(1, SQUARE_WAVE)
# mixer.create_track(2, TRIANGLE_WAVE)
mixer.create_track(0, SINE_WAVE)

# Add a 1-second tone on track 0, slide pitch from c# to f#)
# mixer.add_silence(1,duration=1.5)
# mixer.add_silence(2,duration=5.5)
# mixer.add_silence(3,duration=8.5)

mixer.add_note(0, note='d', octave=5, duration=1)
mixer.write_wav('d5.wav')
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
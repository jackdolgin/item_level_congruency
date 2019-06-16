from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy.random import random, randint, normal, shuffle
import random
import os  # handy system and path functions
import sys  # to get file system encoding
import math


# Create a voice-key to be used:
vpvk = vk.OnsetVoiceKey(
    sec=2, #time alloted to verbally respond once this variable starts
    file_out='data/trial_'+str(trials.thisN).zfill(3)+'_'+word+'.wav') #saves recording from each trial in the form `trial_000_pug.wav`

# Start it recording (and detecting):
vpvk.start()  # non-blocking; don't block when using Builder


# The recorded sound is saved upon .stop() by default. But
# its a good idea to call .stop() explicitly, eg, if there's much slippage:

vpvk.stop()

# Add the detected time into the PsychoPy data file:
thisExp.addData('vocal_RT', round(vpvk.event_onset, 3))
thisExp.addData('bad_baseline', vpvk.bad_baseline)
thisExp.addData('filename', vpvk.filename)
thisExp.nextEntry()

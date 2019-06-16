from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy.random import random, randint, normal, shuffle
import random
import os  # handy system and path functions
import sys  # to get file system encoding
import math
import psychopy.voicekey as vk
vk.pyo_init()


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

expInfo = {'SubjectNO':'00', 'SubjectInitials':'TEST'}
dlg = gui.DlgFromDict(dictionary=expInfo, title="Stroop Example", order=['SubjectNO', 'SubjectInitials'])
if dlg.OK == False: core.quit()  # user pressed cancel

filename = _thisDir + os.sep + u'data/%s/%s' % (expInfo['SubjectNO'], expInfo['SubjectNO'])    #creates data file name
# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(extraInfo = expInfo, dataFileName = filename)

# Setup the Window
win = visual.Window(
    size = (1024, 768), color = [.15, .15, .15], fullscr = False,
    allowGUI = False, monitor = 'testMonitor', useFBO = True)
# store frame rate of monitor
f_rate = win.getActualFrameRate()
expInfo['frameRate'] = f_rate
framelength = win.monitorFramePeriod

def runTrial(params1):
    # Create a voice-key to be used:
    vpvk = vk.OnsetVoiceKey(
        # sec=2, #time alloted to verbally respond once this variable starts
        ) #saves recording from each trial in the form `trial_000_pug.wav`
    vpvk = vk.OffsetVoiceKey(file_out='data/trial_'+str(params1) +'.wav')
    inst6 = visual.TextStim(
        win = win, text = "Say aloud the number... " + str(params1),
        units = 'deg', height = 1, wrapWidth = 20)
    inst6.setAutoDraw(True)
    # Start it recording (and detecting):
    vpvk.start()  # non-blocking; don't block when using Builder
    frameN = -1 # number of completed frames (so 0 is the first frame)
    while frameN < int(round(2.0/framelength)):
        frameN += 1
        win.flip()
    # The recorded sound is saved upon .stop() by default. But
    # its a good idea to call .stop() explicitly, eg, if there's much slippage:
    vpvk.stop()
    inst6.setAutoDraw(False)

    # Add the detected time into the PsychoPy data file:
    thisExp.addData('vocal_RT', round(vpvk.event_onset, 3))
    thisExp.addData('vocal_RT_offset', round(vpvk.event_offset, 3))
    thisExp.addData('bad_baseline', vpvk.bad_baseline)
    thisExp.addData('filename', vpvk.filename)
    thisExp.nextEntry()

for trial in range(4):
    runTrial(trial)

thisExp.saveAsWideText(filename+'.csv')
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()

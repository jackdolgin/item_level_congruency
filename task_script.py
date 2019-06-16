#Using Python 2.7 and PsychoPy2
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

timeout = int(round(4.0/framelength))

def runTrial(params1):
    # Create a voice-key to be used:
    vpvk = vk.OnsetVoiceKey()
    vpvk = vk.OffsetVoiceKey(file_out='data/trial_'+str(params1) +'.wav', delay = 0) # it appears adding in the "delay = 0" parameter is leading to somewhat of an error about "ReferenceError: weakly-referenced object no longer exists"; only occurs beginning on the second trial; but the voice is still recorded and data looks ok so maybe it's nothing to worry about? in any event i still don't understand what this 'delay' variable (or the 'sec' variable) means
    instrs = visual.TextStim(
        win = win, text = "Say aloud the number... " + str(params1),
        units = 'deg', height = 1, wrapWidth = 20)
    print ("early")
    instrs.setAutoDraw(True)
    # Start it recording (and detecting):
    vpvk.start()
    frameN = -1 # number of completed frames (so 0 is the first frame)
    while frameN < timeout:
        frameN += 1
        win.flip()
        if hasattr(vpvk, 'event_offset') and vpvk.event_offset > 0:
            print (vpvk.event_offset)
            break
    instrs.setAutoDraw(False)

    # Add the detected time into the PsychoPy data file:
    thisExp.addData('vocal_RT', round(vpvk.event_onset, 3))
    if frameN < timeout:
        thisExp.addData('vocal_RT_offset', round(vpvk.event_offset, 3))
    else:
        thisExp.addData('vocal_RT_offset', 0)
    thisExp.addData('bad_baseline', vpvk.bad_baseline)
    thisExp.addData('filename', vpvk.filename)
    thisExp.nextEntry()
    print "end trial"

for trial in range(4):
    runTrial(trial)

thisExp.saveAsWideText(filename+'.csv')
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()

import json
import time
from telnetlib import Telnet
import serial

# ser = serial.Serial('COM9', 9600, timeout=1)

from lazyme.string import color_print

tn = Telnet('localhost', 13854)
start = time.clock()

i = 0
tn.write('{"enableRawOutput": true, "format": "Json"}')

eSenseDict = {'attention': 0, 'meditation': 0}
waveDict = {'lowGamma': 0, 'highGamma': 0, 'highAlpha': 0, 'delta': 0, 'highBeta': 0, 'lowAlpha': 0, 'lowBeta': 0,
            'theta': 0}
signalLevel = 0

color_print('Simulation for 100 sec.', color='blue',bold=True)
flag = False
blink_flag = False
blink_count = 0
speedFlag = 0
while True:

    blinkStrength = 0

    line = tn.read_until('\r')

    if len(line) > 20:
        timeDifference = time.clock() - start
        i = timeDifference
        dict1 = json.loads(str(line))
        if "poorSignalLevel" in dict1:
            signalLevel = dict1['poorSignalLevel']
        if "blinkStrength" in dict1:
            blinkStrength = dict1['blinkStrength']
        if "eegPower" in dict1:
            waveDict = dict1['eegPower']
            eSenseDict = dict1['eSense']
        attentionStr = str(eSenseDict['attention'])
        meditationStr = str(eSenseDict['meditation'])
        blinkStrengthStr = str(blinkStrength)
        print "Attention: " + attentionStr,
        print "Meditation: " + meditationStr,
        print "Blink Strength: " + blinkStrengthStr

        meditationInt = int(meditationStr)
        attentionInt = int(attentionStr)
        blinkStrengthInt = int(blinkStrengthStr)
        if blinkStrengthInt > 80 and not flag:
            flag = True
            speedFlag = 1 if meditationInt <= 70 else 2
            color_print('Start', color='green', bold=True)
            # ser.write('f')
        elif blinkStrengthInt > 120 and flag:
            color_print('Stop', color='red', bold=True)
            color_print('Force blink if you want to continue.', color='yellow')
            flag = False
            # ser.write('s')

        if blinkStrengthInt == 0 and blink_count == 2 and flag:
            color_print('Left', color='blue')
            # ser.write('l')
        elif blinkStrengthInt == 0 and blink_count == 3 and flag:
            color_print('Right', color='blue')
            # ser.write('r')

        if blinkStrengthInt > 0:
            blink_count = blink_count + 1
        elif blinkStrengthInt == 0:
            blink_count = 0

        # if meditationInt <= 60 and speedFlag == 2 and flag:
        #     speedFlag = 1
        #     color_print('Speed: Slow', color='yellow')
        # elif meditationInt > 60 and speedFlag == 1 and flag:
        #     speedFlag = 2
        #     color_print('Speed: Fast', color='red')
# ser.close()
tn.close()

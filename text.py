#3.9*963 ##!/usr/bin/env python
import numpy as np
import sys
import cv2
from playsound import playsound
from gtts import gTTS

print ("Enter the Text :")
##str=raw_input()
str=input()

print (str)
#while True:
    
#mtext = 'welcome to india welcome to india welcome to india '
lag = 'en'
myobj = gTTS(text=str, lang=lag)
##, slow =False)
myobj.save("test.mp3")
playsound("test.mp3")
##os.system("mpg321 test.mp3")

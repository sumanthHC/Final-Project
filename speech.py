#Python 2.x program for Speech Recognition 

import speech_recognition as sr 
import os

##import RPi.GPIO as GPIO


#enter the name of usb microphone that you found 
#using lsusb 
#the following name is only used as an example 
mic_name = "USB Device 0x46d:0x825: Audio (hw:1, 0)"
#Sample rate is how often values are recorded 
sample_rate = 48000
#Chunk is like a buffer. It stores 2048 samples (bytes of data) 
#here. 
#it is advisable to use powers of 2 such as 1024 or 2048 
chunk_size = 1024 #2048
#Initialize the recognizer 
r = sr.Recognizer() 

#generate a list of all audio cards/microphones 
mic_list = sr.Microphone.list_microphone_names() 

#the following loop aims to set the device ID of the mic that 
#we specifically want to use to avoid ambiguity. 
for i, microphone_name in enumerate(mic_list): 
	if microphone_name == mic_name: 
		device_id = i 
device_id = 1

##GPIO.setmode(GPIO.BCM)
##
##GPIO.setup(2, GPIO.OUT)
##GPIO.output(2, GPIO.LOW)
##
##GPIO.setup(3, GPIO.OUT)
##GPIO.output(3, GPIO.LOW)
##
##GPIO.setup(4, GPIO.OUT)
##GPIO.output(4, GPIO.LOW)
##
##GPIO.setup(17, GPIO.OUT)
##GPIO.output(17, GPIO.LOW)

#use the microphone as source for input. Here, we also specify 
#which device ID to specifically look for incase the microphone 
#is not working, an error will pop up saying "device_id undefined"
count=0
while True:
 with sr.Microphone(device_index = device_id, sample_rate = sample_rate,chunk_size = chunk_size) as source: 
	#wait for a second to let the recognizer adjust the 
	#energy threshold based on the surrounding noise level 
        r.adjust_for_ambient_noise(source) 
        print ("Say Something")
        #listens for the user's input 
        audio = r.listen(source) 
                
        try: 
                text = r.recognize_google(audio) 
                print ("you said: " + text )
                if text == 'light on':
##                        GPIO.output(2, GPIO.HIGH)
                        print('lights on')
                if text == 'light off'or text == 'light of':
##                        GPIO.output(2, GPIO.LOW)
                        print('lights off ')
                if text == 'fan on' or text == 'fan onn':
##                        GPIO.output(3, GPIO.HIGH)
                        print('Fan on')
                if text == 'fan off' or text == 'fan of':
##                        GPIO.output(3, GPIO.LOW)
                        print('Fan Off')

                if text == 'tv on' :
##                        GPIO.output(3, GPIO.HIGH)
                        print('TV on')
                if text == 'tv off':
##                        GPIO.output(3, GPIO.LOW)
                        print('TV Off')

                if text == 'led on':
##                        GPIO.output(3, GPIO.HIGH)
                        print('LED on')
                if text == 'led off':
##                        GPIO.output(3, GPIO.LOW)
                        print('LED Off')
                        
                if text == 'stop':
                        print('Stop')
                        
                        count =1
                        break
                
        #error occurs when google could not understand what was said 

        except sr.UnknownValueError: 
                print("Google Speech Recognition could not understand audio") 

        except sr.RequestError as e: 
                print("Could not request results from Googlespeech Recognition service; {0}".format(e))
        if count==1:
                print('hfjhjh')
                
                
                break
 if count==1:
         print('gggg')
         count=0
         break

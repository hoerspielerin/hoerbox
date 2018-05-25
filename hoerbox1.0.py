#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  by hoerspielerIN.py
#   
#  
def main():
	
	return 0



import RPi.GPIO as GPIO
import time
import vlc
import os.path

path = '/home/pi/hoerspielsommer/soundfiles/'
path_utility = '/home/pi/hoerspielsommer/utility/'
debounceTIME = 200
newInput = ''
oldInput = ''
list_to_play = ''
global execute
global audioFileType
audioFileType = '.ogg'
execute = False

GPIO.cleanup()

### Connection List
channel1 = 5
channel2 = 6
channel3 = 13
channel4 = 19
channel5 = 20
channel6 = 21
channel7 = 17
channel8 = 18
channel9 = 27
channel10 = 22


def initialising():
	
	GPIO.setmode(GPIO.BCM)

	GPIO.setup(channel1, GPIO.IN, pull_up_down = GPIO.PUD_UP)
	GPIO.setup(channel2, GPIO.IN, pull_up_down = GPIO.PUD_UP)
	GPIO.setup(channel3, GPIO.IN, pull_up_down = GPIO.PUD_UP)
	GPIO.setup(channel4, GPIO.IN, pull_up_down = GPIO.PUD_UP)
	GPIO.setup(channel5, GPIO.IN, pull_up_down = GPIO.PUD_UP)
	GPIO.setup(channel6, GPIO.IN, pull_up_down = GPIO.PUD_UP)
	GPIO.setup(channel7, GPIO.IN, pull_up_down = GPIO.PUD_UP)
	GPIO.setup(channel8, GPIO.IN, pull_up_down = GPIO.PUD_UP)
	GPIO.setup(channel9, GPIO.IN, pull_up_down = GPIO.PUD_UP)
	GPIO.setup(channel10, GPIO.IN, pull_up_down = GPIO.PUD_UP)
	
	GPIO.add_event_detect(channel1, GPIO.FALLING, callback = my_callback1, bouncetime =debounceTIME)
	GPIO.add_event_detect(channel2, GPIO.FALLING, callback = my_callback2, bouncetime =debounceTIME)
	GPIO.add_event_detect(channel3, GPIO.FALLING, callback = my_callback3, bouncetime =debounceTIME)
	GPIO.add_event_detect(channel4, GPIO.FALLING, callback = my_callback4, bouncetime =debounceTIME)
	GPIO.add_event_detect(channel5, GPIO.FALLING, callback = my_callback5, bouncetime =debounceTIME)
	GPIO.add_event_detect(channel6, GPIO.FALLING, callback = my_callback6, bouncetime =debounceTIME)
	GPIO.add_event_detect(channel7, GPIO.FALLING, callback = my_callback7, bouncetime =debounceTIME)
	GPIO.add_event_detect(channel8, GPIO.FALLING, callback = my_callback8, bouncetime =debounceTIME)
	GPIO.add_event_detect(channel9, GPIO.FALLING, callback = my_callback9, bouncetime =debounceTIME)
	GPIO.add_event_detect(channel10, GPIO.FALLING, callback = my_callback10, bouncetime =debounceTIME)
	
	
def my_callback1(self):
	#BUTTON_1
	global value
	global player
	global newInput
	global oldInput
	player.stop()
	value = '1'
	newInput = oldInput + value
	player = vlc.MediaPlayer(path_utility + 'button1' + audioFileType)
	player.play()
	print(newInput)
	oldInput = newInput
def my_callback2(self):
	#BUTTON_2
	global value
	global player
	global newInput
	global oldInput
	player.stop()
	value = '2'
	newInput = oldInput + value
	player = vlc.MediaPlayer(path_utility + 'button2' + audioFileType)
	player.play()
	print(newInput)
	oldInput = newInput
def my_callback3(self):
	#BUTTON_3
	global value
	global player
	global newInput
	global oldInput
	player.stop()
	value = '3'
	newInput = oldInput + value
	player = vlc.MediaPlayer(path_utility + 'button3' + audioFileType)
	player.play()
	print(newInput)
	oldInput = newInput
	input_buffer()
def my_callback4(self):
	#BUTTON_2
	global value
	global player
	global newInput
	global oldInput
	player.stop()
	value = '4'
	newInput = oldInput + value
	player = vlc.MediaPlayer(path_utility + 'button4' + audioFileType)
	player.play()
	print(newInput)
	oldInput = newInput
	input_buffer()
def my_callback5(self):
	#BUTTON_5
	global value
	global player
	global newInput
	global oldInput
	player.stop()
	value = '5'
	newInput = oldInput + value
	player = vlc.MediaPlayer(path_utility + 'button5' + audioFileType)
	player.play()
	print(newInput)
	oldInput = newInput
	input_buffer()
def my_callback6(self):
	#BUTTON_6
	global value
	global player
	global newInput
	global oldInput
	player.stop()
	value = '6'
	newInput = oldInput + value
	player = vlc.MediaPlayer(path_utility + 'button6' + audioFileType)
	player.play()
	print(newInput)
	oldInput = newInput
	input_buffer()
def my_callback7(self):
	#BUTTON_7
	global value
	global player
	global newInput
	global oldInput
	player.stop()
	value = '7'
	newInput = oldInput + value
	player = vlc.MediaPlayer(path_utility + 'button7' + audioFileType)
	player.play()
	print(newInput)
	oldInput = newInput
	input_buffer()
def my_callback8(self):
	#BUTTON_8
	global value
	global player
	global newInput
	global oldInput
	player.stop()
	value = '8'
	newInput = oldInput + value
	player = vlc.MediaPlayer(path_utility + 'button8' + audioFileType)
	player.play()
	print(newInput)
	oldInput = newInput
	input_buffer()
def my_callback9(self):
	#BUTTON_9
	global value
	global player
	global newInput
	global oldInput
	player.stop()
	value = '9'
	newInput = oldInput + value
	player = vlc.MediaPlayer(path_utility + 'button9' + audioFileType)
	player.play()
	print(newInput)
	oldInput = newInput
	input_buffer()
def my_callback10(self):
	#BUTTON_CALL
	global value
	global player
	global newInput
	global oldInput
	global execute
	player.stop()
	#player = vlc.MediaPlayer(path + '14.ogg')
	#player.play()
	print(newInput)
	execute = True

initialising()

   
player = vlc.MediaPlayer(path_utility + 'intro' + audioFileType) # INITIAL SOUND 
player.play()

while (1):
	time.sleep(1)
	
	
	if (execute == True):
		print "execute the playback"
		
		song = path + newInput + audioFileType
		
		print(song)		
		if (os.path.isfile(song) == True):
			print "execute is possible"
			oldInput =''
			player = vlc.MediaPlayer(path_utility + 'dial' + audioFileType)
			player.play()
			time.sleep(9)
			player = vlc.MediaPlayer(song)
			player.play()

		else :
			print "execute is not possible"
			oldInput =''
			player = vlc.MediaPlayer(path_utility + 'busy' + audioFileType)
			oldInput =''
			player.play()
			
		execute = False	
		
		
	else :
		
		time.sleep(0.01)










if __name__ == '__main__':
	main()


#!/usr/bin/env python2

import RPi.GPIO as GPIO
import time
import sys

def init():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(25, GPIO.OUT)

def sound(length, freq):
	i = 1.0/freq
	fut = time.time() + length
	while time.time() < fut:
		now = time.time()
		GPIO.output(25, GPIO.HIGH)
		GPIO.output(25, GPIO.LOW)
		time.sleep(i - 0.00018)

def play(music):
	for note in music:
		if note[0] != '/':
			c = note.index(",")
			freq = int(note[:c])
			time = float(note[c+1:])
			sound(time, freq)

if __name__ == "__main__":
	init()
	music = open(sys.argv[1]).read().split()
	play(music)

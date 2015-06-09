#!/usr/bin/env python


import subprocess
import datetime
import time

while True:
	tomorrow = datetime.datetime.replace(datetime.datetime.now() + datetime.timedelta(days=1), hour=0, minute=0, second=0)
	#Tomorrow Date , with time set as 00:00:00 

	now = datetime.datetime.now()	#Present Time

	counter = time.strftime("%d")  	#day of month

	left = tomorrow - now		#Time left until next day 00:00:00

	message = "Github Commit Streak.Day : %s \n Time Left for today %s :" % (counter, left)

	subprocess.Popen(['notify-send', message])	#notify-send is called to send a notification to desktop.

	time.sleep(5) #Sleep For 4 Hours.


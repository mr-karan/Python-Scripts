import subprocess
import datetime
import time

while True:
    tomorrow = datetime.datetime.replace(datetime.datetime.now() + datetime.timedelta(days=1), hour=0, minute=0, second=0)
    now = datetime.datetime.now()

    left = tomorrow - now

    message = "Github Commit Streak Day Time Left for today %s :" % (left)

    subprocess.Popen(['notify-send', message])

    time.sleep(14400)

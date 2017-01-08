import time
import os, sys
import datetime
from random import randint

class timer:
    def __init__(self):
        pass

    def looper(self):
        while (True):
            self.calculate()
            t = randint(3600,10000)
            print 'sleep for:',t
            time.sleep(t)

    def calculate(self):
        prev = datetime.datetime(2017, 1, 1, 0, 0, 0)
        next = datetime.datetime(2018, 1, 1, 0, 0, 0)
        now = datetime.datetime.now()
        nowStr = datetime.datetime.now().strftime("%d-%m-%Y")
        prevDiff = now - prev
        prevDiff = str(self.chop_microseconds(prevDiff))
        nextDiff = next - now
        nextDiff = str(self.chop_microseconds(nextDiff))
        noti = prevDiff+"\n"+nextDiff
        message = "reattach-to-user-namespace osascript -e 'display notification \""+noti+"\" with title \""+nowStr+"\" sound name \"Submarine\"'"
        os.system(message)

    def chop_microseconds(self, delta):
        return delta - datetime.timedelta(microseconds=delta.microseconds)


if __name__ == "__main__":
    t = timer()
    t.looper()

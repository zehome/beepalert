#!/usr/bin/env python

import sys
import datetime
import threading
import subprocess

class BeepThread(threading.Thread):
    def __init__(self):
        self.evt = threading.Event()
        self.value = False
        super(BeepThread, self).__init__()
        self.setDaemon(True)

    def setbeep(self, value):
        if value != self.value:
            self.value = value
            if value:
                self.evt.set()

    def run(self):
        while True:
            self.evt.wait(1)
            self.evt.clear()
            if self.value:
                subprocess.call("beep -f 2093", shell=True)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Usage: %s threshold" % (sys.argv[0],)
        sys.exit(0)

    try:
        threshold = float(sys.argv[1])
    except ValueError:
        print "Invalid threshold."
        sys.exit(1)

    beepthread = BeepThread()
    beepthread.start()
    while True:
        line = sys.stdin.readline()
        try:
            load1m = float(line.split()[0])
        except (ValueError, IndexError):
            print "Error parsing command line!"
            continue
        loadtest = load1m > threshold
        if loadtest:
            print "%s Load %s" % (datetime.datetime.now(), load1m,)
        beepthread.setbeep(loadtest)
    beepthread.join()

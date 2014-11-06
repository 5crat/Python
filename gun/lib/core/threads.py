#!/usr/bin/env python
# -*-coding:utf-8-*-
#-*-author:scrat-*-

import time
import threading
from thread import error as ThreadError

from lib.core.setting import MAX_THREADS
from lib.core.setting import PYVERSION


def _setDaemon(thread):
    if PYVERSION >= "2.6":
        thread.daemon = True
    else:
        thread.setDaemon(True)

def runThreads(numThreads, threadFunction):

    threads = []

    if numThreads > MAX_THREADS:
        numThreads = MAX_THREADS
    try:
        if numThreads > 1:
            pass
        else:
            threadFunction()
            return

        # start threads
        for numThread in xrange(numThreads):
            thread = threading.Thread(target=threadFunction, name=str(numThread))
            _setDaemon(thread)

            try:
                thread.start()
            except ThreadError:
                break

            threads.append(thread)

        # and wait all thread finish
        alive = True
        while alive:
            alive = False
            for thread in threads:
                if thread.isAlive():
                    alive = True
                    time.sleep(0.1)
    except:
        print "Thread Error!"
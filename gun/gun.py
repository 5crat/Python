#!/usr/bin/env python
#-*-coding:utf-8-*-
#-*-author:scrat-*-

import os
import sys
import time
import inspect
from lib.core.data import paths
from lib.core.common import banner


def modulePath():
    """
    This will get us the program's directory
    """

    try:
        _ = sys.executable
    except NameError:
        _ = inspect.getsourcefile(modulePath)

    return os.path.dirname(os.path.realpath(_))

def main():
    try:
        paths.ROOT_PATH = modulePath()
        banner()
        print '[*] starting at %s\n\n' % time.strftime("%X")
    except KeyboardInterrupt:
        print
        err_msg = 'User Aborted!'
    except EOFError:
        err_msg = 'Exit!'
    except SystemExit:
        pass
    finally:
        print '[*] shutdown at %s\n' % time.strftime("%X")
if __name__ == '__main__':
    main()

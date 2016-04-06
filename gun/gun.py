#!/usr/bin/env python
#-*-coding:utf-8-*-
#-*-author:scrat-*-

import os
import sys
import time
import inspect
from libs.core.data import paths
from libs.core.common import banner
from libs.core.common import setPaths
from libs.core.common import setConfAttribute
from libs.plugins.subDomainsBrute.subDomainsBrute import DNSBrute

from libs.core.dbhandle import DBhandle

def modulePath():
    """
    get the script's directory
    """
    _ = inspect.getsourcefile(modulePath)
    return os.path.dirname(os.path.realpath(_))

def main():
    try:
        paths.ROOT_PATH = modulePath()
        setPaths()
        setConfAttribute()
        banner()

        db = DBhandle()
        a = DNSBrute('taikang.com', output=db)
        a.run()
        db.close()
        print '\r\n[*] starting at %s\n' % time.strftime("%X")
    except KeyboardInterrupt:
        print 'User Aborted!'
    except EOFError:
        print 'Exit!'
    except SystemExit:
        pass
    finally:
        print '[*] shutdown at %s\n' % time.strftime("%X")
if __name__ == '__main__':
    main()
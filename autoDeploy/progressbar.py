import math
import sys
import time

def bar(cur, total):
    """progressbar from net"""
    percent = '{:.0%}'.format(cur * 1.0 / total)
    sys.stdout.write('\r')
    sys.stdout.write('[%-50s] %s' % ('#' * int(math.floor(cur * 50 / total)), percent))

# coding=utf-8
import re
import time
import random
import sys


if __name__ == "__main__":
    for i in range(1,101):
        sys.stdout.write('\r{}>{}%'.format('='*(i/10), i))
        time.sleep(0.1)
        sys.stdout.flush()
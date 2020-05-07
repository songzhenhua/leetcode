# coding=utf-8
import re
import time
import random
import sys


if __name__ == "__main__":
    pattern = re.compile(r'abc\w*')
    with open("aaa", 'r') as f:
        contents = f.readlines()
        for content in contents:
            content.strip('\n')
            result = pattern.findall(content)
            print result
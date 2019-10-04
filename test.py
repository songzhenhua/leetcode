# coding=utf-8
import re
import time



if __name__ == "__main__":
    a=[1,2,3,3,3]
    l = []
    index = 0
    max_num = max(a)
    while True:
        try:
            index = a.index(max_num)
            l.append(index)
            a[index] = None
        except ValueError:
            break
    a = [max_num if i == None else i for i in a]
    print a,l
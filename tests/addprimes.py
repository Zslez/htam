from json import load, dump
from math import log

__0 = (0).__ne__
__int = int
__set = set
__list = list
__open = open
__load = load
__dump = dump
__range = range
__tuple = tuple
__print = print
__filter = filter
__sorted = sorted
__log = log

from time import time

lo = 180000000
step = 10000000
times = 1

with __open('htam/primelist.json') as f: plist = __load(f)

s = 100000

for i in range(int(len(plist) // s) + 1):
    with __open(f'htam/primelists/pl{i}.json', 'w') as f:
        __dump(plist[i * s:(i + 1) * s], f, indent = 4)

'''
for l in __range(lo, lo + (step * times), step):
    with __open('pl.json') as f: plist = __load(f)
    def prime():
        for i in __range(l + 1, l + step, 2):
            r = __int(i ** 0.5) + 1
            for j in plist:
                if j > r: yield i; break
                if i % j == 0: break
    plist = __tuple(__set(plist) | __set(prime()))
    with __open('pl.json', 'w') as f: __dump(__sorted(plist), f, indent = 4)
    __print(l + step)
'''
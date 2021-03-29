from math import log
from time import time
from itertools import chain

__0 = (0).__ne__
__log = log
__int = int
__len = len
__list = list
__chain = chain
__range = range
__tuple = tuple
__filter = filter
__sorted = sorted

def old(x):
    lo = __log(x)
    l = __int(x * (lo + __log(lo)) - x // 1000)
    s = __int(l ** 0.5) + 1
    pl = [0 if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 else i for i in __range(3, l)]
    for p in __chain(__range(11, s, 6), __range(7, s, 6)):
        if pl[p - 3]:
            for i in __range(p * 2, l, p):
                pl[i - 3] = 0
    return __tuple(__filter(__0, pl))[x - 4]

def new(x):
    lo = __log(x)
    l = __int(x * (lo + __log(lo)) - x // 1000)
    s = __int(l ** 0.5) + 1
    pl = [0 if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 else i for i in __range(3, l)]
    for p in __range(11, s, 6):
        if pl[p - 3]:
            for i in __range(p * 2, l, p):
                pl[i - 3] = 0
    for p in __range(7, s, 6):
        if pl[p - 3]:
            for i in __range(p * 2, l, p):
                pl[i - 3] = 0
    return __tuple(__filter(__0, pl))[x - 4]

test = 10000000

start = time()
print(old(test))
end = time()
print(f'Tempo di esecuzione: {end - start}')


start = time()
print(new(test))
end = time()
print(f'Tempo di esecuzione: {end - start}')
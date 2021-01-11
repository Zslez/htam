from time import time
from math import log
from htam import prime

__int = int
__range = range
__tuple = tuple
__filter = filter

def prime2(x):
    if x > 5:
        lo = log(x)
        l = __int(x * (lo + log(lo)))
        pl = [2] + [0 if i % 2 == 0 else i for i in __range(3, l)]
        for p in __range(3, __int(l ** (1 / 2)) + 1, 2):
            for i in __range(p * 2, l, p):
                pl[i - 2] = 0
        return __tuple(__filter((0).__ne__, pl))[x - 1]
    else:
        if x < 1: return None
        elif x == 1: return 2
        elif x == 5: return 11
        else: return 2 * x - 1

# TEST 1
start = time()
print(prime(100000))
end = time()
print(end - start)


# TEST 2
start = time()
print(prime2(100000))
end = time()
print(end - start)
from time import time

def trunc(x): return x.__trunc__()

def sqrt(x):
    a, b = 0.5, 0
    while a != b:
        b, a = a, a / 2 * (3 - x * (a ** 2))
    return a * x

_sqrt = sqrt

# TEST 1
start = time()
for i in range(1000):
    r = _sqrt(5)
print(r)
end = time()
print(f'Tempo di esecuzione: {end - start}')

# TEST 2
start = time()
for i in range(1000):
    r = 5 ** 0.5
print(r)
end = time()
print(f'Tempo di esecuzione: {end - start}')
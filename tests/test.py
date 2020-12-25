####################
#                  #
#    SPEED TEST    #
#                  #
####################

from time import time
from htam import prime, primefac, div, fib

start = time()
prime(10000)
end = time()
print(end - start)

# 0.13251662254333496

start = time()
primefac(87234581)
end = time()
print(end - start)

# 0.05323958396911621

start = time()
div(872345)
end = time()
print(end - start)

# 0.06825923919677734

start = time()
len(str(fib(100000))) # 20899 digits in less than 0.2 sec
end = time()
print(end - start)

# 0.19488763809204102

#########################################################################

####################
#                  #
#    OEIS  TEST    #
#                  #
####################

from htam import OEIS

start = time()
a, b = OEIS(), OEIS()               # Random Sequences
end = time()
print(end - start)                  # 2.075106620788574

# once the instance is created all sequence's attributes are generated,
# so everything below will take a very small amount of time

start = time()
a.sequence()
b.sequence()
tuple(a.terms())                    # terms is a generator
tuple(b.terms())                    # terms is a generator
a.links()
b.links()
a.comments()
b.comments()
end = time()
print(end - start)                  # 0.026909589767456055
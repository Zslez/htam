# LICENSE

# Copyright (c) 2020 Cristiano Sansò

# Permission is hereby granted, free of charge,
# to any person obtaining a copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


# pylint: disable = no-member


# Variables
__pack = 'htam'
__abs = abs
__int = int
__len = len
__pow = pow
__str = str
__sum = sum
__list = list
__print = print
__range = range
__tuple = tuple
__filter = filter


# Imports
import classes
import math


# INFO function
def __print_info(name, ops = ''):
    o, a = f'(x{ops})', 34
    s = f'{__pack}.{name}{o}'
    c = (a - __len(s))
    b = c / 2
    
    if b != b // 1:
        b1, b2 = c // 2, c // 2 - 1
    else:
        b1 = b2 = (b - 1) // 1

    __print()    
    __print('=============== INFO ===============')
    __print('[]' + ' ' * (a - 2)            + '[]')
    __print('[]' + ' ' * b1 + s + ' ' * b2  + '[]')
    __print('[]' + ' ' * (a - 2)            + '[]')
    __print('====================================')



# Fractional part
def frac(x):
    '''\nthis function returns the fractional part of a number\nit returns "None" if the argument is not valid
\nex1.\n>>> frac(12.13)\n0.13
\nex2.\n>>> frac(-135.1010101)\n-0.1010101'''
    power = 10 ** (__len(__str(x)) - __len(__str(__int(x))) - 1)
    ix = __int(x)
    x *= power
    return (__int(x) - ix * power) / power



# GCD
def gcd(x, y, *args):
    '''\nthis function returns the greatest common divisor of two numbers
\nex1.\n>>> gcd(120, 88)\n8
\nex2.\n>>> gcd(33, 44)\n11
\nex3.\n>>> gcd(110, 230, 350, 470, 590)\n10'''
    if x < 0: x = -x
    if y < 0: y = -y
    args = (i if i > 0 else -i for i in args)
    while y > 0:
        x, y = y, x % y
    for i in args:
        while i > 0:
            x, i = i, x % i
    return x



# LCM
def lcm(x, y, *args):
    '''\nthis function returns the least common multiple of two numbers\
\nex1.\n>>> lcm(3, 6)\n6
\nex2.\n>>> lcm(4, 22)\n44
\nex3.\n>>> lcm(33, 44, 55, 66)\n660'''
    result = x * y // gcd(x, y)
    for i in args:
        result = result * i // gcd(result, i)
    return result



# Mod
def mod(x, y, z = None):
    '''\nz is an integer automatically set to 0\n
\nthis function returns the solution to the equation
\n      zk ≡ x (mod y)
\nthe result will be k = "solution" (mod y)
\nthis function will return "None" if the equation has no solution
\nif z is missing or set to None this fuction will return
\n        x (mod y)
\nex1.\n>>> mod(7, 4, 8)\nNone
\nex2.\n>>> mod(7, 4, 5)\n3
\nex3.\n>>> mod(25, 10)\n5'''
    while True:
        if not z:
            return x % y
        g = gcd(z, y)
        if g == 1:
            inverse = 0
            x, z = x % y, z % y
            for i in __range(1, y):
                if z * i % y == 1:
                    inverse = i
                    break
            return __int(x * inverse % y)
        else:
            if not x // g == x / g:
                return None
            x /= g
            z /= g
            y /= g



# Divisors
def div(x, y = 1):
    '''\ny is an integer automatically set to 1
this function returns the number of divisors of x, if y is 1 or missing
\nit returns a tuple containing all divisors of x, if y is 2
\nex1.\n>>> div(488)\n8
\nex2.\n>>> div(488, 2)\n[1, 2, 4, 8, 61, 122, 244, 488]'''
    d = (1,) + __tuple(__filter(lambda n: x % n == 0, __range(2, x // 2 + 1))) + (x,)
    if y == 1:
        return __len(d)
    elif y == 2:
        return d



# Prime
def prime(x):
    '''\nthis function returns the x-th prime number (it returns 2 if x < 1)
\nex1.\n>>> prime(10)\n29
\nex2.\n>>> prime(8266)\n84857'''
    if x > 5:
        lo = math.log(x)
        l = __int(x * (lo + math.log(lo)))
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



# Relatively Prime checker
def rel(x, y = None):
    '''\ny is an integer automatically set to None
\nthis function returns "True" if x and y are relatively prime, it returns "False" if not
\nif y is set to None or missing this function will return "True" if x is prime and "False" otherwise
\nex1.\n>>> rel(91)\nFalse
\nex2.\n>>> rel(14, 27)\nTrue
\nex3.\n>>> rel(2, 120)\nFalse'''
    if not y:
        for i in __range(2, __int(x ** (1 / 2)) + 1):
            if x % i == 0:
                return False
            else:
                continue
        return True
    else:
        if gcd(x, y) == 1:
            return True
        else:
            return False



# Primes less than a given number
def pi(x, y = 2):
    '''\ny is an integer automatically set to 2 (y should always be greater or equal to 2)
this function returns the number of primes between y argument and x
\nex1.\n>>> pi(1356)\n217
\nex2.\n>>> pi(180623)\n16392'''
    return __sum((rel(i) for i in __range(y, x)))



# Factors
def primefac(x):
    '''\nthis function returns a list of abs(x)'s prime factors
    \nex1.\n>>> primefac(120)\n[2, 2, 2, 3, 5]
    \nex2.\n>>> primefac(13)\n[13]'''
    x, factors, primelist, num = __abs(x), [], [2], 3
    while primelist[-1] < __int(x ** (1 / 2)) + 1:
        for p in primelist:
            if num % p == 0:
                break
        else:
            primelist.append(num)
        num += 2
    while x != 1:
        y = x
        for i in primelist:
            if x % i == 0:
                factors.append(i)
                x /= i
        if x == y:
            factors.append(__int(x))
            return factors
    factors.sort()
    return factors



# Factorial
def fac(x):
    '''\nthis function returns argument factorial
\nex1.\n>>> fac(6)\n720
\nex2.\n>>> fac(12)\n479001600
\nex2.\n>>> fac(0)\n1'''
    prod = 1
    for i in __range(1, x + 1):
        prod *= i
    return prod



# Collatz
def col(x):
    '''\nthis function returns a list containing each step of the Collatz Conjecture check process
\nex1.\n>>> col(7)\n[7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
\nex2.\n>>> col(170)\n[170, 85, 256, 128, 64, 32, 16, 8, 4, 2, 1]'''
    collist = []
    while x > 1:
        collist.append(__int(x))
        if x % 2 == 0:
            x /= 2
        else:
            x = 3 * x + 1
    else:
        collist.append(__int(x))
    return collist



# Euler's Totient Function
def tot(x):
    '''\nthis function returns the number of integers between 1 and n that are relatively prime to n
\nex1.\n>>> tot(163)\n162
\nex2.\n>>> tot(2222)\n1000'''
    count = 0        
    for i in __range(1, x + 1):
        if gcd(x, i) == 1:
            count += 1
    return count



# Base Converter
def base(x, y, z):
    '''\nthis function returns x converted from base y to base z
\nif z is greater than 10 the result will have a space between each digit
at the same time, if y is greater than 10, the input x must be a string with spaces between each digit
it returns "None" if x can't exist in base y
\nex1.\n>>> base(123)\n1111011
\nex2.\n>>> base(34, 8, 13)\n2 2
\nex3.\n>>> base('8 12', 17, 4)\n2110'''
    count, xlist = [], []
    
    # Separating digits
    if y > 10:
        for i in __str(x):
            if i != ' ':
                count.append(i)
            else:
                if count != []:
                    xlist.append(''.join(count))
                    count = []
                else:
                    continue
        xlist.append(''.join(count))
    else:
        xlist = [i for i in __str(x)]

    a, base10, xlist = __len(xlist), __int(''.join(xlist)), [__int(i) for i in xlist]

    # Checking Digits
    for i in xlist:
        if i < y:
            continue
        else:
            return None

    # Conversion to base 10
    if y != 10:
        base10 = 0
        for i in __range(a):
            base10 += xlist[i] * y ** (a - i - 1)

    # Conversion to base z
    x, basez_list, remain = base10, [], 1
    while x != 0:
        remain = x % z
        basez_list.append(remain)
        x = x // z
    basez = [__str(basez_list[__len(basez_list) - i - 1]) for i in __range(__len(basez_list))]

    if z <= 10:
        return ''.join(basez)
    else:
        return ' '.join(basez)



# Primitive root mod n
def primitive(x, y = 1):
    '''\ny is an integer automatically set to 1
\nthis function returns the number of primitive roots mod x if y = 1
it returns the list of primitive roots mod x if y = 2\n
\nex1.\n>>> primitive(17)\n8
\nex2.\n>>> primitive(17, 2)\n[3, 5, 6, 7, 10, 11, 12, 14]'''
    coset = {i for i in __range(1, x) if gcd(i, x) == 1}
    result = [k for k in __range(1, x) if coset == {__pow(k, j, x) for j in __range(1, x)}]
    if y == 1:
        return __len(result)
    elif y == 2:
        return result



# Fibonacci
def fib(x):
    '''\nthis function returns the x-th fibonacci number, it returns "None" if the argument is not valid
\nex1.\n>>> fib(0)\n0
\nex2.\n>>> fib(20)\n6765'''
    a, b = 0, 1
    for _ in __range(x):
        a, b = b, a + b
    return a



# Classes
class Scholar(classes.Scholar): pass
class OEIS(classes.OEIS): pass



# Info
def info(x = None):
    '''\nrun htam.info() to see general informations about htam functions and classes'''

    funcdict = {
        'frac': frac,
        'mod': mod,
        'gcd': gcd,
        'lcm': lcm,
        'div': div,
        'prime': prime,
        'pi': pi,
        'primefac': primefac,
        'fac': fac,
        'col': col,
        'rel': rel,
        'tot': tot,
        'base': base,
        'primitive': primitive,
        'fib': fib,
    }

    classdict = {
        'OEIS': OEIS,
    }

    # All Functions that takes 2, 3 or more arguments respectively
    arg2 = ['div', 'gcd', 'lcm', 'pi', 'rel', 'primitive']
    arg3 = ['mod', 'base']
    args = ['gcd', 'lcm']

    if not x:
        __print(f'\n{__pack.upper()}\n'
            '\nver. 2.1.0\n'
            f'\nHere the {str(len(funcdict))} functions available in {__pack}\n')
        for i in funcdict.keys():
            __print('>>> ' + i)
        __print(f'\nHere the {str(len(classdict))} class available in {__pack}\n')
        for i in classdict.keys():
            __print('>>> ' + i)
        __print(f'\nrun {__pack}.info(<func_or_class_name>) to see more detailed informations for that function.')
    elif x in funcdict.keys():
        if x in arg2:
            __print_info(x, ',y')
        elif x in arg3:
            __print_info(x, ', y, z')
        elif x in args and x in arg2:
            __print_info(x, ', y, *args')
        elif x in args:
            __print_info(x, ', *args')
        else:
            __print_info(x)
        __print(funcdict[x].__doc__)
    elif x in classdict.keys():
        if x == 'OEIS':
            __print_info(x, ', seq = None')
        __print(classdict[x].__doc__)
    else:
        __print('No function or class named', x)
# LICENSE

#Copyright (c) 2020 Cristiano Sansò

#Permission is hereby granted, free of charge,
#to any person obtaining a copy of this software and associated documentation files (the "Software"),
#to deal in the Software without restriction, including without limitation the rights to
#use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
#and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
#INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
#CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


# variables
__pack = 'htam'



# INFO function
def __print_info(func, ops = ''):
    o = '(x' + ops + ')'
    a = 34
    b = (a - len(__pack + '.' +  func + o))/2
    b1 = 0
    b2 = 0
    

    if b != int(b):
        b1 = int((a - len(__pack + '.' + func + o))//2)
        b2 = int((a - len(__pack + '.' + func + o))/2) - 1
    else:
        b1 = b2 = int((a - len(__pack + '.' + func + o))/2) - 1
    
    print('\n' + '=============== INFO ===============')
    print('[]' + ' '*(a-2) + '[]')
    print('[]' + ' '*b1 + __pack + '.' + func + o + ' '*b2 + '[]')
    print('[]' + ' '*(a-2) + '[]')
    print('====================================')



# Floor
def floor(x):
    '''\nthis function returns the greatest integer less or equal to x\nit returns "None" if the argument is not valid
    \nex1.\n>>> floor(-3.015)\n-4
    \nex2.\n>>> floor(4.87)\n4
    \nex3.\n>>> floor(7)\n7'''

    try:
        return int(x // 1)
    except:
        return None



# Ceil
def ceil(x):
    '''\nthis function returns the least integer greater or equal to x\nit returns "None" if the argument is not valid
    \nex1.\n>>> ceil(-3.015)\n-3
    \nex2.\n>>> ceil(4.87)\n5
    \nex3.\n>>> ceil(7)\n7'''

    try:
        if int(x) == x:
            return int(x)
        else:
            return int(x // 1) + 1
    except:
        return None



# Fractional part
def frac(x):
    '''\nthis function returns the fractional part of a number as an integer\nit returns "None" if the argument is not valid
    \nex1.\n>>> frac(12.13)\n13
    \nex2.\n>>> frac(135.1010101)\n1010101'''

    try:
        power = 10 ** (len(str(x)) - len(str(int(x))) - 1)
        ix = int(x)
        x *= power
        return int(x) - ix * power
    except:
        return None



# Root
def root(x, y = 2):
    '''\ny is a number automatically set to 2\nthis function returns the yth root of x\nit returns "None" if 1 or more arguments are not valid
    \nex1.\n>>> root(4)\n2.0
    \nex2.\n>>> root(5, 3)\n1.7099759466766968
    \nex3.\n>>> root(4, 4) == root(2, 2)\nTrue'''

    try:
        return x**(1/y)
    except:
        return None



# GCD
def gcd(x, y, *args):
    '''\nthis function returns the greatest common divisor of two numbers\nit returns "None" if 1 or more arguments are not valid
    \nex1.\n>>> gcd(120, 88)\n8
    \nex2.\n>>> gcd(33, 44)\n11
    \nex3.\n>>> gcd(110, 230, 350, 470, 590)\n10'''

    try:
        while y > 0:
            x, y = y, x % y
        for i in args:
             while i > 0:
                x, i = i, x % i
        return x
    except:
        return None



# LCM
def lcm(x, y, *args):
    '''\nthis function returns the least common multiple of two numbers\nit returns "None" if 1 or more arguments are not valid
    \nex1.\n>>> lcm(3, 6)\n6
    \nex2.\n>>> lcm(4, 22)\n44
    \nex3.\n>>> lcm(33, 44, 55, 66)\n660'''

    try:
        result = int(x*y/gcd(x, y))
        for i in args:
            result = int(result*i/gcd(result, i))
        return result
    except:
        return None



# Mod
def mod(x, y, z = 0):
    '''\nz is an integer automatically set to 0\n
        \nthis function returns the solution to the equation
        \n      zk ≡ x (mod y)
        \nthe result will be k = "solution" (mod y)
        \nthis function will return "None" if the equation has no solution, or if 1 or more arguments are not valid
        \nif z is missing or set to 0 this fuction will return
        \n        x (mod y)
        \nex1.\n>>> mod(7, 4, 8)\nNone
        \nex2.\n>>> mod(7, 4, 5)\n3
        \nex3.\n>>> mod(25, 10)\n5'''
    
    try:
        while True:
            g = gcd(z, y)
            if g == 1:
                if z == 0:
                    return x % y
                else:
                    inverse = 0
                    z = z % y
                    x = x % y
                    for i in range(1, y):
                        if z*i % y == 1:
                            inverse = i
                            break
                        else:
                            continue
                    return int((x*inverse) % y)
            else:
                try:
                    assert int(x/g) == x/g
                    x /= g
                    z /= g
                    y /= g
                    continue
                except:
                    return None
    except:
        return None



# Divisors
def div(x, y = 1):
    '''\ny is an integer automatically set to 1\nthis function returns the number of divisors of x if y is 1 or missing
        \nit returns the list of divisors of x if y is 2\nit returns "None" if 1 or more arguments are not valid
        \nex1.\n>>> div(488)\n8
        \nex2.\n>>> div(488, 2)\n[1, 2, 4, 8, 61, 122, 244, 488]'''

    try:
        count = 0
        divlist = []

        for i in range(1, x + 1):
            if x % i == 0:
                count += 1
                divlist.append(i)
        
        if y == 1:
            return count
        elif y ==2:
            return divlist
        else:
            return None
    except:
        return None



# Prime
def prime(x):
    '''\nthis function returns the xth prime number\nit returns "None" if the argument is not valid
    \nex1.\n>>> prime(10)\n29
    \nex2.\n>>> prime(8266)\n84857'''

    try:
        primelist = [2]
        num = 3
        while len(primelist) < x:
            for p in primelist:
                if num % p == 0:
                    break
            else:
                primelist.append(num)
            num += 2
        return primelist[-1]
    except:
        return None



# Relatively Prime checker
def rel(x, y = 0):
    '''\ny is an integer automatically set to 0
    \nthis function returns "True" if x and y are relatively prime, it returns "False" if not, and it returns "None" if 1 or more arguments are not valid
    \nif y is set to 0 or missing this function will return "True" if x is prime and "False" otherwise
    \nex1.\n>>> rel(91)\nFalse
    \nex2.\n>>> rel(14, 27)\nTrue
    \nex3.\n>>> rel(2, 120)\nFalse'''
    try:
        if x == 0 or x == 1:
            return False

        if y == 0:
            for i in range(2, int(x**(1/2)) + 1):
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
    except:
        return None



# Primes less than a given number
def pi(x, y = 1):
    '''\ny is an integer automatically set to 1\nthis function returns the number of primes between y argument and x\nit returns "None" if 1 or more arguments are not valid
    \nex1.\n>>> pi(1356)\n217
    \nex2.\n>>> pi(180623)\n16392'''

    try:
        count = 0
        for i in range(y, x):
            if rel(i) == True:
                count += 1
        return count
    except:
        return None



# Factors
def primefac(x):
    '''\nthis function returns a list of x's prime factors\nit returns "None" if the argument is not valid
    \nex1.\n>>> primefac(120)\n[2, 2, 2, 3, 5]
    \nex2.\n>>> primefac(13)\n[13]'''
    try:
        factors = []

        primelist = [2]
        num = 3
        while len(primelist) < x:
            for p in primelist:
                if num % p == 0:
                    break
            else:
                primelist.append(num)
            num += 2

        while x != 1:
            for i in primelist:
                if x % i == 0:
                    factors.append(i)
                    x /= i

        factors.sort()
        return factors
    except:
        return None



# Factorial
def fac(x):
    '''\nthis function returns argument factorial
    \nex1.\n>>> fac(6)\n720
    \nex2.\n>>> fac(12)\n479001600
    \nex2.\n>>> fac(0)\n1'''
    prod = 1

    for i in range(1, x + 1):
        prod *= i
    
    return prod



# Collatz
def col(x):
    '''\nthis function returns a list containing each step of the Collatz Conjecture check process\nit returns "None" if the argument is not valid
    \nex1.\n>>> col(7)\n[7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    \nex2.\n>>> col(170)\n[170, 85, 256, 128, 64, 32, 16, 8, 4, 2, 1]'''

    try:
        collist = []
        while x > 1:
            collist.append(int(x))
            if x % 2 == 0:
                x /= 2
            else:
                x = (3*x + 1)
        else:
            collist.append(int(x))
        return collist
    except:
        return None



# Euler's Totient Function
def tot(x):
    '''\nthis function returns the number of integers between 1 and n that are relatively prime to n\nit returns "None" if the argument is not valid
    \nex1.\n>>> tot(163)\n162
    \nex2.\n>>> tot(2222)\n1000'''

    try:
        count = 0        
        for i in range(1, x + 1):
            if gcd(x, i) == 1:
                count += 1
        return count
    except:
        return None



# Base Converter
def base(x, y = 10, z = 2):
    '''\ny is an integer automatically set to 10\nz is an integer automatically set to 2
    \nthis function returns x converted from base y to base z
    \nif z is greater than 10 the result will have a space between each digit\nat the same time, if y is greater than 10, the input x must be a string with spaces between each digit\nit returns "None" if 1 or more arguments are not valid, or if x can't exist in base y
    \nex1.\n>>> base(123)\n1111011
    \nex2.\n>>> base(34, 8, 13)\n2 2
    \nex3.\n>>> base('8 12', 17, 4)\n2110'''


    count = []
    xlist = []

    # Separating digits
    if y > 10:
        for i in str(x):
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
        for i in str(x):
            xlist.append(i)

    
    a = len(xlist)
    base10 = int(''.join(xlist))
    xlist = [int(i) for i in xlist]

    # Checking Digits
    for i in xlist:
        if i < y:
            continue
        else:
            return None

    # Conversion to base 10
    if y != 10:
        base10 = 0
        for i in range(a):
            base10 += xlist[i] * y ** (a - i - 1)

    # Conversion to base z
    x = base10
    basez_list = []
    remain = 1
    while x != 0:
        remain = x % z
        basez_list.append(remain)
        x = x // z
    basez = [str(basez_list[len(basez_list) - i - 1]) for i in range(len(basez_list))]

    if z < 10:
        return ''.join(basez)
    else:
        return ' '.join(basez)



# Primitive root mod n
def primitive(x, y = 1):
    '''\ny is an integer automatically set to 1
    \nthis function returns the number of primitive roots mod x if y = 1\nit returns the list of primitive roots mod x if y = 2\n
    \nex1.\n>>> primitive(17)\n8
    \nex2.\n>>> primitive(17, 2)\n[3, 5, 6, 7, 10, 11, 12, 14]'''
    try:
        coset = {i for i in range(1, x) if gcd(i, x) == 1}
        result = [k for k in range(1, x) if coset == {pow(k, j, x) for j in range(1, x)}]
        if y == 1:
            return len(result)
        elif y == 2:
            return result
    except:
        return None



# Info
def info(x = 0):
    '''\nrun htam.info() to see general informations about htam functions'''

    # Dictionary of all functions
    funcdict = {
        'floor': floor,
        'ceil': ceil,
        'frac': frac,
        'root': root,
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
        'base': base
    }

    # All Functions that takes 2 or 3 arguments respectively
    arg2 = ['root', 'div', 'gcd', 'lcm', 'pi', 'rel']
    arg3 = ['mod', 'base']
    args = ['gcd', 'lcm']

    if x == 0:
        print(
            '\n' + __pack.upper() + '\n'
            '\nver. 1.3.1\n '
            '\nHere\'s a list of functions ' + __pack + ' can perform. \n'
            )
        for i in funcdict.keys():
            print('>    ' + i)
        print(
            '\nrun ' + __pack + '.info(*function_name*) to see more detailed informations for that function.'
            )
    elif x in funcdict.keys():
        if x in arg2:
            __print_info(x, ',y')
        elif x in arg3:
            __print_info(x, ', y, z')
        elif x in args and x in arg2:
            __print_info(x, ', y, *args')
        elif x in args and x not in arg2:
            __print_info(x, ', *args')
        else:
            __print_info(x)
        print(funcdict[x].__doc__)
    else:
        print('No function named', x)
Htam is my very first coding project, it is a math Python library and it includes a lot of useful math functions.

I created it because I like maths and to test my Python skills.

- run htam.info() to see general informations about htam and all functions included
- run htam.info(function_name) to see detailed informations about that function

If you run into any issue, please send me an email and i will update the package as soon as I can.

I'm still working to improve this package, so, if you have any idea for a future update or a re-styling of an already existing function, please let me know with an email, I would really appreciate it.

Enjoy :)



Change Log
==========

1.3.1 (3/10/2020)
------------------
Minor Corrections

1.3.0 (3/10/2020)
------------------
New math function:
    1) "htam.primitive" >>>   primitive root

Various Improvements:
    - now "htam.gcd" and "htam.lcm" takes how many arguments you want

Other Minor Corrections


1.2.2 (28/09/2020)
------------------
Minor Corrections


1.2.0 (27/09/2020)
------------------
New math function:
    1)  "htam.base" >>>   base converter

Other Changes:
    - function info now includes some examples for each function

Various Improvements:
    - "htam.gcd" is now used into "htam.lcm", reducing code length
    - "htam.frac" now uses a faster method to the number of fractional digits, reducing code length
    - fixed a bug in the code of "htam.rel" and "htam.pi" that made these functions return a wrong result

Other Minor Corrections


1.1.0 (25/09/2020)
------------------
Two new math functions:
    1)  "htam.rel"  >>>   coprime checker
    2)  "htam.tot"  >>>   Euler's Totient function

Other Changes:
    - function info restyled

Various improvements:
    - "htam.pi" function speed of execution increased
    - "htam.floor" function is now literally a 1-line code, maybe i'll remove it in the future
    - now some functions reuses other functions to improve overall performances, in particular:
        - "htam.gcd" is now used into "htam.rel" and into "htam.mod"
        - the new "htam.rel" function replaced some lines of code into "htam.pi"
        - the new "htam.rel" is also used into "htam.tot"
    

1.0.4 (24/09/2020)
------------------
Minor Corrections


1.0.1 (24/09/2020)
------------------
Now each function returns "None" when 1 or more arguments are not valid


1.0.0 (23/09/2020)
------------------
First Release >>> 13 math functions included:
    1)  "htam.floor"        >>>   floor
    2)  "htam.ceil"         >>>   ceiling
    3)  "htam.frac"         >>>   fractional part
    4)  "htam.root"         >>>   nth root of a number
    5)  "htam.mod"          >>>   linear congruence solver
    6)  "htam.gcd"          >>>   greatest common divisor
    7)  "htam.lcm"          >>>   least common multiple
    8)  "htam.div"          >>>   divisors of a number
    9)  "htam.prime"        >>>   nth prime number
    10) "htam.pi"           >>>   number of primes less than a given number (pi function)
    11) "htam.primefac"     >>>   prime factorization of a number
    12) "htam.fac"          >>>   factorial of a number
    13) "htam.col"          >>>   collatz conjecture checker
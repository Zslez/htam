![PyPI - Downloads](https://img.shields.io/pypi/dd/htam)
![PyPI - License](https://img.shields.io/pypi/l/htam)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/htam)

# HTAM

Htam is my very first coding project, it is a math Python library and it includes a lot of useful math functions.

If you run into any issue, please send me an email and i will update the package as soon as I can.

I'm still working, and always looking for improvents and changes for this package, so, if you have any idea for a future update or a re-styling of an already existing function, please let me know with an email, I would really appreciate it.

If you liked my library, please consider leaving a star to my [github repo](https://github.com/Zslez/htam), it costs just 1 minute but I'd really appreciate it.

Enjoy :)


# Installation
<br>

[Windows](#Windows) <br>
[Linux/MacOS](#Linux/MacOS) <br>

<br>

---

<br>

## Windows
Press the `win` key, type `cmd` and press Enter to open the Command Prompt, now type the command

```bash
> pip install htam
```

> If pip does not work, you can try pip3

press Enter and wait until the installation is finished.

Now to assert you have `htam` installed, type
```bash
> py
```

> If py does not work, you can try python or python3

and then
```
>>> import htam
```
If it does not return any error, you installed it correctly.

<br>

---

<br>

## Linux/MacOS
Open the Terminal, now type the command

```bash
$ pip install htam
```

> If pip does not work, you can try pip3

press Enter and wait until the installation is finished.

Now to assert you have `htam` installed, type
```bash
$ python3
```
and then
```
>>> import htam
```
If it does not return any error, you installed it correctly.

<br>





# Start Using HTAM

> - execute htam.info() to see general informations about htam and all functions included
> - execute htam.info("<function_or_class_name>") to see detailed informations about that function/class and some examples
> - go on 

<br>



# Email
cristiano.sanso.04@gmail.com

<br>

# Change Log

## 2.0.9 (25/12/2020)

Minor Corrections

<br>

---

<br>

## 2.0.7 (25/12/2020)

Now OEIS generates all sequence's attribute when the instance is created, so getting any attribute later will take almost no time

<br>

---

<br>

## 2.0.0 (24/12/2020)

BIG UPDATE:

> new class OEIS: <br>
> - search for a sequence on https://oeis.org/ and return any attribute like description, links, comments, etc. <br>
> - if no argument is given for the constructor, OEIS will return a random sequence from https://oeis.org/
> - WARNING: using this class for the first time may install some required missing python modules

Various Improvements:

> - "htam.div" speed of execution increased <br>
> - "htam.prime" speed of execution extremely increased<br>
e.g. htam.prime(100000) took more than 6 mins before, while just 4.7 seconds now <br>
> - "htam.primefac" speed of execution extremely increased<br>
e.g. htam.primefac(1299709) took more than 6 mins before, while just 0.0016 seconds now (greve) <br>
> - some random code reduction

Other Changes:
> - Functions no more returns 'None' when arguments are not valid because it's unnecessary
> - Deleted "htam.root" because it's unnecessary since it's just 1 simple line of code
> - Deleted "htam.floor" and "htam.ceil" because they are already in the python official math library

Other Minor Corrections

<br>

---

<br>

## 1.4.1 (22/10/2020)

Minor Corrections

<br>

---

<br>

## 1.4.0 (14/10/2020)

New math function:

> - "htam.fib" >>> n-th Fibonacci number

Various Improvements:

> - "htam.primefac" speed of execution increased
> - fixed a bug in  "htam.rel" that made this function return a wrong result for 0, 1 and -1
> - some random code reduction
> - removed some unnecessary variables

Other Minor Corrections

<br>

---

<br>

## 1.3.9 (4/10/2020)

Minor Corrections

<br>

---

<br>

## 1.3.0 (3/10/2020)

New math function:

> - "htam.primitive" >>>   primitive root

Various Improvements:

> - now "htam.gcd" and "htam.lcm" takes how many arguments you want

Other Minor Corrections

<br>

---

<br>

## 1.2.2 (28/09/2020)

Minor Corrections

<br>

---

<br>

## 1.2.0 (27/09/2020)

New math function:

> - "htam.base" >>>   base converter

Other Changes:

> - function info now includes some examples for each function

Various Improvements:

> - "htam.gcd" is now used into "htam.lcm", reducing code length
> - "htam.frac" now uses a faster method to the number of fractional digits, reducing code length
> - fixed a bug in the code of "htam.rel" and "htam.pi" that made these functions return a wrong result

Other Minor Corrections

<br>

---

<br>

## 1.1.0 (25/09/2020)

Two new math functions:

> - "htam.rel"  >>>   coprime checker
> - "htam.tot"  >>>   Euler's Totient function

Other Changes:

> - function info restyled

Various improvements:

> - "htam.pi" speed of execution increased
> - "htam.floor" function is now literally a 1-line code, maybe i'll remove it in the future
> - now some functions reuses other functions to improve overall performances.

<br>

---

<br>


## 1.0.4 (24/09/2020)

Minor Corrections

<br>

---

<br>

## 1.0.1 (24/09/2020)

Now each function returns "None" when 1 or more arguments are not valid

<br>

---

<br>

## 1.0.0 (23/09/2020)

First Release >>> 13 math functions included:

> 1)  "htam.floor"            >>>   floor
> 2)  "htam.ceil"             >>>   ceiling
> 3)  "htam.frac"            >>>   fractional part
> 4)  "htam.root"            >>>   n-th root of a number
> 5)  "htam.mod"            >>>   linear congruence solver
> 6)  "htam.gcd"             >>>   greatest common divisor
> 7)  "htam.lcm"              >>>   least common multiple
> 8)  "htam.div"               >>>   divisors of a number
> 9)  "htam.prime"          >>>   n-th prime number
> 10) "htam.pi"                 >>>   number of primes less than a given number (pi function)
> 11) "htam.primefac"    >>>   prime factorization of a number
> 12) "htam.fac"               >>>   factorial of a number
> 13) "htam.col"                >>>   collatz conjecture checker

#! /usr/bin/python

#16 Nov 2013
#App to determine largest prime factor of a given number

from math import sqrt

number = 600851475143

def factor(num):
    if num%x==0:
        print x
        factor(num/x)
        return True



def isprime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in range (3, int(n**0.5)+1, 2):
        if n%x == 0:
            return False
    return True

x = 0    
while x < sqrt(number):
    if isprime(x):
        factor(number)
    x=x+1
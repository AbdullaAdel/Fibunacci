##!/usr/bin/env python

nterms = int(input('How many terms?\n'))

n1, n2 = 0 , 1

count = 0

print('fib sequence: ')
while count < nterms:
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    
    count += 1
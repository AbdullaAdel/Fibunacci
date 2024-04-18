##!/usr/bin/env python

nterms = int(input('How many terms?\n'))

def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n1, n2 = 0 , 1
count = 0

print('fib sequence: ')

for i in range(nterms):
    print(fibonacci(i))
    
    print('THIS IS A BRANCH')
    print('THIS IS MERGING TIME')

    print('Done Merging')
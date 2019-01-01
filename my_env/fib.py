
def fibonnaci(n):
    'recursive implementation'
    if n == 0 or n == 1:# Syntax use 'or' for '||'
     return n

    return fibonnaci(n - 1)+ fibonnaci(n - 2)

def fibonnaciDP(n):
    memo = [None]*(n + 1)
    memo[0] = 0
    memo[1] = 1

    for i in range(2,n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n]

import time
print("Recursion")
start = time.clock()
print (fibonnaci(5))
print (time.clock() - start)

start = time.clock()
print (fibonnaci(10))
print (time.clock() - start)

start = time.clock()
print (fibonnaci(30))
print (time.clock() - start)

print("Dynamic Programming -- Memoization bottom-up ")
start = time.clock()
print (fibonnaciDP(5))
print (time.clock() - start)

start = time.clock()
print (fibonnaciDP(10))
print (time.clock() - start)

start = time.clock()
print (fibonnaciDP(30))
print (time.clock() - start)


start = time.clock()
print (fibonnaciDP(100))
print (time.clock() - start)

start = time.clock()
print (fibonnaciDP(10000))
print (time.clock() - start)


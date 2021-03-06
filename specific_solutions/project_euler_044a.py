"""
Pentagonal numbers are generated by the formula, P_(n)=n(3n-1)/2. The first
ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P_(4) + P_(7) = 22 + 70 = 92 = P_(8). However, their
difference, 70-22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, P_(j) and P_(k), for which their sum
and difference is pentagonal and D = |P_(k) - P_(j)| is minimised; what
is the value of D?

"""

import time
t1 = time.time()

def pentagonal(n):
    return n * (3*n - 1) / 2

def D(k, j):
    return int(1.5*k**2 - 0.5*k - 1.5*j**2 + 0.5*j)

def is_pentagonal(x):
    # if pentagonal: returns index... else: returns False
    numerator = (24*x + 1.0)**0.5 + 1
    #print x, numerator,
    if numerator % 6 == 0:
        return int(numerator / 6)
    else:
        return False

def evaluate(k, j):
    # if sum and difference are pentagonal: return D, else: return False
    if is_pentagonal(pentagonal(k) - pentagonal(j)) and \
       is_pentagonal(pentagonal(k) + pentagonal(j)):
        return pentagonal(k) - pentagonal(j)
    else:
        return False

k = 2
solved = False
best_d = 10**10
while solved == False:
    #if k % 100 == 0:
    #    print k
    for j in xrange(k-1, 0, -1):
        if pentagonal(k) - pentagonal(j) < best_d:
            d = evaluate(k, j)
            # print k, pentagonal(k), j, pentagonal(j), d
            if d > 0 and d < best_d:
                print "possible:", k, pentagonal(k), j, pentagonal(j), d, \
                      time.time() - t1
                best_d = d
                if pentagonal(k) - pentagonal(k-1) > best_d:
                    solved = True
        else:
            break
    k += 1

print time.time() - t1


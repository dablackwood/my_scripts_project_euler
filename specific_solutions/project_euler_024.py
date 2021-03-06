"""
A permutation is an ordered arrangement of objects. For example, 3124
is one possible permutation of the digits 1, 2, 3 and 4. If all of the
permutations are listed numerically or alphabetically, we call it
lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of
the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?



def factorial(n):
    product = 1
    for item in xrange(2, n + 1):
        product = product * item
    return product

number = 2
while factorial(number) < 1000000:
    print number, "! =\t", factorial(number)
    number += 1

ended up doing this with pencil and paper -> 2783915460

"""

import probstat
p = probstat.Permutation(range(10))
print ''.join(map(str, p[999999]))

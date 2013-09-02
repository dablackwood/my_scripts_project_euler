"""
In the first one-thousand expansions of the continued fraction
representation for 2^(1/2), how many fractions contain a
numerator with more digits than denominator?

"""

import time
t1 = time.time()

def next_fraction(prev_fract):
    n = prev_fract[0]
    d = prev_fract[1]
    return (n + 2*d, n + d)

fractions = [(3,2)]
while len(fractions) < 1000:
    fractions.append(next_fraction(fractions[-1]))
#print fractions
correct = [0] * len(fractions)
for index in xrange(len(fractions)):
    if len(str(fractions[index][0])) > len(str(fractions[index][1])):
        correct[index] = 1

#print correct
print sum(correct)
print time.time() - t1

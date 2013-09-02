"""
In England the currency is made up of pound, lb., and pence, p, and
there are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, lb.1 (100p) and lb.2 (200p).

It is possible to make lb.2 in the following way:

    1xlb.1 + 1x50p + 2x20p + 1x5p+ 1x2p + 3x1p

How many different ways can lb.2 be made using any number of coins?

"""

import time
t1 = time.time()

def assign_next(value, remainder):
    #print "a", value, remainder, current, len(correct)
    place = denom.index(value)
    current[place] = remainder / value
    if value == 1:
        #print "yes", current,
        correct.append(current[:])
        #print correct
    else:
        remainder -= (remainder / value) * value
        place += 1
        assign_next(denom[place], remainder)
        place -= 1
        #print "x", value, current[place], place, current
        while current[place] > 0:
            #print "d"
            current[place] -= 1
            remainder += value
            assign_next(denom[place + 1], remainder)


denom = [200, 100, 50, 20, 10, 5, 2, 1]
current = [0] * len(denom)
remainder = 200
correct = []

assign_next(200, remainder)

print len(correct)#, correct
print time.time() - t1

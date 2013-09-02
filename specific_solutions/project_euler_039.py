"""
If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?

"""

import time
t1 = time.time()

def gen_triple(m, n):
    if m <= n:
        return False
    else:
        return [(2*m*n), (m**2 - n**2), (m**2 + n**2)]

def is_coprime(m, n):
    test = 2
    while test**2 <= m:
        if m % test == 0 and n % test == 0:
            return False
        test += 1
    return True

def add_result(p, triple):
    if p not in results:
        results[p] = [triple]
    else:
        results[sum(triple)].append(triple)

def add_multiples(p, triple):
    multiple = 2
    mult_triple = triple[:]
    while p * multiple <= 1000:
        for side in xrange(3):
            mult_triple[side] = multiple * triple[side]
        add_result(p * multiple, mult_triple)
        multiple += 1
        
results = {}
tabulated = {}
m = 2
while m**2 < 500:
    n = 1
    while n < m:
        if is_coprime(m, n):
            triple = gen_triple(m, n)
            p = sum(triple)
            if p <= 1000:
                #print p, triple, m, n
                add_result(p, triple)
                add_multiples(p, triple)
        n += 1
    m += 1

for key in results:
    tabulated[key] = len(results[key])

best_index = tabulated.values().index(max(tabulated.values()))
print tabulated.keys()[best_index], "= p"
#print results[tabulated.keys()[best_index]]
#print results[120]
#print tabulated
#print results
print time.time() - t1

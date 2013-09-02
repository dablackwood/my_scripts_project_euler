"""
How many, not necessarily distinct, values of C(n, r), for 1 <= n <= 100,
are greater than one-million?

"""
import time
t1 = time.time()

def next_pascal(prev_row):
    #print prev_row
    next_row = [1]
    for index in xrange(1, len(prev_row)):
        next_row.append(prev_row[index] + prev_row[index - 1])
        #print next_row
    next_row.append(1)
    return next_row

def row_count(row):
    for index in xrange(2, (1 + len(row)) / 2):
        if row[index] >= 1000000:
            return (1 + row[1] - 2 * index)
    return 0

tally = 0
row = [1, 4, 6, 4, 1]
while row[1] < 101:
    tally += row_count(row)
    row = next_pascal(row)

print tally
print time.time() - t1

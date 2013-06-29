# Find the sum of the multiples of three or five below 1000
total = 0
n = 3
while n < 1000:
    #print n,
    if n % 3 == 0 or n % 5 == 0:
        #print "*",
        total = total + n
    #else:
        #print " ",
    #print total
    n = n + 1
print total

# Find the difference between the sum of the squares of the first
# one hundred natural numbers and the square of the sum.


# the first 'k' numbers
k=100
n=1
iteration = 0
sum = 0

while n <= k:
    iteration = n*k**2 + n*k - n**2 - n**3
    sum = sum + iteration
    n = n+1

print sum

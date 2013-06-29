fib_list = [1,2]

def next_fib(list):
    index = len(list)
    list.append(list[index-2] + list[index-1])

def even_sum(list):
    total = 0
    n = 0
    while n <= len(list)-1:
        if n % 3 == 1:
            total = total + list[n]
        n = n + 1
    return total

while fib_list[len(fib_list)-1] < 4000000:
    next_fib(fib_list)

# print fib_list
print even_sum(fib_list)

# correct!


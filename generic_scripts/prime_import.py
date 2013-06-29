
import time
t1 = time.time()

def prime_import():
    infile = open('prime_list_e6.txt', 'r') # specifiy which file to use
    prime_list = infile.read()
    prime_list = prime_list.split(',')
    prime_list = prime_list[:-1]
    infile.close()
    #print prime_list[:20]
    for index in xrange(len(prime_list)):
        prime_list[index] = int(prime_list[index])
    #print prime_list[:20]
    return prime_list


prime_list = prime_import()

#print prime_list[-20:]

print time.time() - t1

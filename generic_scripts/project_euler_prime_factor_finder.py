# this program will generate the prime factorization of the input

def is_factor(n, k):
    b = 0
    divided = n
    if divided % k != 0:
        return
    else:
        while divided % k == 0:
            divided = divided / k
            b = b + 1
        return [divided, k, b]
    
def factorize(n):
    factor_list = {}#[]
    remains = n
    result = []
    k = 2
    while k <= remains:
        if remains == 1:
            return factor_list
        result = is_factor(remains, k)
        if result is not None:
            remains = result[0]
            del result[0]        
            factor_list[result[0]] = result[1]#.append(result)
        elif k > remains:
            return factor_list
        if k == 2:
            k = k + 1
        else:
            k = k + 2
    if factor_list == {}:
        factor_list = 'prime'
    return factor_list
        
number_in_question = input("What number would you like to factor: ")
print number_in_question, factorize(number_in_question)


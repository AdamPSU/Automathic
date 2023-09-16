#sum_of_odd calculates all the postive odd integers before n

def sum_of_odd(n):
    hashset = set() 
    for i in range(1, n*2):
        if i % 2 == 1:
            hashset.add(i) 
    return sorted(list(hashset))  

def integer_multiples(n, m): 
    hashset = set() 
    for i in range(1, n+1): 
        hashset.add(i*m)
    return sorted(list(hashset)) 




#sum_of_odd calculates all the postive odd integers before n

def sum_of_odd(n):

    sum = 0

    for i in range(1, n):
        if i % 2 == 1:
            sum += i 

    return sum

print(sum_of_odd(6))
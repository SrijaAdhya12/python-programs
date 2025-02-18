def mini_max_sum(my_numlist):
    new_numlist = sorted(my_numlist)
    min_sum = sum(new_numlist[:-1])
    max_sum = sum(new_numlist[1:])
    return min_sum , max_sum

print(mini_max_sum(list(map(int, input("Enter a list: ").split()))))


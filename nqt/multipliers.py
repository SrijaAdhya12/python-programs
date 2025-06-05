

def multiples_of_ten(my_list):
    j = 0
    for i in range(len(my_list)):
        if my_list[i] % 10 != 0:
            my_list[i], my_list[j] = my_list[j] , my_list[i]
            j+=1
    


my_list = list(map(int, input().split(" ")))
multiples_of_ten(my_list)
print(my_list)

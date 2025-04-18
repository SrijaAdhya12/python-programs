def standard_deviation(my_list):
    new_list = []
    mean = sum(my_list)/len(my_list)
    for i in my_list:
        val = (i - mean)*(i - mean)
        new_list.append(val)
    total_sumation =  sum(new_list)
    standard_def = (total_sumation/len(my_list))**0.5
    return standard_def
    


my_list = list(map(int, input().split()))
print(f"{standard_deviation(my_list):.2f}")


    
    
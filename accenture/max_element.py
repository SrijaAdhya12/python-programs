def find_maxelement(num_list):
    max_element = num_list[0]
    max_index = 0
    for k,v in enumerate(num_list):
        if v > max_element:
            max_element = v
            max_index = k
    print(max_element)
    print(max_index)





num_list = list(map(int, input().split()))
find_maxelement(num_list)

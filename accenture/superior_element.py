def find_superior_element(num_list):
    max_element = float("-inf")
    total_count = 0

    for i in range(len(num_list)-1,-1,-1):
        if num_list[i] > max_element:
            max_element = num_list[i]
            total_count += 1
    return total_count


n = int(input())
num_list = list(map(int, input().split(" ")))
print(find_superior_element(num_list))
 
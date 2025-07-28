def find_oddsum(num_list):
    sum = 0

    for i in num_list:
        if i % 2 != 0:
            sum += i
    return sum










num_list = list(map(int , input().split(" ")))
print(find_oddsum(num_list))
def odd_evenlist(num_list):
    res = ""
    for i in num_list:
        if i % 2 == 0:
            res += "even"
        else:
            res += "odd"
    return res





num_list = list(map(int, input().split(" ")))
print(odd_evenlist(num_list))

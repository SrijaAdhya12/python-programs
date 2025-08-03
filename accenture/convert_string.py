def convert_string(s):
    count_upper = 0
    count_lower = 0
    for i in s:
        if i.isupper():
            count_upper += 1
        else:
            count_lower += 1
    return s.upper() if  count_upper > count_lower else s.lower()


s = input()
print(convert_string(s))

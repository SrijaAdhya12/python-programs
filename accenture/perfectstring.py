def perfect_string(s):
    length = 0
    max_length = 0
    for i in s:
        if i == ".":
            max_length = max(max_length, length)
            length = 0
        else:
            length +=1
        
    return max(max_length, length)


s = input()
print(perfect_string(s))

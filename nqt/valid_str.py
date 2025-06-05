def valid_str(my_str):
    count_hash = 0
    count_star = 0
    for i in my_str:
        if i == "*":
            count_star += 1
        else:
            count_hash += 1
    if count_star > count_hash:
        return count_star - count_hash
    if count_star < count_hash:
        return count_star - count_hash
    return count_star - count_hash




my_str = input()
print(valid_str(my_str))

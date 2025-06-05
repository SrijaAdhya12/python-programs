def hiking(s):
    count = 0
    total_ride=0
    for i in s:
        if i == 'U':
            count+=1
        else:
            count-=1
        if i == 'U' and count == 0:
            total_ride+=1
    return total_ride   

    



s = input()
print(hiking(s))

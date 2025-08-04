def find_bread(s):
    stack = []
    res = ""

    for ch in s:
        if stack and ch == stack[0]:
            res += ch
            stack.clear()  
        else:
            stack.append(ch)

    return res


s = input().strip()
print(find_bread(s))

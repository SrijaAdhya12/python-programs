def find_oddstr(s):
    for i in range(len(s) -1, -1, -1):
        if int(s[i]) % 2 != 0:
            return s[:i+1]
    return "No odd string"
    

s = input()
print(find_oddstr(s))
def remove_p(s):
    removal = 0
    for i in range(len(s)-2):
        if s[i] == "p" and s[i+1] == "p" and s[i+2] == "p":
            removal += 1
    return removal




s = input()
print(remove_p(s))
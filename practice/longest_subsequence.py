def longest_subsequence(text1 , text2):
    set1 = set(text1)
    set2 = set(text2)
    
    common = set1 & set2
    print(common)
    return len(common)

text1 = input("Enter text 1: ")
text2 = input("Enter text 2: ")


def longest_subsequense(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

print(longest_subsequence(text1,text2))

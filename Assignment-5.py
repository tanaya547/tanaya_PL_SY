# Longest Common Subsequence (LCS) using Dynamic Programming

def lcs(str1, str2):
    m, n = len(str1), len(str2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    i, j = m, n
    ans = []

    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            ans.append(str1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    ans.reverse()
    return "".join(ans), dp[m][n]


# Main Program
sequence1 = input("Enter the first sequence: ")
sequence2 = input("Enter the second sequence: ")

res, length = lcs(sequence1, sequence2)

print("\nLongest Common Subsequence:", res)
print("Length of LCS:", length)

# Output 1:
# Enter the first sequence: ABCDEF
# Enter the second sequence: ACDF
# Longest Common Subsequence: ACDF
# Length of LCS: 4

# Output 2:
# Enter the first sequence: ABCXYZ
# Enter the second sequence: AXBYCZ
# Longest Common Subsequence: ABCZ
# Length of LCS: 4

# Output 3:
# Enter the first sequence: PQRST
# Enter the second sequence: PRSTU
# Longest Common Subsequence: PRST
# Length of LCS: 4

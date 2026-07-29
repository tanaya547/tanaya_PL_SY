# Fibonacci using Dynamic Programming

def fib_memo(num, dp):
    if num <= 1:
        return num

    if dp[num] != -1:
        return dp[num]

    dp[num] = fib_memo(num - 1, dp) + fib_memo(num - 2, dp)
    return dp[num]


def fib_tab(num):
    if num <= 1:
        return num

    dp = [0] * (num + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, num + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[num]


# Driver Code
num = int(input("Enter Fibonacci position: "))

dp = [-1] * (num + 1)

memo_result = fib_memo(num, dp)
tab_result = fib_tab(num)

print("\nResult using Memoization :", memo_result)
print("Result using Tabulation  :", tab_result)

# Output:
# Enter Fibonacci position: 12

# Result using Memoization : 144
# Result using Tabulation  : 144
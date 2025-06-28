t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    prices = list(map(int, input().split()))

    if k == 0 or n == 0:
        print(0)
        continue

    if k >= n // 2:
        profit = 0
        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        print(profit)
        continue

    dp = [[0] * n for _ in range(k + 1)]

    for i in range(1, k + 1):
        max_diff = -prices[0]
        for j in range(1, n):
            dp[i][j] = max(dp[i][j - 1], prices[j] + max_diff)
            max_diff = max(max_diff, dp[i - 1][j] - prices[j])

    print(dp[k][n - 1])

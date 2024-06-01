def graduation_prob(N):
    dp = [0] * (N + 1)
    dp[0] = 1
    dp[1] = 2
    dp[2] = 4
    dp[3] = 7
    for i in range(4, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    total_ways = 2 ** N
    ways_to_miss = total_ways - dp[N]
    return ways_to_miss
    
def attendance_ways(N):
    dp = [[0] * 4 for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(1, N + 1):
        dp[i][0] = sum(dp[i - 1])
        for j in range(1, 4):
            dp[i][j] = dp[i - 1][j - 1]
    total_ways = sum(dp[N])
    missed_ceremony_ways = sum(dp[N - 1][1:])

    return total_ways

input_n = 5
ways_to_miss = graduation_prob(input_n)
total_ways = attendance_ways(input_n)
print(str(ways_to_miss)+'/'+str(total_ways))

#Задача про лягушку
def frog_routes(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    dp = [0] * (n + 1)
    dp[1] = 1
    if n >= 2:
        dp[2] = 1
    if n >= 3:
        dp[3] = 2
    for i in range(4, n + 1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    return dp[n]


#Задача про матрицу
def min_path_sum(matrix):
    if not matrix or not matrix[0]:
        return 0
    m, n = len(matrix), len(matrix[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = matrix[0][0]

    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + matrix[0][j]
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + matrix[i][0]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = matrix[i][j] + min(dp[i-1][j], dp[i][j-1])
    return dp[m-1][n-1]


#Задача про монеты

def min_coins(coins, s):
    if s == 0:
        return 0
    if not coins or s < 0:
        return -1
    dp = [float('inf')] * (s + 1)
    dp[0] = 0
    for i in range(1, s + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[s] if dp[s] != float('inf') else -1

#задача про массив

def longest_increasing_subsequence(arr):
    if not arr:
        return 0
    n = len(arr)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


#задача про рюкзак

def knapsack(W, weights, values):
    n = len(weights)
    dp = [0] * (W + 1)
    for i in range(n):
        weight, value = weights[i], values[i]
        for j in range(W, weight - 1, -1):
            dp[j] = max(dp[j], dp[j - weight] + value)
    return dp[W]



if __name__ == "__main__":
    print("задача про лягушку (n=7)")
    print(f"результат: {frog_routes(7)}\n")

    print("задача про лягушку (n=10)")
    print(f"результат: {frog_routes(10)}\n")

    print("задача про матрицы")
    mat = [[2, 4, 1, 3], [1, 6, 2, 1], [3, 1, 5, 2]]
    print(f"результат: {min_path_sum(mat)}\n")

    print("задача про матрицы (2x2)")
    mat2 = [[3, 7], [2, 5]]
    print(f"результат: {min_path_sum(mat2)}\n")

    print("задача про монеты (сумма 15, номиналы [1, 3, 4])")
    print(f"результат: {min_coins([1, 3, 4], 15)}\n")

    print("задача про монеты (сумма 8, номиналы [2, 5])")
    print(f"результат: {min_coins([2, 5], 8)}\n")

    print("задача про монеты (сумма 3, номиналы [2, 4])")
    print(f"результат: {min_coins([2, 4], 3)}\n")

    print("задача про возрастающую подпоследовательность")
    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"результат: {longest_increasing_subsequence(arr)}\n")

    print("задача про возрастающую подпоследовательность")
    arr2 = [1, 2, 3, 4, 5]
    print(f"результат: {longest_increasing_subsequence(arr2)}\n")

    print("задача про рюкзак (вместимость 7)")
    weights = [1, 2, 3, 5]
    values = [1, 6, 10, 16]
    print(f"результат: {knapsack(7, weights, values)}\n")

    print("задача про рюкзак (вместимость 10)")
    weights2 = [3, 4, 5, 6]
    values2 = [2, 3, 4, 5]
    print(f"результат: {knapsack(10, weights2, values2)}\n")


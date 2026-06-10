def knapsack_dynamic_programming(C, items):
    n = len(items)
    dp = [[0] * (C + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        current_p = items[i - 1]["p"]
        current_w = items[i - 1]["w"]
        for w in range(C + 1):
            if current_w <= w:
                dp[i][w] = max(
                    dp[i - 1][w], dp[i - 1][w - current_w] + current_p
                )
            else:
                dp[i][w] = dp[i - 1][w]
    max_value = dp[n][C]
    chosen_items = []
    w = C
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            chosen_items.append(items[i - 1])
            w -= items[i - 1]["w"]
    chosen_items.reverse()

    return max_value, chosen_items
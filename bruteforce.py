import itertools

def knapsack_brute_force(C, items):
    best_value = 0
    best_combination = []
    for r in range(len(items) + 1):
        for combination in itertools.combinations(items, r):
            total_weight = sum(item["w"] for item in combination)
            total_value = sum(item["p"] for item in combination)
            if total_weight <= C and total_value > best_value:
                best_value = total_value
                best_combination = list(combination)

    return best_value, best_combination
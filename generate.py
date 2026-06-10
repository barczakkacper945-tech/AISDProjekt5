import random

def generate_knapsack_data(filename, C, n, max_value=50, max_weight=20):
    with open(filename, "w") as f:
        f.write(f"{C}\n")
        f.write(f"{n}\n")
        for _ in range(n):
            p = random.randint(1, max_value)
            w = random.randint(1, max_weight)
            f.write(f"{p} {w}\n")
    print(f"Dane zostały wygenerowane i zapisane do pliku: {filename}")
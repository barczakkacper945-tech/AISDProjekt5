def read_knapsack_data(filename):
    with open(filename, "r") as f:
        lines = f.read().splitlines()
    C = int(lines[0].strip())
    n = int(lines[1].strip())
    items = []
    for idx, line in enumerate(lines[2 : 2 + n]):
        if line.strip():
            p, w = map(int, line.split())
            items.append({"id": idx + 1, "p": p, "w": w})

    return C, n, items
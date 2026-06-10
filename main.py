import itertools
import random
import time
from generate import generate_knapsack_data
from read import read_knapsack_data
from bruteforce import knapsack_brute_force
from dynamicprogramming import knapsack_dynamic_programming

if __name__ == "__main__":
    file_name = "knapsack_data.txt"

    pojemnosc_C = 50
    liczba_przedmiotow_n = 15

    generate_knapsack_data(file_name, pojemnosc_C, liczba_przedmiotow_n)
    print("-" * 50)

    C, n, items = read_knapsack_data(file_name)
    print(f"Wczytano dane: Pojemność plecaka C = {C}, Liczba przedmiotów n = {n}")
    print("Przedmioty dostępne do spakowania:")
    for item in items:
        print(f"  Przedmiot {item['id']}: Wartość = {item['p']}, Waga = {item['w']}")

    print("-" * 50)

    start_bf = time.time()
    val_bf, items_bf = knapsack_brute_force(C, items)
    end_bf = time.time()

    print("=== WYNIK BRUTE FORCE ===")
    print(f"Maksymalna wartość: {val_bf}")
    print(f"Całkowita waga: {sum(i['w'] for i in items_bf)}")
    print(f"Spakowane przedmioty (ID): {[i['id'] for i in items_bf]}")
    print(f"Czas wykonania BF: {end_bf - start_bf:.6f} sekund")

    print("-" * 50)
    start_dp = time.time()
    val_dp, items_dp = knapsack_dynamic_programming(C, items)
    end_dp = time.time()

    print("=== WYNIK PROGRAMOWANIA DYNAMICZNEGO ===")
    print(f"Maksymalna wartość: {val_dp}")
    print(f"Całkowita waga: {sum(i['w'] for i in items_dp)}")
    print(f"Spakowane przedmioty (ID): {[i['id'] for i in items_dp]}")
    print(f"Czas wykonania PD: {end_dp - start_dp:.6f} sekund")
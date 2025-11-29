# Exercice 4 : Programmation Dynamique
import string
import random
import time

# 4.1 - Fibonacci Naïf 

def fibonacci_naif(n):
    if n <= 1:
        return n
    return fibonacci_naif(n-1) + fibonacci_naif(n-2)

# Mettre en commentaire pour skip et avoir un résultat plus rapide
print(" Fibonacci Naïf pour n = 30: " + str(fibonacci_naif(30)))
print(" Fibonacci Naïf pour n = 40: " + str(fibonacci_naif(40)))
print(" Fibonacci Naïf pour n = 50: " + str(fibonacci_naif(50)))

# Fibonacci avec Memoization

def dp_main():
    print("4.1 - Fibonacci")

    def fibonacci_memoization(n, memo={}):
        if n in memo:
            return memo[n]
        if n <= 1:
            return n
        memo[n] = fibonacci_memoization(n-1, memo) + fibonacci_memoization(n-2, memo)
        return memo[n]
    start = time.perf_counter()
    print(" Fibonacci avec Memoization pour n = 30: " + str(fibonacci_memoization(30)))
    end = time.perf_counter()
    print(f"Durée totale n = 30 : {end - start:.6f} s")

    start = time.perf_counter()
    print(" Fibonacci avec Memoization pour n = 40: " + str(fibonacci_memoization(40)))
    end = time.perf_counter()
    print(f"Durée totale n = 40 : {end - start:.6f} s")

    start = time.perf_counter()
    print(" Fibonacci avec Memoization pour n = 50: " + str(fibonacci_memoization(50)))
    end = time.perf_counter()
    print(f"Durée totale n = 50 : {end - start:.6f} s")
    print("--------------------------------")

    # Fibonacci par Itération

    def fibonacci_iteration(n):
        if n <=1:
            return n
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    start = time.perf_counter()
    print(" Fibonacci par Itération pour n = 30: " + str(fibonacci_iteration(30)))
    end = time.perf_counter()
    print(f"Durée totale n = 30 : {end - start:.6f} s")
    print(" Fibonacci par Itération pour n = 40: " + str(fibonacci_iteration(40)))
    end = time.perf_counter()
    print(f"Durée totale n = 40 : {end - start:.6f} s")
    start = time.perf_counter()
    print(" Fibonacci par Itération pour n = 50: " + str(fibonacci_iteration(50)))
    end = time.perf_counter()
    print(f"Durée totale n = 50 : {end - start:.6f} s")
    print("--------------------------------")
    # Fibonacci Optimisé

    def fibonacci_optimise(n: int) -> int:
        if n <= 1:
            return n
        prev, curr = 0, 1
        for _ in range(2, n + 1):
            prev, curr = curr, prev + curr
        return curr

    start = time.perf_counter()
    print(" Fibonacci Optimisé pour n = 30: " + str(fibonacci_optimise(30)))
    end = time.perf_counter()
    print(f"Durée totale n = 30 : {end - start:.6f} s")
    start = time.perf_counter()
    print(" Fibonacci Optimisé pour n = 40: " + str(fibonacci_optimise(40)))
    end = time.perf_counter()
    print(f"Durée totale n = 40 : {end - start:.6f} s")
    start = time.perf_counter()
    print(" Fibonacci Optimisé pour n = 50: " + str(fibonacci_optimise(50)))
    end = time.perf_counter()
    print(f"Durée totale n = 50 : {end - start:.6f} s")
    print("--------------------------------")



    # 4.2 - Sac à dos 0/1
    print("4.2 - Sac à dos 0/1")
    def knapsack(weights, values, capacity):
        n = len(weights)
        dp = [[0]* (capacity + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for w in range(capacity + 1):
                if weights[i-1] <= w:
                    dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
                else:
                    dp[i][w] = dp[i-1][w]
        return dp[n][capacity]

    def knapsack_bruteforce(weights, values, capacity):
        n = len(weights)
        best = 0

        def brute_force(i, poids, valeur):
            nonlocal best
            if poids > capacity:
                return
            if i == n:
                best = max(best, valeur)
                return
            brute_force(i + 1, poids, valeur)
            brute_force(i + 1, poids + weights[i], valeur + values[i])

        brute_force(0, 0, 0)
        return best

    weights = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
    values = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
    capacity = 50
    start = time.perf_counter()
    print("Sac à dos 0/1 (DP) : " + str(knapsack(weights, values, capacity)))
    end = time.perf_counter()
    print(f"Durée totale : {end - start:.6f} s")
    print("--------------------------------")
    start = time.perf_counter()
    print("Sac à dos 0/1 (Bruteforce) : " + str(knapsack_bruteforce(weights, values, capacity)))
    end = time.perf_counter()
    print(f"Durée totale : {end - start:.6f} s")
    print("--------------------------------")

    # 4.3 - Plus Longue Sous-Séquence Commune (LCS)

    def generate_random_string(length):
        return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))

    print("4.3 - Plus Longue Sous-Séquence Commune (LCS)")
    def lcs(str1, str2):
        m = len(str1)
        n = len(str2)
        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]

    str1 = generate_random_string(100)
    str2 = generate_random_string(100)
    start = time.perf_counter()
    print("LCS de " + str1 + " et " + str2 + " : " + str(lcs(str1, str2)))
    end = time.perf_counter()
    print(f"Durée totale : {end - start:.6f} s")
    print("--------------------------------")

    # 4.3 - Plus Longue Sous-Séquence Commune (LCS) Optimisé -> O(min(m, n))
    print("4.3 - Plus Longue Sous-Séquence Commune (LCS) Optimisé ")
    def lcs_optimise(str1, str2):
        m = len(str1)
        n = len(str2)
        if m < n:
            str1, str2 = str2, str1
            m, n = n, m
        dp = [0]*(n+1)
        for i in range(1, m+1):
            prev = 0
            for j in range(1, n+1):
                current = dp[j]
                if str1[i-1] == str2[j-1]:
                    dp[j] = prev + 1
                else:
                    dp[j] = max(dp[j], dp[j-1])
                prev = current
        return dp[n]

    start = time.perf_counter()
    print("LCS Optimisé de " + str1 + " et " + str2 + " : " + str(lcs_optimise(str1, str2)))
    end = time.perf_counter()
    print(f"Durée totale : {end - start:.6f} s")
    print("--------------------------------")
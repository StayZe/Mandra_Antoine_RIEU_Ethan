
items = [(60, 10), (100, 20), (120, 30)] 
W = 50

def solve_fractionnaire(objets, capacite):
    objets_tries = sorted(objets, key=lambda x: x[0]/x[1], reverse=True)
    valeur = 0
    reste = capacite
    
    for v, p in objets_tries:
        if reste == 0: break
        quantite = min(p, reste)
        valeur += quantite * (v / p)
        reste -= quantite
    return valeur

def solve_01_dp(objets, capacite):
    dp = [0] * (capacite + 1)
    
    for v, p in objets:
        for w in range(capacite, p - 1, -1):
            dp[w] = max(dp[w], dp[w - p] + v)
    return dp[capacite]

res_frac = solve_fractionnaire(items, W)
res_01 = solve_01_dp(items, W)

print(f"Objets (Valeur, Poids) : {items}")
print(f"Capacité du sac        : {W}")
print("-" * 30)
print(f"1. Fractionnaire (Glouton) : {res_frac}")
print(f"2. Entier 0/1 (DP)         : {res_01}")
print("-" * 30)
print(f"Différence (Perte)         : {res_frac - res_01}")
def monnaie():
    """Algorithme glouton de rendu de monnaie"""
    print("=" * 80)
    print("1. RENDU DE MONNAIE - ALGORITHME GLOUTON")
    print("=" * 80)
    
    def rendu_monnaie_glouton(montant, systeme_monetaire):
        pieces_triees = sorted(systeme_monetaire, reverse=True)
        
        resultat = []
        reste = montant
        
        for piece in pieces_triees:
            if piece <= reste:
                nombre_de_pieces = reste // piece 
                resultat.extend([piece] * nombre_de_pieces) 
                reste = reste % piece 
        return resultat
    
    systeme = [1, 2, 5, 10, 20, 50, 100]
    montant_cible = 37
    
    solution = rendu_monnaie_glouton(montant_cible, systeme)
    
    print(f"\nSystème monétaire : {systeme}")
    print(f"Montant à rendre : {montant_cible}")
    print(f"Pièces rendues : {solution}")
    print(f"Nombre total de pièces : {len(solution)}")
    print()


def activity():
    """Algorithme glouton de sélection d'activités"""
    print("=" * 80)
    print("2. SÉLECTION D'ACTIVITÉS - ALGORITHME GLOUTON")
    print("=" * 80)
    
    def selection_activites(activites):
        activites_triees = sorted(activites, key=lambda x: x[2])
        selection = []
        derniere_fin = 0
        
        print(f"\nOrdre après tri par fin : {activites_triees}\n")
        print("--- Déroulement ---")

        for act in activites_triees:
            nom, debut, fin = act
            if debut >= derniere_fin:
                selection.append(nom)
                derniere_fin = fin
                print(f"[OUI] {nom} ({debut}-{fin}) : Sélectionnée (début {debut} >= fin précédente)")
            else:
                print(f"[NON] {nom} ({debut}-{fin}) : Rejetée (début {debut} < fin précédente {derniere_fin})")
        return selection
    
    liste_activites = [
        ("A1", 1, 3),
        ("A2", 2, 5),
        ("A3", 4, 6),
        ("A4", 5, 8)
    ]
    
    print(f"\nListe originale : {liste_activites}")
    resultat = selection_activites(liste_activites)
    
    print("\n--- Résultat Final ---")
    print(f"Activités retenues : {resultat}")
    print(f"Nombre total : {len(resultat)}")
    print()


def knapsack():
    """Problème du sac à dos - Comparaison Glouton vs Programmation Dynamique"""
    print("=" * 80)
    print("3. SAC À DOS FRACTIONNAIRE VS ENTIER 0/1")
    print("=" * 80)
    
    items = [(60, 10), (100, 20), (120, 30)] 
    W = 50
    
    def solve_fractionnaire(objets, capacite):
        objets_tries = sorted(objets, key=lambda x: x[0]/x[1], reverse=True)
        valeur = 0
        reste = capacite
        
        for v, p in objets_tries:
            if reste == 0: 
                break
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
    
    print(f"\nObjets (Valeur, Poids) : {items}")
    print(f"Capacité du sac        : {W}")
    print("-" * 30)
    print(f"1. Fractionnaire (Glouton) : {res_frac}")
    print(f"2. Entier 0/1 (DP)         : {res_01}")
    print("-" * 30)
    print(f"Différence (Perte)         : {res_frac - res_01}")
    print()


def main():
    """Fonction principale qui exécute tous les algorithmes gloutons"""
    print("\n")
    print("╔" + "═" * 78 + "╗")
    print("║" + " " * 20 + "ALGORITHMES GLOUTONS (GREEDY)" + " " * 29 + "║")
    print("╚" + "═" * 78 + "╝")
    print()
    
    # Exécution des 3 algorithmes
    monnaie()
    print("\n")
    
    activity()
    print("\n")
    
    knapsack()
    print("\n")
    
    # Conclusion
    print("=" * 80)
    print("ANALYSE DES ALGORITHMES GLOUTONS")
    print("=" * 80)
    print("""
Les algorithmes gloutons font des choix localement optimaux à chaque étape
dans l'espoir d'obtenir une solution globalement optimale.

Avantages :
  - Simplicité d'implémentation
  - Efficacité temporelle (généralement O(n log n) à cause du tri)
  - Faible utilisation de mémoire

Inconvénients :
  - Ne garantit pas toujours la solution optimale
  - Nécessite une analyse rigoureuse pour prouver l'optimalité

Applications classiques :
  1. Rendu de monnaie : Optimal pour certains systèmes monétaires
  2. Sélection d'activités : Toujours optimal (stratégie "earliest finish")
  3. Sac à dos fractionnaire : Optimal, mais pas pour le 0/1 entier
    """)


if __name__ == "__main__":
    main()


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

print(f"Système monétaire : {systeme}")
print(f"Montant à rendre : {montant_cible}")
print(f"Pièces rendues : {solution}")
print(f"Nombre total de pièces : {len(solution)}")
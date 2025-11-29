def selection_activites(activites):
    activites_triees = sorted(activites, key=lambda x: x[2])
    selection = []
    derniere_fin = 0
    
    print(f"Ordre après tri par fin : {activites_triees}\n")
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

print(f"Liste originale : {liste_activites}")
resultat = selection_activites(liste_activites)

print("\n--- Résultat Final ---")
print(f"Activités retenues : {resultat}")
print(f"Nombre total : {len(resultat)}")
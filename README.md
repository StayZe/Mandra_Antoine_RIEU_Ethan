# TP Algo Avancée - ESGI B3 - Mandra Antoine | Rieu Ethan

Projet d'implémentation et d'analyse d'algorithmes fondamentaux en Python.

## 📋 Contenu du projet

Ce projet contient les implémentations suivantes :

1. **Algorithmes de tri** (`src/sorting.py`)
   - Bubble Sort (Tri à bulles)
   - Insertion Sort (Tri par insertion)
   - Merge Sort (Tri fusion)
   - Quick Sort (Tri rapide)
   - Selection Sort (Tri par sélection)

2. **Structures de données** (`src/data_structures.py`)
   - Stack (Pile)
   - Queue (File)
   - Heap (Tas)

3. **Programmation dynamique** (`src/dp.py`)
   - Fibonacci (Naïf, Mémoïsation, Itératif, Optimisé)
   - Sac à dos 0/1
   - Plus longue sous-séquence commune (LCS)

4. **Algorithmes gloutons** (`src/greedy.py`)
   - Rendu de monnaie
   - Sélection d'activités
   - Sac à dos fractionnaire vs 0/1

5. **Compression** (`src/compression.py`)
   - Algorithme de Huffman

## 🚀 Lancement des scripts

### Prérequis

Python 3.7 ou supérieur

### Exécuter tous les algorithmes

Pour exécuter l'ensemble des algorithmes et voir tous les résultats :

```bash
python tests/test_all.py
```

Cette commande exécute tous les modules dans l'ordre et affiche les résultats dans la console.

### Exécuter un module spécifique

Vous pouvez également exécuter chaque module individuellement :

#### Algorithmes de tri
```bash
python src/sorting.py
```
Teste et benchmark 5 algorithmes de tri sur différentes tailles de données (100, 1000, 5000, 10000 éléments).

#### Structures de données
```bash
python src/data_structures.py
```
Démontre l'utilisation des piles, files et tas.

#### Programmation dynamique
```bash
python src/dp.py
```
Compare les performances des différentes approches (récursif, DP, itératif) pour Fibonacci, sac à dos et LCS.

#### Algorithmes gloutons
```bash
python src/greedy.py
```
Exécute les algorithmes gloutons pour le rendu de monnaie, la sélection d'activités et le sac à dos.

#### Compression Huffman
```bash
python src/compression.py
```
Teste la compression Huffman sur différents types de données et génère un rapport dans `results/compression_analysis.txt`.

## 📁 Structure du projet

```
.
├── README.md
├── src/
│   ├── sorting.py              # Algorithmes de tri
│   ├── data_structures.py      # Structures de données
│   ├── dp.py                   # Programmation dynamique
│   ├── greedy.py               # Algorithmes gloutons
│   ├── compression.py          # Compression Huffman
│   ├── main.py                 # (optionnel)
│   ├── sorting/                # Versions originales des tris
│   └── exercice-5/             # Versions originales des algorithmes gloutons
├── tests/
│   └── test_all.py             # Script principal pour tout exécuter
└── results/                    # Dossier des résultats
    ├── compression_analysis.txt
    ├── complexity_analysis.txt
    ├── data_structures.txt
    ├── dp_results.txt
    └── sorting_benchark.txt
```

## 📊 Résultats

Certains modules génèrent des fichiers de résultats dans le dossier `results/` :

- `compression_analysis.txt` : Analyse détaillée de la compression Huffman

## 👥 Auteurs

- Mandra Antoine
- RIEU Ethan

## 📝 Notes

- Tous les résultats s'affichent directement dans la console
- Les benchmarks utilisent des données aléatoires, les temps d'exécution peuvent varier
- Pour les algorithmes de tri, les tailles testées vont de 100 à 10 000 éléments


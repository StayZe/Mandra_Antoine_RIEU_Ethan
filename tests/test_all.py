import sys
import os

# Ajouter le répertoire parent au path pour pouvoir importer les modules src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import compression, data_structures, dp, greedy, sorting
from collections import deque
import heapq


def print_separator(title):
    """Affiche un séparateur visuel avec un titre"""
    print("\n\n")
    print("╔" + "═" * 78 + "╗")
    print("║" + f"{title:^78}" + "║")
    print("╚" + "═" * 78 + "╝")
    print()


def run_data_structures():
    """Exécute les exercices sur les structures de données"""
    print_separator("STRUCTURES DE DONNÉES")
    
    print("=" * 80)
    print("2.1 - PILE (STACK)")
    print("=" * 80)
    stack = [1, 2, 3, 4, 5]
    data_structures.stack_exercice(stack)
    
    print("\n" + "=" * 80)
    print("2.2 - FILE (QUEUE)")
    print("=" * 80)
    queue = deque([])
    data_structures.queue_exercice(queue)
    
    print("\n" + "=" * 80)
    print("2.3 - TAS (HEAP)")
    print("=" * 80)
    heap = []
    heap2 = [5, 3, 7]
    data_structures.heap_exercice(heap, heap2)
    print()


def main():
    """Fonction principale qui exécute tous les tests"""
    print("\n")
    print("╔" + "═" * 78 + "╗")
    print("║" + " " * 15 + "EXÉCUTION COMPLÈTE DE TOUS LES ALGORITHMES" + " " * 20 + "║")
    print("╚" + "═" * 78 + "╝")
    
    # 1. Algorithmes de tri
    try:
        print_separator("1. ALGORITHMES DE TRI")
        sorting.main()
    except Exception as e:
        print(f"❌ Erreur lors de l'exécution de sorting: {e}")
    
    # 2. Structures de données
    try:
        run_data_structures()
    except Exception as e:
        print(f"❌ Erreur lors de l'exécution de data_structures: {e}")
    
    # 3. Programmation dynamique
    try:
        print_separator("3. PROGRAMMATION DYNAMIQUE")
        dp.dp_main()
    except Exception as e:
        print(f"❌ Erreur lors de l'exécution de dp: {e}")
    
    # 4. Algorithmes gloutons
    try:
        print_separator("4. ALGORITHMES GLOUTONS (GREEDY)")
        greedy.main()
    except Exception as e:
        print(f"❌ Erreur lors de l'exécution de greedy: {e}")
    
    # 5. Compression Huffman
    try:
        print_separator("5. COMPRESSION HUFFMAN")
        compression.compression_main()
    except Exception as e:
        print(f"❌ Erreur lors de l'exécution de compression: {e}")
    
    # Conclusion
    print("\n\n")
    print("╔" + "═" * 78 + "╗")
    print("║" + " " * 25 + "TOUS LES TESTS SONT TERMINÉS" + " " * 25 + "║")
    print("╚" + "═" * 78 + "╝")
    print("\n")
    print("Résumé des modules exécutés:")
    print("  ✓ 1. Algorithmes de tri (Bubble, Insertion, Merge, Quick, Selection)")
    print("  ✓ 2. Structures de données (Stack, Queue, Heap)")
    print("  ✓ 3. Programmation dynamique (Fibonacci, Sac à dos, LCS)")
    print("  ✓ 4. Algorithmes gloutons (Monnaie, Activités, Sac à dos)")
    print("  ✓ 5. Compression Huffman")
    print()


if __name__ == "__main__":
    main()


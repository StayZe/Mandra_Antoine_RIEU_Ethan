import random
import time


def bubble(arr):
    """Tri à bulles"""
    arr_copy = arr.copy()
    n = len(arr_copy)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr_copy[j] > arr_copy[j+1]:
                arr_copy[j], arr_copy[j+1] = arr_copy[j+1], arr_copy[j]
    return arr_copy


def insertion(arr):
    """Tri par insertion"""
    arr_copy = arr.copy()
    n = len(arr_copy)
    for i in range(1, n):
        insert_index = i
        current_value = arr_copy.pop(i)
        for j in range(i-1, -1, -1):
            if arr_copy[j] > current_value:
                insert_index = j
        arr_copy.insert(insert_index, current_value)
    return arr_copy


def merge(arr):
    """Tri fusion"""
    def mergeSort(array):
        if len(array) <= 1:
            return array

        mid = len(array) // 2
        leftHalf = array[:mid]
        rightHalf = array[mid:]

        sortedLeft = mergeSort(leftHalf)
        sortedRight = mergeSort(rightHalf)

        return merge_combine(sortedLeft, sortedRight)

    def merge_combine(left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result

    return mergeSort(arr.copy())


def quick(arr):
    """Tri rapide"""
    arr_copy = arr.copy()
    
    def partition(array, low, high):
        pivot = array[high]
        i = low - 1

        for j in range(low, high):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]

        array[i+1], array[high] = array[high], array[i+1]
        return i+1

    def quicksort(array, low=0, high=None):
        if high is None:
            high = len(array) - 1

        if low < high:
            pivot_index = partition(array, low, high)
            quicksort(array, low, pivot_index-1)
            quicksort(array, pivot_index+1, high)

    quicksort(arr_copy)
    return arr_copy


def selection(arr):
    """Tri par sélection"""
    arr_copy = arr.copy()
    n = len(arr_copy)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr_copy[j] < arr_copy[min_index]:
                min_index = j
        min_value = arr_copy.pop(min_index)
        arr_copy.insert(i, min_value)
    return arr_copy


def main():
    """Fonction principale pour tester et benchmarker les algorithmes de tri"""
    
    print("=" * 80)
    print("BENCHMARK DES ALGORITHMES DE TRI")
    print("=" * 80)
    print()
    
    # Différentes tailles de listes pour le benchmark
    test_sizes = [100, 1000, 5000, 10000]
    
    for size in test_sizes:
        print(f"\n{'=' * 80}")
        print(f"TAILLE DE LA LISTE: {size} éléments")
        print(f"{'=' * 80}\n")
        
        # Générer une liste aléatoire
        test_list = [random.randint(0, 1000000) for _ in range(size)]
        
        # Afficher un échantillon de la liste non triée (premiers 10 éléments)
        print(f"Échantillon liste non triée (10 premiers): {test_list[:10]}\n")
        
        # Liste des algorithmes à tester
        algorithms = [
            ("Bubble Sort", bubble),
            ("Insertion Sort", insertion),
            ("Merge Sort", merge),
            ("Quick Sort", quick),
            ("Selection Sort", selection)
        ]
        
        results = []
        
        for name, func in algorithms:
            try:
                start_time = time.time()
                sorted_list = func(test_list)
                end_time = time.time()
                duration = end_time - start_time
                
                # Vérifier que la liste est bien triée
                is_sorted = all(sorted_list[i] <= sorted_list[i+1] for i in range(len(sorted_list)-1))
                
                results.append((name, duration, is_sorted))
                
                print(f"{name}:")
                print(f"  Temps d'exécution: {duration:.6f} secondes")
                print(f"  Statut: {'✓ Trié correctement' if is_sorted else '✗ ERREUR DE TRI'}")
                print(f"  Échantillon résultat (10 premiers): {sorted_list[:10]}\n")
                
            except Exception as e:
                print(f"{name}:")
                print(f"  ERREUR: {str(e)}\n")
        
        # Résumé des performances pour cette taille
        print(f"\n{'-' * 80}")
        print(f"RÉSUMÉ DES PERFORMANCES (Taille: {size})")
        print(f"{'-' * 80}")
        
        # Trier les résultats par temps d'exécution
        results.sort(key=lambda x: x[1])
        
        for i, (name, duration, is_sorted) in enumerate(results, 1):
            print(f"{i}. {name}: {duration:.6f}s")
        
        print()
    
    # Conclusion générale
    print(f"\n{'=' * 80}")
    print("ANALYSE COMPARATIVE")
    print(f"{'=' * 80}\n")
    print("Complexités temporelles:")
    print("  - Bubble Sort:    O(n²) moyen et pire cas")
    print("  - Insertion Sort: O(n²) moyen et pire cas, O(n) meilleur cas")
    print("  - Selection Sort: O(n²) dans tous les cas")
    print("  - Merge Sort:     O(n log n) dans tous les cas")
    print("  - Quick Sort:     O(n log n) moyen, O(n²) pire cas\n")
    print("Recommandations:")
    print("  - Pour petites listes: Insertion Sort")
    print("  - Pour grandes listes: Merge Sort ou Quick Sort")
    print("  - Pour stabilité garantie: Merge Sort")
    print("  - Pour économie de mémoire: Quick Sort (in-place)\n")


if __name__ == "__main__":
    main()


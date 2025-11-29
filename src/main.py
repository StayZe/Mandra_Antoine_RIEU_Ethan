import time
import sys


def code1_double_boucle(n):
    """Code 1 : Double boucle - O(n²)"""
    # Simulation d'un tableau n x n
    arr = [[i * n + j for j in range(n)] for i in range(n)]
    count = 0
    
    for i in range(n):
        for j in range(n):
            # Simule printf("%d", arr[i][j])
            count += 1
    
    return count


def code2_boucle_logarithmique(n):
    """Code 2 : Boucle logarithmique - O(log n)"""
    # Simulation d'un tableau
    arr = list(range(n))
    count = 0
    i = 1  # Commence à 1 car i *= 2 ne marche pas si i = 0
    
    while i < n:
        # Simule printf("%d", arr[i])
        count += 1
        i *= 2
    
    return count


def code3_recursion_logarithmique(n):
    """Code 3 : Récursion logarithmique - O(log n)"""
    count = 0
    
    def recursive(n):
        nonlocal count
        if n <= 1:
            return
        # Simule printf("%d", n)
        count += 1
        recursive(n // 2)
    
    recursive(n)
    return count


def test_complexity(func, n, func_name):
    """Teste une fonction et mesure le temps d'exécution"""
    try:
        start_time = time.time()
        operations = func(n)
        end_time = time.time()
        duration = end_time - start_time
        
        return {
            'name': func_name,
            'n': n,
            'operations': operations,
            'time': duration,
            'success': True
        }
    except Exception as e:
        return {
            'name': func_name,
            'n': n,
            'operations': 0,
            'time': 0,
            'success': False,
            'error': str(e)
        }


def main():
    """Fonction principale pour analyser la complexité"""
    
    output_file = "results/complexity_analysis.txt"
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("EXERCICE 1 : ANALYSE DE COMPLEXITE\n\n")
        
        # Définition des codes
        codes = [
            {
                'func': code1_double_boucle,
                'name': 'Code 1 : Double boucle',
                'code': """for(int i = 0; i < n; i++) {
    for(int j = 0; j < n; j++) {
        printf("%d", arr[i][j]);
    }
}""",
                'best': 'O(n²)',
                'average': 'O(n²)',
                'worst': 'O(n²)',
                'space': 'O(1)',
                'description': 'Deux boucles imbriquées'
            },
            {
                'func': code2_boucle_logarithmique,
                'name': 'Code 2 : Boucle logarithmique',
                'code': """for(int i = 1; i < n; i *= 2) {
    printf("%d", arr[i]);
}""",
                'best': 'O(log n)',
                'average': 'O(log n)',
                'worst': 'O(log n)',
                'space': 'O(1)',
                'description': 'i double à chaque itération'
            },
            {
                'func': code3_recursion_logarithmique,
                'name': 'Code 3 : Récursion logarithmique',
                'code': """void recursive(int n) {
    if(n <= 1) return;
    printf("%d", n);
    recursive(n/2);
}""",
                'best': 'O(log n)',
                'average': 'O(log n)',
                'worst': 'O(log n)',
                'space': 'O(log n)',
                'description': 'n divisé par 2 à chaque appel récursif'
            }
        ]
        
        # Question 1 : Complexité
        f.write("1. COMPLEXITE EN MEILLEUR/MOYEN/PIRE CAS\n\n")
        
        for code_info in codes:
            f.write(f"{code_info['name']}\n")
            f.write(f"{code_info['code']}\n\n")
            f.write(f"Meilleur cas : {code_info['best']}\n")
            f.write(f"Cas moyen : {code_info['average']}\n")
            f.write(f"Pire cas : {code_info['worst']}\n")
            f.write(f"Espace mémoire : {code_info['space']}\n")
            f.write(f"Explication : {code_info['description']}\n\n")
        
        # Question 2 : Impact pour n = 1 000 000
        f.write("\n2. IMPACT POUR n = 1 000 000\n\n")
        
        import math
        n_million = 1_000_000
        
        ops_code1 = n_million * n_million
        f.write(f"Code 1 (Double boucle)\n")
        f.write(f"Opérations : {ops_code1:,}\n")
        f.write(f"Temps estimé : environ {ops_code1 / 1e9:.0f} secondes\n")
        f.write(f"Conclusion : Impraticable\n\n")
        
        ops_code2 = math.floor(math.log2(n_million))
        f.write(f"Code 2 (Boucle logarithmique)\n")
        f.write(f"Opérations : {ops_code2}\n")
        f.write(f"Temps estimé : moins de 1 microseconde\n")
        f.write(f"Conclusion : Très rapide\n\n")
        
        ops_code3 = math.floor(math.log2(n_million))
        f.write(f"Code 3 (Récursion logarithmique)\n")
        f.write(f"Opérations : {ops_code3} appels récursifs\n")
        f.write(f"Temps estimé : moins de 1 microseconde\n")
        f.write(f"Conclusion : Très rapide\n\n")
        
        # Question 3 : Tests réels
        f.write("\n3. TEMPS D'EXECUTION REELS\n\n")
        
        test_sizes = [10, 100, 1000, 10000]
        
        print("Tests en cours...")
        
        for size in test_sizes:
            f.write(f"Tests avec n = {size:,}\n\n")
            
            print(f"Taille : n = {size:,}")
            
            for code_info in codes:
                if code_info['name'] == 'Code 1 : Double boucle' and size >= 10000:
                    f.write(f"{code_info['name']} : Test ignoré (trop lent)\n")
                    f.write(f"Opérations théoriques : {size * size:,}\n\n")
                    print(f"  {code_info['name']} : SKIPPED")
                    continue
                
                result = test_complexity(code_info['func'], size, code_info['name'])
                
                if result['success']:
                    f.write(f"{result['name']}\n")
                    f.write(f"Opérations : {result['operations']:,}\n")
                    f.write(f"Temps : {result['time']:.6f} secondes\n\n")
                    print(f"  {code_info['name']}: {result['time']:.6f}s")
                else:
                    f.write(f"{result['name']} : Erreur\n\n")
                    print(f"  {code_info['name']}: ERREUR")
        
        # Conclusion
        f.write("\nCONCLUSION\n\n")
        f.write("Pour n = 1 000 000 :\n")
        f.write("Code 1 est impraticable (1 trillion d'opérations)\n")
        f.write("Codes 2 et 3 sont très efficaces (environ 20 opérations)\n")
        f.write("Rapport : environ 50 milliards de fois plus rapide\n")
    
    print(f"\nAnalyse terminée")
    print(f"Résultats dans : {output_file}\n")


if __name__ == "__main__":
    main()


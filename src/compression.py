import heapq
import time
import os
import random
import string
from collections import Counter

class Node:
	def __init__(self, char=None, freq=0, left=None, right=None):
		self.char = char
		self.freq = freq
		self.left = left
		self.right = right

	def __lt__(self, other):
		return self.freq < other.freq

def build_huffman_tree(data):
	"""
	Construction de l'arbre Huffman en O(n log n)
	Complexité : O(n log n) où n est le nombre de caractères uniques
	"""
	freq_map = Counter(data)
	heap = [Node(char, freq) for char, freq in freq_map.items()]
	heapq.heapify(heap)  # O(n)

	while len(heap) > 1:  # O(n) itérations
		left = heapq.heappop(heap)  # O(log n)
		right = heapq.heappop(heap)  # O(log n)
		parent = Node(freq=left.freq + right.freq, left=left, right=right)
		heapq.heappush(heap, parent)  # O(log n)

	return heap[0] if heap else None

def build_huffman_codes(node, code="", codes=None):
	"""
	Génération des codes Huffman à partir de l'arbre
	Complexité : O(n) où n est le nombre de caractères uniques
	"""
	if codes is None:
		codes = {}
	if node.char is not None:
		codes[node.char] = code
	if node.left is not None:
		build_huffman_codes(node.left, code + "0", codes)
	if node.right is not None:
		build_huffman_codes(node.right, code + "1", codes)
	return codes

def compress_text(data):
	"""
	Compression de données avec Huffman
	Retourne le texte compressé (chaîne de bits) et les codes
	"""
	tree = build_huffman_tree(data)
	if tree is None:
		return "", {}
	codes = build_huffman_codes(tree)
	compressed_text = "".join(codes[char] for char in data)
	return compressed_text, codes

def decompress_text(compressed_text, codes):
	"""
	Décompression de données avec Huffman
	"""
	inverse_codes = {v: k for k, v in codes.items()}
	current_code = ""
	decompressed_text = ""
	for bit in compressed_text:
		current_code += bit
		if current_code in inverse_codes:
			decompressed_text += inverse_codes[current_code]
			current_code = ""
	return decompressed_text

def calculate_size_in_bits(text):
	"""Calcule la taille en bits d'un texte (8 bits par caractère)"""
	return len(text) * 8

def calculate_compressed_size(compressed_bits):
	"""Calcule la taille en bits du texte compressé"""
	return len(compressed_bits)

def test_compression(data, data_name, results_file):
	"""
	Teste la compression sur un type de données donné
	Mesure : taille originale, taille compressée, % compression, temps d'exécution
	"""
	print(f"\n{'='*60}")
	print(f"Test sur : {data_name}")
	print(f"{'='*60}")
	
	# Mesure de la taille originale
	original_size_bits = calculate_size_in_bits(data)
	original_size_bytes = len(data)
	
	# Compression avec mesure du temps
	start_time = time.time()
	compressed_text, codes = compress_text(data)
	compression_time = time.time() - start_time
	
	# Mesure de la taille compressée
	compressed_size_bits = calculate_compressed_size(compressed_text)
	compressed_size_bytes = (compressed_size_bits + 7) // 8  # Arrondi supérieur
	
	# Calcul du pourcentage de compression
	compression_ratio = (1 - compressed_size_bits / original_size_bits) * 100 if original_size_bits > 0 else 0
	
	# Décompression avec mesure du temps
	start_time = time.time()
	decompressed_text = decompress_text(compressed_text, codes)
	decompression_time = time.time() - start_time
	
	# Vérification de l'intégrité
	is_correct = decompressed_text == data
	
	# Affichage des résultats
	print(f"Taille originale : {original_size_bytes} octets ({original_size_bits} bits)")
	print(f"Taille compressée : {compressed_size_bytes} octets ({compressed_size_bits} bits)")
	print(f"Taux de compression : {compression_ratio:.2f}%")
	print(f"Temps de compression : {compression_time:.6f} s")
	print(f"Temps de décompression : {decompression_time:.6f} s")
	print(f"Temps total : {compression_time + decompression_time:.6f} s")
	print(f"Intégrité : {'✓ OK' if is_correct else '✗ ERREUR'}")
	
	# Écriture dans le fichier de résultats
	results_file.write(f"\n{'='*60}\n")
	results_file.write(f"Test sur : {data_name}\n")
	results_file.write(f"{'='*60}\n")
	results_file.write(f"Taille originale : {original_size_bytes} octets ({original_size_bits} bits)\n")
	results_file.write(f"Taille compressée : {compressed_size_bytes} octets ({compressed_size_bits} bits)\n")
	results_file.write(f"Taux de compression : {compression_ratio:.2f}%\n")
	results_file.write(f"Temps de compression : {compression_time:.6f} s\n")
	results_file.write(f"Temps de décompression : {decompression_time:.6f} s\n")
	results_file.write(f"Temps total : {compression_time + decompression_time:.6f} s\n")
	results_file.write(f"Intégrité : {'✓ OK' if is_correct else '✗ ERREUR'}\n")
	
	return {
		'original_size': original_size_bytes,
		'compressed_size': compressed_size_bytes,
		'compression_ratio': compression_ratio,
		'compression_time': compression_time,
		'decompression_time': decompression_time,
		'is_correct': is_correct
	}

def compression_main():
	"""
	Fonction principale pour tester la compression Huffman
	Teste sur : texte anglais, fichier binaire, données aléatoires
	"""
	results_path = "results/compression_analysis.txt"
	
	with open(results_path, 'w', encoding='utf-8') as results_file:
		results_file.write("Exercice 6 - Compression Huffman\n")
		results_file.write("="*60 + "\n")
		
		# 1. Test sur texte anglais
		english_text = """
		The quick brown fox jumps over the lazy dog. This is a classic pangram 
		that contains every letter of the English alphabet at least once. 
		Compression algorithms work by identifying patterns and redundancies 
		in data. Huffman coding is a lossless data compression algorithm that 
		assigns variable-length codes to characters based on their frequency 
		of occurrence. More frequent characters get shorter codes, while less 
		frequent characters get longer codes. This results in efficient 
		compression for text data with varying character frequencies.
		"""
		test_compression(english_text, "Texte anglais", results_file)
		
		# 2. Test sur fichier binaire (simulation avec des bytes aléatoires)
		# Pour les données binaires, on traite chaque byte comme un caractère
		binary_data = bytes([random.randint(0, 255) for _ in range(1000)])
		# Convertir en chaîne pour le traitement (chaque byte devient un caractère)
		binary_str = ''.join(chr(b) for b in binary_data)
		test_compression(binary_str, "Fichier binaire (1000 bytes)", results_file)
		
		# 3. Test sur données aléatoires
		random_data = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=2000))
		test_compression(random_data, "Données aléatoires (2000 caractères)", results_file)
		
		# 4. Test sur texte avec répétitions (meilleur cas pour Huffman)
		repetitive_text = "AAAAA" * 100 + "BBBB" * 50 + "CCC" * 30 + "DD" * 20 + "E" * 10
		test_compression(repetitive_text, "Texte avec répétitions", results_file)
		
		# 5. Test sur texte court
		short_text = "hello world"
		test_compression(short_text, "Texte court", results_file)
		
		results_file.write(f"\n{'='*60}\n")
		results_file.write("Analyse de complexité :\n")
		results_file.write("- Construction arbre : O(n log n) où n = nombre de caractères uniques\n")
		results_file.write("- Génération codes : O(n)\n")
		results_file.write("- Compression : O(m) où m = longueur du texte\n")
		results_file.write("- Décompression : O(m)\n")
		results_file.write(f"{'='*60}\n")
	
	print(f"\n{'='*60}")
	print("Résultats sauvegardés dans :", results_path)
	print(f"{'='*60}\n")

if __name__ == "__main__":
	compression_main()
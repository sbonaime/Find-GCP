import sys
from collections import Counter

def filter_file(input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Extraire l'en-tête et les données
    header = lines[0]
    data_lines = lines[1:]
    
    # Construire un dictionnaire pour compter les occurrences des index
    index_counts = Counter(line.split()[6] for line in data_lines)
    
    # Filtrer les lignes
    filtered_lines = [line for line in data_lines if index_counts[line.split()[6]] > 2]
    
    # Réécriture du fichier avec les lignes filtrées
    with open(input_file, 'w', encoding='utf-8') as f:
        f.write(header)
        f.writelines(filtered_lines)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file>", file=sys.stderr)
        sys.exit(1)
    
    input_file = sys.argv[1]
    filter_file(input_file)

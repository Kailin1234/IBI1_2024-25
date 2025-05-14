# Input files
def read_fasta(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
        seq = ''.join([line.strip() for line in lines if not line.startswith('>')])
    return seq

seq1 = read_fasta('P04179.fasta') 
seq2 = read_fasta('P09671.fasta') 
seq3 = read_fasta('random.fasta')

# Calculate the edit distance
def edit_distance(seqA, seqB):
    distance = 0
    for i in range(len(seqA)):
        if seqA[i] != seqB[i]:
            distance += 1
    return distance

# Input BLOSUM file
def blosum_matrix(file_path):
    blosum_dict = {}
    with open(file_path, "r") as file:
        lines = file.readlines()[6:] # Read all lines from the file
        headers = lines[0].strip().split() # Split the first line into headers, and every AA will be split as an individual string and stored in a list
        for line in lines [1:]: # Iterate through the rest of the lines
            row = line.strip().split() # Split each line into a list of strings
            amino_acid = row[0] # The first element is the amino acid
            scores = list(map(int, row[1:])) # Convert the rest of the elements from strings to integers
            for i, header in enumerate(headers): # Iterate through the headers, and return the index and the header
                blosum_dict[(amino_acid, header)] = scores[i] # Create a dictionary with tuples of amino acids as keys and their corresponding scores using relative indices
                blosum_dict[(header, amino_acid)] = scores[i] # Create a symmetric dictionary for the BLOSUM matrix
    return blosum_dict

blosum = blosum_matrix("BLOSUM62.txt")

# Compare two amino acid sequences
def compare_sequences(seqA, seqB):
    paired = list(zip(seqA, seqB))
    total_score = 0
    edit_distance =	0
    for pair in paired:
        score = blosum.get(pair, -4) # Get the score from the BLOSUM matrix
        total_score += score # Add the score to the total score
    identical = sum(1 for a, b in paired if a == b)
    identity_percent = (identical / len(paired)) * 100 # Calculate the percentage of identical amino acids 
    return total_score, identity_percent

# Calculate the score and identity percentage
choice = input("Which sequences do you want to compare?(human-mouse/human-random/mouse-random): ")
if choice == "human-mouse":
    distance = edit_distance(seq1, seq2)
    total_score, identity_percent = compare_sequences(seq1, seq2)
elif choice == "human-random":
    distance = edit_distance(seq1, seq3)
    total_score, identity_percent = compare_sequences(seq1, seq3)
elif choice == "mouse-random":
    distance = edit_distance(seq2, seq3)
    total_score, identity_percent = compare_sequences(seq2, seq3)
print(f"Edit distance: {distance}")
print(f"Total score: {total_score}")
print(f"Identity percentage: {identity_percent:.2f}%") # .2f means 2 decimal places, add % sign
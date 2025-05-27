# 1.Processing the targeted file through skipping the header lines
def read_fasta(filepath): # Function to read a FASTA file and return the sequence as a string
    with open(filepath, 'r') as f: # Open the file in read mode
        lines = f.readlines() # Read all lines
        seq = ''.join([line.strip() for line in lines if not line.startswith('>')]) # Join all lines into a single string besides the header lines
    return seq # Return the sequence string

# 2.Reading the sequences from the FASTA files (human, mouse, and random)
seq1 = read_fasta('P04179.fasta') # Read the human sequence
seq2 = read_fasta('P09671.fasta') # Read the mouse sequence
seq3 = read_fasta('random.fasta') # Read the random sequence

# 3.Defining a definition to calculate the edit distance 
def edit_distance(seqA, seqB): # The input parameters are two sequences
    distance = 0 # Initialize the distance to 0
    for i in range(len(seqA)): # Iterate through the length of the sequences
        if seqA[i] != seqB[i]: # If the characters at the same position are not equal
            distance += 1 # Increment the distance by 1
    return distance # Return the final edit distance

# 4.Inputing BLOSUM file and creating a dictionary to store the BLOSUM scores
def blosum_matrix(file_path): # Function to read a BLOSUM matrix file and return a dictionary of scores
    blosum_dict = {} # Initialize an empty dictionary to store the BLOSUM scores
    with open(file_path, "r") as file: # Open the BLOSUM file in read mode
        lines = file.readlines()[6:] # Read all lines from the file
        headers = lines[0].strip().split() # Split the first line into headers, and every AA will be split as an individual string and stored in a list
        for line in lines [1:]: # Iterate through the rest of the lines
            row = line.strip().split() # Split each line into a list of strings
            amino_acid = row[0] # The first element is the amino acid
            scores = list(map(int, row[1:])) # Convert the rest of the elements from strings to integers
            for i, header in enumerate(headers): # Iterate through the headers, and return the index and the header
                blosum_dict[(amino_acid, header)] = scores[i] # Create a dictionary with tuples of amino acids as keys and their corresponding scores using relative indices
                blosum_dict[(header, amino_acid)] = scores[i] # Create a symmetric dictionary for the BLOSUM matrix
    return blosum_dict # Return the BLOSUM dictionary
blosum = blosum_matrix("BLOSUM62.txt") # Read the BLOSUM matrix file

# 5.Comparing two amino acid sequences
def compare_sequences(seqA, seqB): # Define a function to compare two sequences
    paired = list(zip(seqA, seqB)) # Pair the sequences together, creating a list of tuples where each tuple contains one amino acid from each sequence
    total_score = 0 # Initialize the total score to 0
    edit_distance =	0 # Initialize the edit distance to 0
    for pair in paired: # Iterate through the paired sequences
        score = blosum.get(pair, -4) # Get the score from the BLOSUM matrix
        total_score += score # Add the score to the total score
    identical = sum(1 for a, b in paired if a == b) # Count the number of identical amino acids in the paired sequences
    identity_percent = (identical / len(paired)) * 100 # Calculate the percentage of identical amino acids 
    return total_score, identity_percent # Return the total score and identity percentage

# 6.Calculating the score and identity percentage
distance1 = edit_distance(seq1, seq2) # Calculate the edit distance between human and mouse sequences
total_score1, identity_percent1 = compare_sequences(seq1, seq2) # Compare the human and mouse sequences
distance2 = edit_distance(seq1, seq3) # Calculate the edit distance between human and random sequences
total_score2, identity_percent2 = compare_sequences(seq1, seq3) # Compare the human and random sequences
distance3 = edit_distance(seq2, seq3) # Calculate the edit distance between mouse and random sequences
total_score3, identity_percent3 = compare_sequences(seq2, seq3) # Compare the mouse and random sequences
print(f"Human-Mouse: edit distance: {distance1}, total score: {total_score1}, identity percent: {identity_percent1:.2f}%") # Output the results for human and mouse sequences
print(f"Human-Random: edit distance: {distance2}, total score: {total_score2}, identity percent: {identity_percent2:.2f}%") # Output the results for human and random sequences
print(f"Mouse-Random: edit distance: {distance3}, total score: {total_score3}, identity percent: {identity_percent3:.2f}%") # Output the results for mouse and random sequences
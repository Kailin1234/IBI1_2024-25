# 1.Import the necessary library.
# 2.Open the input file and output files.
# 3.Define a function to splice TATA genes.
# 4.Check the donor and acceptor sequence and set the output file accordingly.
# 5.Check if the line is a header line and handle the gene name and sequence accordingly.
# 6.Search for the donor and acceptor sequence and find all occurrences of the TATA box in the gene sequence and count them.
# 7.Write the output file.

import re # Import the re library to use regular expression

input_file = open(r'c:\cygwin64\home\kaili\IBI1_2024-25\IBI1_2024-25\Practical7\tata_genes.fa', 'r') # Open the input file containing gene sequences
output1 = open(r'c:\cygwin64\home\kaili\IBI1_2024-25\IBI1_2024-25\Practical7\GTAG_spliced_genes.fa', 'w') # Open the output file for GTAG spliced genes
output2 = open(r'c:\cygwin64\home\kaili\IBI1_2024-25\IBI1_2024-25\Practical7\GCAG_spliced_genes.fa', 'w') # Open the output file for GCAG spliced genes
output3 = open(r'c:\cygwin64\home\kaili\IBI1_2024-25\IBI1_2024-25\Practical7\ATAC_spliced_genes.fa', 'w') # Open the output file for ATAC spliced genes

def spliced_tata_genes(input_file, donor_acceptor): # Define a function to splice TATA genes based on donor and acceptor sequences
    gene_name = "" # Initialize an empty string to store the current gene name
    gene_sequence = "" # Initialize an empty string to store the current gene sequence
    if donor_acceptor == "GT.+AG": # Check the donor and acceptor sequence
        output = output1 # Set the output file for GTAG spliced genes
    elif donor_acceptor == "GC.+AG": # Check the donor and acceptor sequence
        output = output2 # Set the output file for GCAG spliced genes
    elif donor_acceptor == "AT.+AC": # Check the donor and acceptor sequence
        output = output3 # Set the output file for ATAC spliced genes
    for line in input_file: # Iterate through each line in the input file
        if re.search('^>', line): # Check if the line starts with '>', which is the header line
            if gene_name and re.search(donor_acceptor, gene_sequence): # Search for the donor and acceptor sequence in the gene sequence
                seg = re.findall("TATA[AT]A[AT]", gene_sequence) # Find all occurrences of the TATA box in the gene sequence
                amount = len(seg[:]) # Count the number of TATA boxes found
                output.write(f">{gene_name} {amount}\n{gene_sequence}\n") # Write the gene name, number of TATA boxes, and gene sequence to the output file
            gene_name = line.strip()[1:] # Extract the gene name from the header line, removing the '>' to prevent repetition
            gene_sequence = "" # Reset the gene sequence for the new gene
        else: # If the line is not a header line, it contains part of the gene sequence
            gene_sequence += line.strip() # Append the line to the current gene sequence

    if gene_name and re.search(donor_acceptor, gene_sequence): # Check if the last gene sequence contains the donor and acceptor sequence
        output.write(f">{gene_name} {amount}\n{gene_sequence}\n") # Write the last gene name, number of TATA boxes, and gene sequence to the output file

donor_acceptor = input("Enter the donor and acceptor sequence (GT.+AG, GC.+AG or AT.+AC): ") # Let the user input the donor and acceptor sequence
spliced_tata_genes(input_file, donor_acceptor) # Call the function to splice TATA genes based on the user input
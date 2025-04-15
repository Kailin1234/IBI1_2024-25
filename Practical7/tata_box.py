import re

input = open(r'c:\cygwin64\home\kaili\IBI1_2024-25\IBI1_2024-25\Practical7\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
output = open(r"c:\cygwin64\home\kaili\IBI1_2024-25\IBI1_2024-25\Practical7\tata_genes.fa", 'w')
gene_name = ""
gene_sequence = ""

# 读第二行时写了第一行
for line in input:
    if re.search('^>', line):
        if gene_name and re.search("TATA[AT]A[AT]", gene_sequence):
                output.write(f">{gene_name}\n{gene_sequence}\n")
        gene_name = line.strip().split(' ')[0].split('_')[0]
        gene_sequence = ""
    else:
        gene_sequence += line.strip()

if gene_name and re.search("TATA(T|A)A(T|A)", gene_sequence):
    output.write(f">{gene_name}\n{gene_sequence}\n")
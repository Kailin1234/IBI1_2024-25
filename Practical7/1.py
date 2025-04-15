import re

input = open(r'c:\cygwin64\home\kaili\IBI1_2024-25\IBI1_2024-25\Practical7\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
output1 = open(r'c:\cygwin64\home\kaili\IBI1_2024-25\IBI1_2024-25\Practical7\GTAG_spliced_genes.fa', 'w')
output2 = open(r'c:\cygwin64\home\kaili\IBI1_2024-25\IBI1_2024-25\Practical7\GCAG_spliced_genes.fa', 'w')
output3 = open(r'c:\cygwin64\home\kaili\IBI1_2024-25\IBI1_2024-25\Practical7\ATAC_spliced_genes.fa', 'w')
gene_name1 = ""
gene_name2 = ""
gene_name3 = ""
gene_sequence1 = ""
gene_sequence2 = ""
gene_sequence3 = ""
gene_name = []
gene_sequence = []
tata_box = ""

for line in input:
    if re.search('^>', line):
        if gene_name and re.search("TATA[AT]A[AT]", gene_sequence):
                tata_box += f">{gene_name}\n{gene_sequence}\n"
        gene_name = line.strip().split(' ')[0].split('_')[0]
        gene_sequence = ""
    else:
        gene_sequence += line.strip()

if gene_name and re.search("TATA(T|A)A(T|A)", gene_sequence):
    tata_box += f">{gene_name}\n{gene_sequence}\n"

for line in tata_box:
    if re.search('^>', line):
        if gene_name1 and re.search("GT.+AG", gene_sequence1):
            seg1 = re.findall("TATA[AT]A[AT]", gene_sequence1)
            number1 = len(seg1[:])
            output1.write(f">{gene_name1} {number1}\n{gene_sequence1}\n")
        gene_name1 = line.strip()
        gene_sequence1 = ""
    else:
        gene_sequence1 = line.strip()


if gene_name1 and re.search("GT.+AG", gene_sequence1):
    output1.write(f">{gene_name1} {number1}\n{gene_sequence1}\n")



for line in tata_box:
    if re.search('^>', line):
        if gene_name2 and re.search("GC.+AG", gene_sequence2):
            seg2 = re.findall("TATA[AT]A[AT]", gene_sequence2)
            number2 = len(seg2[:])
            output2.write(f">{gene_name2} {number2}\n{gene_sequence2}\n")
        gene_name2 = line.strip()
        gene_sequence2 = ""
    else:
        gene_sequence2 = line.strip()


if gene_name2 and re.search("GC.+AG", gene_sequence2):
    output2.write(f">{gene_name2} {number2}\n{gene_sequence2}\n")



for line in tata_box:
    if re.search('^>', line):
        if gene_name3 and re.search("AT.+AC", gene_sequence3):
            seg3 = re.findall("TATA[AT]A[AT]", gene_sequence3)
            number3 = len(seg3[:])
            output3.write(f">{gene_name3} {number3}\n{gene_sequence3}\n")
        gene_name3 = line.strip()
        gene_sequence3 = ""
    else:
        gene_sequence3 = line.strip()


if gene_name3 and re.search("AT.+AC", gene_sequence3):
    output3.write(f">{gene_name3} {number3}\n{gene_sequence3}\n")

output1.close()
output2.close()
output3.close()
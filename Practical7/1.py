import re

file_handle = open(r'c:\cygwin64\home\kaili\IBI1_2024-25\IBI1_2024-25\Practical7\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
processed_line = []
for line in file_handle:
    if re.search('^>', line):
        processed_line.append('\n')
        if re.search(r'_mRNA', line):
            line = re.sub(r'_mRNA''.+?\n', '', line)
        if re.search(r'cdna', line):
            line = re.sub('cdna''.+?\n', '', line)
    line = line.strip()
    processed_line.append(line)

result = " ".join(processed_line)
output = open(r"c:\cygwin64\home\kaili\IBI1_2024-25\IBI1_2024-25\Practical7\output.fa", 'w')
for line in result:
    output.write(line)
output.close()

objective_line = []
process = open(r"c:\cygwin64\home\kaili\IBI1_2024-25\IBI1_2024-25\Practical7\output.fa", 'r')
for line in process:
    if re.search(r'TATA(T|A)A(T|A)', line):
        line = re.sub(' ', '\n', line)
        line = line.rstrip()
        objective_line.append(line)

output = open(r"c:\cygwin64\home\kaili\IBI1_2024-25\IBI1_2024-25\Practical7\tata_genes.fa", 'w')
for line in objective_line:
    output.write(line)
output.close()
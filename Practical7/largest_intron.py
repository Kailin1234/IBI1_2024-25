import re
seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
largest_intron = re.findall(r'GT.+AG', seq)
print(largest_intron)
lenth = len(largest_intron[0])
print(lenth)
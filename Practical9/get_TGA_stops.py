import re
seq = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
new_file = open('TGA_genes.fa', 'w')
a = seq.read()
b = a.split('>')  # Split the sequence of each gene
k = 0
for i in b:
    if re.findall(r'TGA\n$', i):  # Find the sequence that ends in TGA
        c = re.sub(r'\n', '', b[k])  # Remove all newlines
        new_file.write('>' + ''.join(re.findall(r' gene:(.+?) ', c)) + '\n' + ''.join(re.findall(r'](.+)', c)) + '\n')  # Put the the name and the sequence
    k += 1  # Record the serial number in the list

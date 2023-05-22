import re
Input = input('Please input TAA, TAG and TGA as the stop codon: ')
seq = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
new_file = open('%s_stop_genes.fa' % Input, 'w')  # make a file including input
a = seq.read()
b = a.split('>')  # Split the sequence of each gene
k = 0
for i in b:
    if re.findall(Input+r'\n$', i):  # Find the sequence that ends in the Input and newlines
        c = re.sub(r'\n', '', b[k])  # Remove all newlines
        new_file.write('>' + ''.join(re.findall(r' gene:(.+?) ', c)) + ' ' + str(len(re.findall(Input, c))) + '\n' + ''.join(re.findall(r'](.+)', c)) + '\n')
        # the number of coding sequences which could	be generated using the given stop codon
    k += 1  # Record the serial number in the list

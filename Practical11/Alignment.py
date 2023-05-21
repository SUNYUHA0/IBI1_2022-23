import blosum as bl
matrix = bl.BLOSUM(62)

'''
Extract the sequence of amino acids
'''
def seq(name):
   k = ""
   f = open(name, 'r')
   for i in f:
       k = i[:-1]
   return k
cat = seq('ACE2_cat.fa')
human = seq('ACE2_human.fa')
mouse = seq('ACE2_mouse.fa')

'''
Use blosum to figure out the scores
'''
def scores(name1, name2):
    v = 0
    for	i in range(len(name1)):
        v += matrix[name1[i]][name2[i]]
    return v

'''
Calculate the ratio of the same amino acids
'''
def percentage(name1, name2):
    n = 0
    for	i in range(len(name1)):
        if name1[i] == name2[i]:
            n += 1
    return n

'''
Extract the title of each amino acid
'''
def output(fname1, fname2):
    a = open(fname1)
    a = a.read()
    b = open(fname2)
    b = b.read()
    return a + '\n' + b

print(output('ACE2_cat.fa', 'ACE2_human.fa') + '\n' + 'scores =' + ' ' + str(scores(cat, human)) + '\n' + 'percentage =' + ' ' + str(percentage(cat, human)/len(cat)))
print(output('ACE2_cat.fa', 'ACE2_mouse.fa') + '\n' + 'scores =' + ' ' + str(scores(cat, mouse)) + '\n' + 'percentage =' + ' ' + str(percentage(cat, mouse)/len(cat)))
print(output('ACE2_mouse.fa', 'ACE2_human.fa') + '\n' + 'scores =' + ' ' + str(scores(mouse, human)) + '\n' + 'percentage =' + ' ' + str(percentage(mouse, human)/len(human)))

'''
The differences in amino acid sequences between cats and mice were minimal.
1. a high score means that there are many substitutions between the two sequences, suggesting that they diverged over a long period of evolutionary time and may only share a relatively distant common ancestor. 
2. the proteins may have different functions. There are many substitutions, many of which are non-conserved, and these sequences may have diverged to the extent that their structures and functions are completely different. They may share some small conserved regions but, in general, play different roles. 
3. Some positions are conserved, indicating evolutionary constraints. In order to score positively, there must be some conserved or semi-conserved substitutions and conserved regions. These positions may encode functionally or structurally important sites that remain similar even if the sequence diverges in other ways.
'''







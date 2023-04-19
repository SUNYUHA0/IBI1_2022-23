'''
Calculate the percentage and define the name
'''
import re
def calculator (seq):
    seq = seq.upper()  # Convert lowercase to uppercase
    a = re.findall(r'^ATG.+?TGA', seq)  # Take all sequences from the beginning of ATG to the end of TGA
    b = len(a[0]) / len(seq)  # Calculated percentage
    if b > 0.5:
        return str('percent: {:.2%}'.format(b)) + ' ' + 'protein-coding'
    elif b < 0.1:
        return str('percent: {:.2%}'.format(b)) + ' ' + 'non-coding'
    else: str('percent: {:.2%}'.format(b)) + ' ' + 'unclear'
    
seq = 'ATGTGCACATtgagtaaac'
z = calculator(seq)
print(calculator(seq))
'''
Calculate the percentage and define the name
'''
import re
def calculator(seq):
    seq = seq.upper()  # Convert lowercase to uppercase
    a = re.findall(r'ATG.+?TGA', seq)  # Take all sequences from the beginning of ATG to the end of TGA
    b = (len(a[0]) - 3) / len(seq)  # Since the stop codon does not encode an amino acid, the total length needs to be subtracted from the length of the stop codon, 3. Then calculate the percentage..
    if b > 0.5:
        return str('percent: {:.2%}'.format(b)) + ' ' + 'protein-coding'
    elif b < 0.1:
        return str('percent: {:.2%}'.format(b)) + ' ' + 'non-coding'
    else:
        return str('percent: {:.2%}'.format(b)) + ' ' + 'unclear'
    
    
seq = input("Please input a DNA sequence:")
z = calculator(seq)
print(calculator(seq))
  # seq = 'ATGTGCAtgagtaaacattg'. And the output is 'percent: 35.00% unclear'.
  # seq = 'AAAAAAAATTTTTTATGCCCCGGGGGAAATTTTTGAAAAAAA'. And the output is 'percent: 45.24% unclear'.
  # seq = 'TTGATGCCGTCTGGCTGATTT'. And the outpot is 'percent: 57.14% protein-coding'.

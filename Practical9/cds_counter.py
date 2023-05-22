import re
seq = 'ATGCAATCGACTACGATCTGAGAGGGCCTAA'
x = re.findall(r'^ATG.+', seq)  # Find the first sequence in which "ATG" appears
y = "".join(x)  # change the list into string.
a = y.count('TGA')
b = y.count('TAA')
c = a + b
print("Total number of possible coding sequences is", c)  # Print the total	number of possible coding sequences	formed	by this sequence.

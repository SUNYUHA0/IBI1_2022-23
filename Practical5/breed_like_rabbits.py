'''
When the number of rabbits is less than 100, double the number and add the number of generations until the number of rabbits is greater than one hundred
'''
x = 2  # the number of rabbits in first generation
y = 1  # the first generation
while x < 100: # When the total number of rabbits is less than 100
 y += 1  # the number of generation plus 1
 x = 2*x  # Double the number of ducks
if x > 100:When the total number of rabbits is greater than 100
 print(y)  # output result. At 7 generation over 100 rabbits have been born.

# What does this piece of code do?
# Answer:

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0
stored_random_number=0
while progress<10:
	progress+=1 #The cycle time is ten times
	n = randint(1,100) #Pick a random number between 1 and 100
	if n > stored_random_number:
		stored_random_number = n #If n is large, then n is chosen

print(stored_random_number)

a = -3.19 # longitude of Edinburgh
b = -118.24 #longitude of Los Angeles
c = 116.39 #longitude of Haining
d = a - b #longitude distance between Edinburgh and Los Angeles
e = c - a #longitude distance between Edinburgh and Haining
if d > e:
 print("Los Angeles") #if longitude distance between Edinburgh and Los Angeles larger than longitude distance between Edinburgh and Haining. Then print Los Angeles
elif d < e:
 print("Haining") #if longitude distance between Edinburgh and Los Angeles is smaller than longitude distance between Edinburgh and Haining. Then print Haining
else:
 print("the distance is equal") #if the differences are equal then print this.
# the answer is Haining.

X = True
Y = False
W = X and Y
Z = X or Y
print(W)
print(Z)
# W is False and Z is Ture.

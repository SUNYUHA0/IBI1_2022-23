import matplotlib.pyplot as plt
import numpy as np # import matplotlib.pyplot and numpy
countries = ['Los_Angeles_1984', 'Seoul_1988', 'Barcelona_1992', 'Atlanta_1996', 'Sydney_2000', 'Athens_2003', 'Beijing_2008', 'London_2012']
costs = [1, 8, 15, 7, 5, 14, 43, 40]
N = 8
new = sorted(costs)  # the sorted list of costs
print(new) # Arrange the data from largest to smallest and call it new
ind = np.arange(N) # make array from 0 to 7
p = plt.bar(ind, costs, 0.4)
plt.ylabel('cost') # name the y-axis
plt.title('olmpic costs') # name the title
plt.xticks(ind, np.array(countries), fontsize = 5)
plt.yticks(np.arange(0, 45, 5)) # Set the maximum value of the Y-axis to 45, and each small square to 5
plt.show()

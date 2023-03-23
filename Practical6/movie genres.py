import matplotlib.pyplot as plt #import matplotlib.pyplot into python
'''
store and export the data as a dictionary
'''
g = {'Comedy': 73, 'Action': 42, 'Romance': 38, 'Fantasy': 28, 'Science-fiction': 22, 'Horror': 19, 'Crime': 18, 'Documentary': 12, 'History': 8, 'War': 7}
print(g)
values = list(g.values())
keys = list(g.keys()) #I draw this with the help of matplotlib official doc and my friends
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pie.html
plt.pie(values, labels=keys, autopct='%.2f%%' ) #creat a pie chart
plt.show()
'''
assume 'Horror' is input and the '19' is output
'''
Input = 'Horror'
print(g[Input])

import os
import pandas as pd
import matplotlib.pyplot as plt

os.chdir ("D:\github\IBI1_2022-23\Practical7")  # Chage the dirctory

'''
print(os.getcwd())  # View my directory
print(os.listdir())  # See what's in my dirtory
'''

covid_data = pd.read_csv("full_data.csv")  # Read the content of the full_data.csv file into a dataframe object

'''
print(covid_data.head(5))  # Read the first five rows of the file.
print(covid_data.info())  # The data type is int64(4), object(2). The columns are called date, location,  new_cases, new_deaths, total_cases, total_deaths. There are 7996 rows.
print(covid_data.describe())  # The means are 194.546773, 9.322661, 2441.369060, 97.977239. The standard deviations are 2083.395028, 108.183439, 22375.617031, 1023.038977. The minimums are -9.000000, 0.000000, 0.000000, 0.000000. The maximums are 65162.000000, 3698.000000, 777798.000000, 37272.000000.
print(covid_data.iloc[0, 1])  # Check out the  what’s in the first row, second column
print(covid_data.head(1))  #  Verify from looking back at the “head” command
print(covid_data.iloc[2, 0:5])  # Check out the first five columns of the third row
print(covid_data.iloc[0:2, :])  # Check out all of the column content in one to three rows
print(covid_data.iloc[0:10:2, 0:5])  # Check out the first five columns from every second row from the first 10 rows
'''

print((covid_data.iloc[0:1001:100, 1])) # Check out the second column from every 100th row from the first 1000 rows

'''
print(covid_data.iloc[0:3, [0, 1, 3]])  # To see the first three rows, but only the first, second, and fourth column.

my_columns = [True, True, False, True, False, False]
print(covid_data.iloc[0:3, my_columns])  # To see the first three rows, but only the first, second, and fourth column using Booleans.
my_columns = [True, True, False, True, False, False, Ture]
print(covid_data.iloc[0:3, my_columns])  # my_columns is longer than the number of columns of your data frame: name 'Ture' is not defined
my_columns = [True, True, False, True, False]
print(covid_data.iloc[0:3, my_columns])  # my_columns is shorter than the number of columns of your data frame: Boolean index has wrong length: 5 instead of 6

print(covid_data.loc[2:4, "date"])  # Check out the three to five rows of the "date" column
'''

my_rows = []
for i in covid_data.loc[:, "location"]:
    if i == "Afghanistan":
        my_rows.append(True) 
    else:
        my_rows.append(False) 
print(covid_data.loc[my_rows, "total_cases"])  # Check out all total cases in Afghanistan


row_1 = []
for i in covid_data.loc[:, "date"]:
    if i == "2020-03-31":
        row_1.append(True)
    else:
        row_1.append(False)
new_data = covid_data.loc[row_1, ["location", "new_cases", "new_deaths"]]  # Create a new_data where the date is “2020-03-31”, and in three columns “location”, “new cases” and “new deaths
print(new_data.describe())  # The mean of new_cases and new_deaths are 640.461538 and 37.928205


total_new_deaths = sum(covid_data.loc[row_1, "new_deaths"])  # The sum of new deaths
total_new_cases = sum(covid_data.loc[row_1, "new_cases"])  # The sum of new casaes
proportion = total_new_deaths/total_new_cases
print(proportion)  # The proportion of new deaths as a proportion of the new cases on 31 March


new_cases = covid_data.loc[row_1, "new_cases"]
plt.title('The new cases for the whole world on March 31st 2020')
plt.boxplot(new_cases, 
            vert = True, 
            whis = 1.5, 
            patch_artist = True, 
            meanline = False, 
            showbox = True, 
            showcaps = True,
            showfliers = True,
            notch = False
            )
plt.show()

new_deaths = covid_data.loc[row_1, "new_deaths"]
plt.title('The new deaths for the whole world on March 31st 2020')
plt.boxplot(new_deaths, 
            vert = True, 
            whis = 1.5, 
            patch_artist = True, 
            meanline = False, 
            showbox = True, 
            showcaps = True,
            showfliers = True,
            notch = False
            )
plt.show()  # Plot the new cases and new deaths on 31 March as two separate box plots


'''
world_dates = covid_data.loc[:, "date"]
world_new_cases = covid_data.loc[:, "new_cases"]
plt.plot(world_dates, world_new_cases, 'b+')
plt.show()  # Plot the data for the whole world over time and it has bule +

world_dates = covid_data.loc[:, "date"]
world_new_cases = covid_data.loc[:, "new_cases"]
plt.plot(world_dates, world_new_cases, 'r+')
plt.show()  # Plot the data for the whole world over time and it has red +

world_dates = covid_data.loc[:, "date"]
world_new_cases = covid_data.loc[:, "new_cases"]
plt.plot(world_dates, world_new_cases, 'bo')
plt.show()  # Plot the data for the whole world over time and it has bule o

world_new_deaths = covid_data.loc[:, "new_deaths"]
plt.plot(world_dates, world_new_cases, 'ro')
plt.plot(world_dates, world_new_cases, 'b+')
plt.show()  # Compare new cases and new deaths across the world. Plot new cases in one colour and new deaths in another colour.

world_new_deaths = covid_data.loc[:, "new_deaths"]
plt.plot(world_dates, world_new_cases, 'ro')
plt.plot(world_dates, world_new_cases, 'b+')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.show()  # The x-axis rotated 90 degrees
'''


raw = covid_data["location"] == "World"
world = covid_data.loc[raw,:]
world_new_deaths=world.loc[:,"new_deaths"]
world_dates=world.loc[:, "date"]
world_new_cases=world.loc[:,"new_cases"]
plt.legend(['world new deaths', 'world new cases'], loc='upper left')
plt.plot(world_dates, world_new_cases, 'r+', label='new cases')
plt.plot(world_dates, world_new_deaths, 'b+', label='new deaths') 
plt.legend(loc=2, ncol=3)
plt.xticks(world_dates[0:len(world_dates):4],rotation=-90)
plt.title('The new cases and deaths for the whole world over time')
plt.show()  # plot the data for the new cases and new deaths


raw1 = covid_data["location"] == "Afghanistan"
Afghanistan = covid_data.loc[raw1,:]
#print(Afghanistan)
Afghanistan_new_cases = Afghanistan.loc[:,"new_cases"]
Afghanistan_total_cases = Afghanistan.loc[:,"total_cases"]
Afghanistan_dates = Afghanistan.loc[:,"date"]
plt.legend(['Afghanistan new cases', 'Afghanistan total cases'], loc='upper left')
plt.plot(Afghanistan_dates, Afghanistan_total_cases, 'r+', label='total cases') 
plt.plot(Afghanistan_dates, Afghanistan_new_cases, 'b+', label='new cases')
plt.legend(loc=2, ncol=3)
plt.xticks(Afghanistan_dates[0:len(Afghanistan_dates):4],rotation=-90)
plt.title('The new cases and total cases for Afghanistan over time')  # Question: How have new cases and total cases developed over time in the Afghanistan?



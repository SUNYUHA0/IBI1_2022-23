'''
Compare the size of value to salary
'''
def calculator(value, salary):
    if value > 5*salary:
        return "No"
    else:
        return "Yes"

# value = 180000
# salary = 35000
value = 100000
salary = 9000
z = calculator(value, salary)
print(calculator(value,salary))  # An example.
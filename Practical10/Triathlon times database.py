'''
Attribute an instance
'''
class triathlon (object):
    def __init__(self, first_name, last_name, location, swim_time, cycle_time, run_time, total_time):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.swim_time = swim_time
        self.cycle_time = cycle_time
        self.run_time = run_time
        self.total_time = total_time

first_name = 'Peter'
last_name = 'Parker'
location = 'Queens'
swim_time = '60'  # Enter the time in minutes
cycle_time = '50'  # Enter the time in minutes
run_time = '40'  # Enter the time in minutes
total_time = str(int(swim_time) + int(cycle_time) + int(run_time))
triathlon1 = triathlon(first_name, last_name, location, swim_time, cycle_time, run_time, total_time)
print(triathlon1.first_name, triathlon1.last_name, triathlon1.location, triathlon1.swim_time + 'min', triathlon1.cycle_time + 'min', triathlon1.run_time + 'min', triathlon1.total_time + 'min')
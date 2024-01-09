import pandas as pd
import random

data = pd.read_csv('chess-tournament.csv')

# variables
old_group = []
new_group = []

# loading data from the form into a list
for num in data.Sno:
    old_group.append(num)

length = len(old_group) # for the number of iterations

# iterating through the old list to randomly generate a new list
for x in range(length):
    random_num = random.choice(old_group) # randomly generate a value from the old order
    new_group.append(random_num) # append the randomly generated value into the new list
    old_group.pop(old_group.index(random_num)) # delete the number from the old order not to risk duplication
    
print(new_group)



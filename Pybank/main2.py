#Import modules

import os
import csv

#Define variables 
total_amount = 0
average_changes = 0
profit_loses = []
months = []
increase_decrease = []

#Define path 
path = os.path.join("..", "Resources", "02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")

# Open and read csv and append each row to its corresponding list, defined earlier
# Obtain total months with method len()
# Make a For loop to obtain the total amount of profit/loses
# Calculate average changes (average_changes = (final value - initial value) / 86(last month) - 1(first month))

with open(path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader)
    for row in csvreader:
        profit_loses.append(int(row[1]))
        months.append(row[0])
    total_months = len(months)
#print(f"Total Months: {total_months}")
for value in profit_loses:
        total_amount = total_amount + value
average_changes = round((profit_loses[-1]  - profit_loses[0] ) / (total_months - 1), 2)


# Make a new list with the diference between actual value and past value
# Start the for loop in the second row since the first value would have been: value - 0 
# Equation (Greatest increse in profits = actual value - past value)

it = 1
for value in profit_loses:
    if it == len(profit_loses):
        break
    else:
        increase = profit_loses[it] - value
        it = it + 1
            #print(increase)
        increase_decrease.append(increase)

# Delete the first row of months because the increase or decrease is seen from the second month.
# Make a dictionary with months and the new list (increase_decrease)

del months[0]
percentage_change = dict(zip(months, increase_decrease))

# Define a function to sort the dictionary in descending order and assign this to a new list 
# The greatest increase and decrease in profits is the first and last values of the sorted dictionary

def values(item):
    return item[1]
sorted_per_change = []
for pair in sorted(percentage_change.items(), key=values, reverse=True):
    sorted_per_change.append(pair)

print(f"Total Months: {total_months}")
print(f"Total: ${total_amount}")
print(f"Average Change: ${average_changes}")
print(f"Greatest Increase in Profits: {sorted_per_change[0][0]} (${sorted_per_change[0][1]})")
print(f"Greatest Decrease in Profits: {sorted_per_change[-1][0]} (${sorted_per_change[-1][1]})")

# Define the path to create the txt file 
# Instead of using the open function to read files, this is used to write the txt file
# The txt file is created in the same folder, that is in the current working directory

path2 = os.path.join("Financial Analysis.txt")

with open(path2, "w") as textfile:
    textfile.write("Financial Analysis")
    textfile.write("\n---------------------")
    textfile.write(f"\nTotal Months: {total_months}")
    textfile.write(f"\nTotal: ${total_amount}")
    textfile.write(f"\nAverage Change: ${average_changes}")
    textfile.write(f"\nGreatest Increase in Profits: {sorted_per_change[0][0]} (${sorted_per_change[0][1]})")
    textfile.write(f"\nGreatest Decrease in Profits: {sorted_per_change[-1][0]} (${sorted_per_change[-1][1]}")
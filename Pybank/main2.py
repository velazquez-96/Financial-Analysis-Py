import os
import csv

total_amount = 0
average_chanes = 0
profit_loses = []
months = []
increase_decrease = []

path = os.path.join("..", "Resources", "02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")

with open(path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    print(f"Headers: {next(csvreader)}")
    for row in csvreader:
        #print(row[1])
        profit_loses.append(int(row[1]))
        months.append(row[0])

print("Financial Analysis")
print("-----------------------------")

total_months = len(months)
print(f"Total Months: {total_months}")

for value in profit_loses:
    total_amount = total_amount + value
    #average_chanes = (final value - initial value) / 86(last month) - 1(first month)

average_chanes = round((profit_loses[-1]  - profit_loses[0] ) / (total_months - 1), 2)

print(f"Total: ${total_amount}")
print(f"Average Change: ${average_chanes}")

#Greatest increse in profits = actual value - past value

it = 1
for value in profit_loses:
        if it == len(profit_loses):
            break
        else:
            increase = profit_loses[it] - value
            it = it + 1
            #print(increase)
            increase_decrease.append(increase)

#print(increase_decrease)
del months[0]
#print(months)
percentage_change = dict(zip(months, increase_decrease))

def values(item):
    return item[1]
sorted_per_change = []
for pair in sorted(percentage_change.items(), key=values, reverse=True):
    sorted_per_change.append(pair)

#print(sorted_per_change)
print(f"Greatest Increase in Profits: {sorted_per_change[0][0]} (${sorted_per_change[0][1]})")
print(f"Greatest Decrease in Profits: {sorted_per_change[-1][0]} (${sorted_per_change[-1][1]})")


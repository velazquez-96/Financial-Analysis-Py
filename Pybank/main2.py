import os
import csv

total_amount = 0
average_chanes = 0
profit_loses = []
months = []

path = os.path.join("..", "Resources", "02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")

with open(path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    print(f"Headers: {next(csvreader)}")
    for row in csvreader:
        #print(row[1])
        profit_loses.append(int(row[1]))
        months.append(row[0])

total_months = len(months)
print(f"Total Months: {total_months}")

for value in profit_loses:
    total_amount = total_amount + value
    #average_chanes = (final value - initial value) / 86(last month) - 1(first month)

average_chanes = round((profit_loses[-1]  - profit_loses[0] ) / (total_months - 1), 2)

print(f"Total: ${total_amount}")
print(f"Average Change: ${average_chanes}")

# Import required modules, define the path to read th csv file and variables as well

import os 
import csv

path = os.path.join("..", "Resources", "02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv")

total = 0
candidates = []
unique_cand = []
votes_election = []
percentage = []

# Read csv file; skip headers
# Count the number of elements with variable "total" and append row 2 to a new list
# Know the unique candidates in the election converting the list to a set
# Convert the set to a tuple and iterate through it to apply the count method (know the votes of each candidate)
# Append the aforementioned values to a new list
# Calculate percentage of votes iterating through the votes list
# Zip the three lists and sort them in descending order
# The winner is the candidate in the first position


with open(path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader)
    for row in csvreader:
        total = total + 1
        candidates.append(row[2])
    unique_cand = set(candidates)
    for x in tuple(unique_cand):
        z = candidates.count(x)
        votes_election.append(z)
    for t in votes_election:
        c = round((t / total) * 100 )
        percentage.append(c)
    final_results = sorted(list(zip(votes_election, unique_cand, percentage)), reverse=True)
    #print(final_results)
    winner = final_results[0][1]
    # for a,b,c in final_results:
    #     print(f"{b}: {c}% ({a})")


print("Election Results")
print("--------------------------------------")
print(f"Total votes: {total}")
print("--------------------------------------")   
for a,b,c in final_results:
        print(f"{b}: {c}% ({a})")

print("--------------------------------------")
print(f"Winner: {winner}")
print("--------------------------------------")

path2 = os.path.join("Election results")

with open(path2, "w") as textfile:
    textfile.write("Election Results")
    textfile.write("\n--------------------------------------")
    textfile.write(f"\nTotal votes: {total}")
    textfile.write("\n--------------------------------------")   
    for a,b,c in final_results:
        textfile.write(f"\n{b}: {c}% ({a})")
    textfile.write("\n--------------------------------------")
    textfile.write(f"\nWinner: {winner}")
    textfile.write("\n--------------------------------------")
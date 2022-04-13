#Modules
import os
import csv

# Setting up Variables
total_number_of_votes = 0
percentage_of_votes_each_candidate_won = 0.0
total_number_of_votes_each_candidate_won = 0
winner_of_election = "winner"


# Setting up Lists
voter_id = []
country = []
candidate = []
candidate_with_votes =[]


# Pulling and reading the csv file
csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader =  csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        voter_id.append(row[0])
        country.append(row[1])
        candidate.append(row[2])

# The total number of votes cast
total_number_of_votes = len(voter_id)


# A complete list of candidates who received votes
for name in candidate:
    if name not in candidate_with_votes:
        candidate_with_votes.append(name)
#print(candidate_with_votes)

print("hi")
# The percentage of votes each candidate won
counter = 0
for name in candidate:
    if name == candidate_with_votes[0]:
        counter = counter + 1
print(counter)        
print('bye')

# The total number of votes each candidate won



# The winner of the election based on popular vote.



# Print out the results to terminal
print("----------------------------")
print("Election Results")
print("----------------------------")
print("Total Votes: " + str(total_number_of_votes))
print("----------------------------")
#For loop to print canidates with votes
print(str(candidate_with_votes) +": " + str(percentage_of_votes_each_candidate_won) + "% (" + str(total_number_of_votes_each_candidate_won) + ")")
#...
print("----------------------------")
print("Winner: " + str(winner_of_election))
print("----------------------------")

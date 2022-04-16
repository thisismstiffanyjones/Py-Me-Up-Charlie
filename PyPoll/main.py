#Modules
import os
import csv

# Setting up Variables
total_number_of_votes = 0
winner_of_election = "winner"


# Setting up Lists
voter_id = []
votes = []
candidates =[]
number_of_votes_per_canidate = []
precentage_of_votes_per_canidate =[]


# Pulling and reading the csv file
csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader =  csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        voter_id.append(row[0])
        votes.append(row[2])


# The total number of votes cast
total_number_of_votes = len(voter_id)


# A complete list of candidates who received votes
for name in votes:
    if name not in candidates:
        candidates.append(name)


# The total number of votes each candidate won
vote_count=0
i=0
for candidate in candidates:
   
    for vote in votes:
       
        if vote == candidates[i]:
            vote_count = vote_count + 1
   
    number_of_votes_per_canidate.append(vote_count)
   
    i=i+1
   
    vote_count=0


# The percentage of votes each candidate won
bucket = 0
i=0
for number in number_of_votes_per_canidate:
   
    bucket = round(number_of_votes_per_canidate[i] / total_number_of_votes * 100, 3)
   
    precentage_of_votes_per_canidate.append(bucket)
  
    i=i+1
  
    bucket = 0


# The winner of the election based on popular vote.
winning_tally=number_of_votes_per_canidate[1]
for number in number_of_votes_per_canidate:
    if number>winning_tally:
        winning_tally=number
winner_of_election=candidates[number_of_votes_per_canidate.index(winning_tally)]


# Print out the results to terminal
print("----------------------------")
print("Election Results")
print("----------------------------")
print("Total Votes: " + str(total_number_of_votes))
print("----------------------------")

#For loop to print canidates with votes
i=0
for candidate in candidates:
    print(str(candidates[i]) +": " + str(precentage_of_votes_per_canidate[i]) + "% (" + str(number_of_votes_per_canidate[i]) + ")")
    i=i+1

print("----------------------------")
print("Winner: " + str(winner_of_election))
print("----------------------------")


# Printing of Financial Analysis to Text File
output_path = os.path.join("analysis", "poll_data.txt")

with open(output_path, "w") as text_file:
    print(f"--------------------", file=text_file)
    print(f"Election Results", file=text_file)
    print(f"--------------------", file=text_file)
    print(f"Total Votes: {total_number_of_votes}", file=text_file)
    print(f"--------------------", file=text_file)
    
    i=0
    for candidate in candidates:
        print(f"{candidates[i]}: {precentage_of_votes_per_canidate[i]}% ({number_of_votes_per_canidate[i]})", file=text_file)
        i=i+1

    print(f"--------------------", file=text_file)
    print(f"Winner: {winner_of_election}", file=text_file)
    print(f"--------------------", file=text_file)
  
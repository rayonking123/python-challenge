import csv
import os

file_to_load = "C:\\Users\\rockm\\Desktop\\School\\homework\\Python-challenge\\Starter_Code\\PyPoll\\Resources\\election_data.csv"

# Vote Counter
total_votes = 0

# Using a set to store unique candidate names
candidate_options = set()

# Dictionary to store candidate votes
candidate_votes = {}

winning_candidate = ""
winning_count = 0

# Convert to dictionaries
with open(file_to_load) as election_data:
    reader = csv.DictReader(election_data)

    for row in reader:
        total_votes += 1

        candidate_name = row["Candidate"]

    
        candidate_options.add(candidate_name)

       
        candidate_votes.setdefault(candidate_name, 0)

        # Vote count
        candidate_votes[candidate_name] += 1

# Print and write election results

    election_results = (
        f"\nElection Results\n"
        f"----------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-----------------------\n"
    )
    print(election_results)
 

    for candidate in candidate_options:
        votes = candidate_votes[candidate]
        vote_percentage = (votes / total_votes) * 100

        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output)
  

        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate

    winning_candidate_summary = (
        f"-----------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-----------------------\n"
    )

    print(winning_candidate_summary)
   

# In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.

# You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:

# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote

import csv

totalvotes = 0
candidate_list = []
candidate_votes = {}
candidate = ""
percentageofvotespercandidate = 0
totalvotespercandidate = 0
winner = ""
candidate1 = 0
candidate2 = 0
candidate3 = 0
candidate1pct = 0
candidate2pct = 0
candidate3pct = 0


with open('Resources/election_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = next(csv_reader)

    # pull and calculate the names and votes data from the source    
    for row in csv_reader: 
        totalvotes += 1

        candidate = row[2]

        if candidate not in candidate_list:
            candidate_list.append(candidate)
            candidate_votes[candidate] = 0

        candidate_votes[candidate]  += 1

         
        
with open('Analysis/election_data.txt',"w") as file:

    # calculate total number of votes and total votes per candidate
    # calculate percentage of votes per candidate
    result = candidate_votes
    # identify winner
    winner = max (result,key=result.get)
    print("Election Results")
    print("---------------------------------")
    print("Total Votes: ",totalvotes)
    print("---------------------------------")
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        candidatepct = round((votes/totalvotes)*100, 3)
        voter_OP = f"{candidate_name} : {candidatepct}% ({votes}) \n"
        print(voter_OP, end = "")
    print("---------------------------------")
    print("Winner: ",winner)
    print("---------------------------------")
    #with open('Analysis/election_data.txt',"w") as file:
    file.write(voter_OP)


    
#csv.writer('Analysis/election_data.txt')

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

        
    for row in csv_reader:   
        totalvotes += 1
         
        if str(row[2]) == 'Charles Casper Stockham':
            candidate1 += 1
        elif str (row[2]) == 'Diana DeGette':
            candidate2 += 1
        else:
            candidate3 += 1 

        candidate1pct = round((candidate1/totalvotes)*100, 3)
        candidate2pct = round((candidate2/totalvotes)*100, 3)
        candidate3pct = round((candidate3/totalvotes)*100, 3)


    result = {"Charles Casper Stockham":candidate1,"Diana DeGette":candidate2,"Ramon Anthony Doane":candidate3}
    winner = max (result,key=result.get)


with open('Resources/election_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = next(csv_reader)

    for row in csv_reader:
        candidate_list = []
        candidate = row[2]
        if candidate not in candidate_list:
            candidate_list.append(candidate)




print (candidate_list)

output = f"""
Election Results
-------------------------
Total Votes: {totalvotes}
-------------------------
Charles Casper Stockham: {candidate1pct}% ({candidate1})
Diana DeGette: {candidate2pct}% ({candidate2})
Raymon Anthony Doane: {candidate3pct}% ({candidate3})
-------------------------
Winner: {winner}
-------------------------
"""
print(output)

with open('Analysis/election_data.text',"w") as analysis_file:
    analysis_file.write(output)



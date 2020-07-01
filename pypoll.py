import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")


print("opening", csvpath)

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
  
    print(csvreader)

    csv_header =next(csvfile)
 
    print(f"Header: {csv_header}")
    votes = 0
    winner_votes = 0 
    total_candidates = 0
    most_votes = ["", 0]
    candidates = [] 
    candidate_votes = {}


    for row in csvreader:
        votes = votes + 1
        total_candidates = row["Candidate"]        


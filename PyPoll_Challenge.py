# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
total_county_votes = 0
# County options, county votes, candidate options and candidate votes.
county_options = []
county_votes = {}
candidate_options = []
candidate_votes = {}
# Track the winning county, vote count, and percentage; the winning candidate, vote count, and percentage.
winning_county = ""
winning_county_count = 0
winning_county_percentage = 0
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate, add the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row. 
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_county_votes += 1 
        # Print the county name from each row.
        county_name = row[1]
        if county_name not in county_options:
            # Add the county name to the county list.
            county_options.append(county_name)
            # 2. Begin tracking that county's vote count. 
            county_votes[county_name] = 0
        # Add a vote to that county's count.
        county_votes[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "a") as txt_file:
    print("County Votes:")
    txt_file.write("County Votes:\n")   
    # Determine the percentage of votes for each county by looping through the counts.
    # Iterate through the county list.
    for county in county_votes:
        # Retrieve vote count of a county.
        counties_votes = county_votes[county]
        # Calculate the percentage of votes.
        counties_vote_percentage = float(counties_votes) / float(total_county_votes) * 100
        county_results = (
            f"{county}: {counties_vote_percentage:.1f}% ({counties_votes:,})\n")
        #  To do: print out each county's name, vote count, and percentage of
        # votes to the terminal.
        # Print the final vote count to the terminal.
        print(county_results)
        #  Save the county results to our text file.
        txt_file.write(county_results)
        # Determine winning vote count, winning percentage, and winning county.
        if (counties_votes > winning_county_count) and (counties_vote_percentage > winning_county_percentage):
            winning_county_count = counties_votes
            winning_county = county
            winning_county_percentage = counties_vote_percentage
    Largest_County_Turnout = (
        f"\n"
        f"-------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"-------------------------\n")
    # Print the winning county's results to the terminal.
    print(Largest_County_Turnout)
    # Save the winning county's name to the text file.
    txt_file.write(Largest_County_Turnout)
    for candidate in candidate_votes:
    # Retrieve vote count and percentage.
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)
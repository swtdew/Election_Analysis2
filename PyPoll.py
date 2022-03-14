# The data we need to retrieve
# 1. Total # of votes cast
# 2. Complete list of candidates who recieved votes
# 3. Percent of votes each candidate won
# 4. Total number of vosetes each candidate won
# 5. Winner of the election based on popular vote

# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)


import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# 1. Initialize a total vote counter.
total_votes = 0
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.Read the file object with the reader function.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # print each row in the CSV file.
# Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Print the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
           # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
with open(file_to_save, "w") as txt_file:
    # After opening the file print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)


    # # Print the candidate list.
    # print(candidate_options)
    # # Print the candidate vote dictionary.
    # print(candidate_votes)
    # print(total_votes)






# file_to_save = os.path.join("Analysis", "election_analysis.txt")
# # Read the file object with the reader function.
# file_reader = csv.reader(election_data)

# # Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:
#     txt_file.write("Counties in the Election") 
#     txt_file.write("\nArapahoe\nDenver\nJefferson")
# # Close the file
# txt_file.close()







# counties = ["Arapahoe","Denver","Jefferson"]
# my_list = [counties]
# print(counties)
# print(counties[0])
# counties_dict= {"Arapahoe": 422829,"Denver": 463353,"Jefferson":432438}
# print(len(counties_dict))
# print(counties_dict)
# print(counties_dict['Arapahoe'])

# github code below ends on line 54 
# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for county in counties_dict:
#     print(county)
# for county in counties_dict.keys():
#     print(county)
# for voters in counties_dict.values():
#     print(voters)
# for county in counties_dict:
#     print(counties_dict[county])   
# for county in counties_dict:
#     print(counties_dict.get(county)) 
# for county,voters in counties_dict.items():
#     print(county,voters)
# voting_data = []
# voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
# voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
# voting_data.append({"county":"Jefferson","registered_voters": 432438})
# voting_data
# for county,voters in counties_dict.items():
#     print(county,voters)
# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                 {"county":"Denver", "registered_voters": 463353},
#                 {"county":"Jefferson", "registered_voters": 432438}]
# for counties_dict in voting_data:
#     print(counties_dict)
# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for county,voters in counties_dict.items():
#     print(county + " county has" + str( voters) + " registered voters")
# for county,voters in counties_dict.items():
#     print(f"{county} county has {voters} registered voters")
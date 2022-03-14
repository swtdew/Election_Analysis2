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
# Open the election results and read the file.
with open(file_to_load) as election_data:
        # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
        # Print each row in the CSV file.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)


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
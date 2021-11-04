# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of canidates who received votes
# 3. The percentage of votes each canidate won
# 4. The total number of votes each canidate won
# 5. The winner of the election based on popular vote 

# Add dependencies (components required for code to execute w/o error)
import csv
#access file & allow us to open, fetch contents, creating/removing directory file
import os
# Assign a variable (file_to_load) to load file from path. 
# (os.path.join - "chaining" concatenates several path components )
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable (file_to_save) to save file to path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# [with] open() election results and read file. 
# (NOTE: NEED COLON at end of with statement; next line REQUIRES INDENT)
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # 1. Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)
#assign variable for file to load & path for file
file_to_load = 'Resources\election_results.csv'
#open() election results & read (r)
    #election_data = open(file_to_load, 'r')
    #refactored: NOTE: with to open() and close
with open(file_to_load) as election_data:

    #To do: perform analysis.
    #NOTE: need to indent after with b/c of ':'
    print(election_data)

#refactored: line 13
#Close file (to store data!!!). (NOTE: if not closed at end of data, can lose some data (be overwriten)
#election_data.close()

#final refactored code from above
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)


# Create filename variable to a direct/indirect path to file
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

     # Write three counties to the file. newline escape sequnence 
     txt_file.write("Countries in the Election\n--------------------------\nArapahoe\nDenver\nJefferson")
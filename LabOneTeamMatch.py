'''
File: LabOneTeamMatch.py
Author: Sidak Singh
Date: Nov 15 2024

Description: All possible games between 7 different teams.
Each team plays each other twice.
'''

#========================== Main program ===================================
for i in range(1, 8):
    for j in range(1, 8):
        if (i == j) :
            continue
        else:
            print(f"Team {i} plays Team {j}")

__author__ = 'Joe'
# load all json files in current directory and add them into one single csv file
import csv
import json
import os

csvFileObj = open("totalProfile.csv", "w")
csvWriter = csv.writer(csvFileObj)
csvWriter.writerow(["indiv_nurse", "screen_name", "username", "tweets", "followers", "following", "SA", "bio"])

for jsonFilename in os.listdir('.'):
    if not jsonFilename.endswith('.json'):
        continue
    print('Open file ' + jsonFilename)
    with open(jsonFilename) as jsonfile:
        x = json.load(jsonfile)

        for row in x:
            csvWriter.writerow(["",
                   row["screen_name"],
                   row["username"],
                   row["tweets"],
                   row["followers"],
                   row["following"],
                   row["SA"],
                   row["bio"]])
csvFileObj.close()

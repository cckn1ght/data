
# shuffle the totalProfile.csv file
import csv, random

csvRows = []
csvFileObj = open('totalProfile.csv', 'r', encoding='utf-8', errors='ignore')
readerObj = csv.reader(csvFileObj)
for row in readerObj:
    if readerObj.line_num == 1:
        continue  # skip the first row
    csvRows.append(row)
csvFileObj.close()

random.shuffle(csvRows)

csvFileObj2 = open('shuffledCSV.csv', 'w', newline='')
csvWriter = csv.writer(csvFileObj2)
# write the first line
csvWriter.writerow(["indiv_nurse", "screen_name", "username", "tweets", "followers", "following", "SA", "bio"])
for row in csvRows:
    csvWriter.writerow(row)
print("The file has been shuffled")
csvFileObj2.close()
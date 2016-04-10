# Find the annotated profiles in the total CSV file
import csv
import json

class nurse_finder(object):
    def __init__(self, in_file, out_file):
        self.csv_rows = []
        self.nurse_number = 0
        self.csv_file = in_file
        self.out_file = out_file
        self.nurse_list = []

    def find(self):
        csv_rows = self.csv_rows
        nurse_number = self.nurse_number
        nurse_list = self.nurse_list
        with open(self.csv_file, 'r', encoding='utf-8', errors='ignore') as f:
            with open(self.out_file, 'w', newline='') as wf:
                # f.next()
                file_reader = csv.reader(f)
                file_reader.__next__()
                for row in file_reader:
                    if row[0] == 'y':
                        # csv_rows.append(row)  # Append the first row
                        nurse_list.append(row[1])
                        nurse_number += 1
                    # elif row[0] == 'y' or row[0] == 'n':     # find the annotated line
                    #     csv_rows.append(row)
                print(str(nurse_number) + " nurses have been found.")
                json.dump(nurse_list, wf)


def main():
    finder1 = nurse_finder('annotated_only.csv', 'yes_nurses.json')
    finder1.find()

if __name__ == "__main__":
    main()

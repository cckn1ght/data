# Find the annotated profiles in the total CSV file
import csv

class annotated_finder(object):
    def __init__(self, in_file, out_file):
        self.csv_rows = []
        self.not_annotated_row = 0
        self.csv_file = in_file
        self.out_file = out_file

    def find(self):
        csv_rows = self.csv_rows
        not_annotated_row = self.not_annotated_row
        with open(self.csv_file, 'r', encoding='utf-8', errors='ignore') as f:
            with open(self.out_file, 'w', encoding='utf-8', newline='') as wf:
                file_reader = csv.reader(f)
                csv.writer(wf).writerow(file_reader.next())
                for row in file_reader:
                    if row[0] == '':
                        # csv_rows.append(row)  # Append the first row
                        csv.writer(wf).writerow(row)
                        not_annotated_row += 1
                    # elif row[0] == 'y' or row[0] == 'n':     # find the annotated line
                    #     csv_rows.append(row)
        print(str(not_annotated_row) + " lines of annotated bios.")

def main():
    finder1 = annotated_finder('nurse_users_annoated.csv', 'not_annotated.csv')
    finder1.find()

if __name__ == "__main__":
    main()

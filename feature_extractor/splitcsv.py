# Find the annotated profiles in the total CSV file
import csv

class annotated_finder(object):
    def __init__(self, in_file, out_file):
        self.csv_rows = []
        self.annotated_row = 0
        self.csv_file = in_file
        self.out_file = out_file

    def find(self):
        csv_rows = self.csv_rows
        annotated_row = self.annotated_row
        with open(self.csv_file, 'r', encoding='utf-8', errors='ignore') as f:
            with open(self.out_file, 'w', newline='') as wf:
                file_reader = csv.reader(f)
                for row in file_reader:
                    # if row[0] != '':
                        # csv_rows.append(row)  # Append the first row
                    csv.writer(wf).writerow(row)
                    annotated_row += 1
                    # elif row[0] == 'y' or row[0] == 'n':     # find the annotated line
                    #     csv_rows.append(row)
                    if annotated_row == 1501:
                        break

        print(str(annotated_row - 1) + " lines of annotated bios.")

def main():
    finder1 = annotated_finder('nurse_users_annoated.csv', '1500pieces.csv')
    finder1.find()

if __name__ == "__main__":
    main()

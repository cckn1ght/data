# Find the annotated profiles in the total CSV file
import csv
from tabulate import tabulate

class evaluator(object):
    def __init__(self, in_file):
        # self.csv_rows = []
        # self.line = 0
        self.csv_file = in_file
        # self.out_file = out_file

    def evaluate(self):
        csv_rows = []
        evaluated_line = 0
        pre_yes = 0
        pre_no = 0
        actual_yes = 0
        actual_no = 0
        both_yes = 0
        both_no = 0
        with open(self.csv_file, 'r', encoding='utf-8', errors='ignore') as f:
            # with open(self.out_file, 'w', encoding='utf-8', newline='') as wf:
            file_reader = csv.reader(f)
            file_reader.__next__()
            # csv.writer(wf).writerow(file_reader.__next__())
            for row in file_reader:
                if row[3] == 'y':
                    # csv_rows.append(row)  # Append the first row
                    # csv.writer(wf).writerow(row)
                    pre_yes += 1
                    if row[1] == 'y':
                        both_yes += 1
                elif row[3] == 'n':
                    pre_no += 1
                    if row[1] == 'n':
                        both_no += 1
                if row[1] == 'y':
                    actual_yes += 1
                elif row[1] == 'n':
                    actual_no += 1
                elif row[1] == '':
                    break
                evaluated_line += 1
                # elif row[0] == 'y' or row[0] == 'n':     # find the annotated line
                #     csv_rows.append(row)
        # print(str(not_annotated_row) + " lines of annotated bios.")
        print('predicted yes: %d' % pre_yes)
        print('predicted no: %d' % pre_no)
        print('actual yes: %d' % actual_yes)
        print('actual no: %d' % actual_no)
        print('both yes: %d' % both_yes)
        print('both no: %d' % both_no)
        table = [['a', 'b', '<--classified as'], [both_yes, pre_no - both_no, ' | a = y'], [pre_yes - both_yes, both_no, ' | b = n']]
        print(tabulate(table))

def main():
    evaluator1 = evaluator('prediction_RandomForest.csv')
    evaluator1.evaluate()

if __name__ == "__main__":
    main()

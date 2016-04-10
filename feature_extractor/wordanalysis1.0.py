import csv
import operator
from nltk import word_tokenize
from nltk.stem.porter import *
from nltk.corpus import stopwords


class word_analyzer():
    def __init__(self, csvfile):
        self.csv_file = csvfile
        self.stemmer = PorterStemmer()
        self.stop_words_list = stopwords.words('english')

    def extract_words(self):
        stop_words_list = self.stop_words_list
        # strings for all words and all names
        all_words_string = ''
        # all_name_string = ''
        bio_freq_yes = {}            # yes class dictionary frequency
        bio_freq_no = {}             # no class dictionary frequency
        # name_freq_yes = {}
        # name_freq_no = {}
        with open(self.csv_file, 'r', encoding='utf-8', errors='ignore') as annotated_file:
            annotated_reader = csv.reader(annotated_file)
            for line in annotated_reader:
                # bio_string = line[7]      # The bio information
                # regular expression filter for all US ASCII Character Set
                bio_string = re.sub(r'[^\x00-\x7f]', r' ', line[2])
                bio_text = word_tokenize(bio_string)
                all_words_string = all_words_string + ' ' + bio_string

                # remove the stop words for bio information
                no_stop_bio_text = [t for t in bio_text if t not in stop_words_list]

                if line[0] in ["y"]:          # line[0] is the class info
                    for word in no_stop_bio_text:       # create bio_freq_yes list for bio words frequency counting
                        word = word.lower()
                        if word in bio_freq_yes:
                            bio_freq_yes[word] += 1
                        else:
                            bio_freq_yes[word] = 1

                if line[0] in ["n"]:
                    for word in no_stop_bio_text:
                        word = word.lower()
                        if word in bio_freq_no:
                            bio_freq_no[word] += 1
                        else:
                            bio_freq_no[word] = 1
        all_tokens = word_tokenize(all_words_string)
        unique_words = set(all_tokens)
        print(unique_words)
        print(all_words_string)
        print(len(all_words_string))
        print(len(unique_words))
        self.sort_words(bio_freq_no, bio_freq_yes)

    def sort_words(self, bio_freq_no, bio_freq_yes):
        # sort the lists
        stemmer = self.stemmer
        words_bio_freq_no_sorted = []
        words_bio_freq_yes_sorted = []

        print("no class bio words frequency")
        bio_freq_no_sorted = sorted(list(bio_freq_no.items()), key=operator.itemgetter(1), reverse=True)
        for tup in bio_freq_no_sorted:
            words_bio_freq_no_sorted.append(tup[0])
        print(bio_freq_no_sorted[:])
        print("\n")

        print("yes class bio words frequency")
        bio_freq_yes_sorted = sorted(list(bio_freq_yes.items()), key=operator.itemgetter(1), reverse=True)
        for tup in bio_freq_yes_sorted:
            words_bio_freq_yes_sorted.append(tup[0])
        print(bio_freq_yes_sorted[:])
        print("   ")

        list_automatic_freq_yes = []
        list_automatic_freq_no = []
        for word in words_bio_freq_no_sorted:
            if word not in words_bio_freq_yes_sorted:
                list_automatic_freq_no.append(stemmer.stem(word.lower()))

        for word in words_bio_freq_yes_sorted:
            if word not in words_bio_freq_no_sorted:
                list_automatic_freq_yes.append(stemmer.stem(word.lower()))

        print("automatic dictionary yes")
        print(list_automatic_freq_yes)
        print("automatic dictionary no")
        print(list_automatic_freq_no)
        self.fun_create_files_of_word_lists(list_automatic_freq_yes, list_automatic_freq_no)

    def fun_create_files_of_word_lists(self, yes_list, no_list):
        with open('auto_yes_list_file.txt', 'w') as yes_list_file:
            for item in yes_list:
                yes_list_file.write(item)
                yes_list_file.write('\n')

        with open('auto_no_list_file.txt', 'w') as no_list_file:
            for item in no_list:
                no_list_file.write(item)
                no_list_file.write('\n')


def main():
    csv_analyzer = word_analyzer('annotated_only.csv')
    csv_analyzer.extract_words()

if __name__ == "__main__":
    main()

import nltk
import re
import string
import csv
import operator
from nltk import word_tokenize
from nltk.stem.porter import *
from nltk.corpus import stopwords

class feature_extractor(object):
    def __init__(self, infile, outfile):
        self.csv_name = infile
        self.output_file = outfile
        self.file_pronouns = 'pronouns.txt'
        self.stemmer = PorterStemmer()
        self.auto_yest_list = 'auto_yes_list_file.txt'
        self.auto_no_list = 'auto_no_list_file.txt'
        self.from_file_list_automatic_freq_no = []
        self.from_file_list_automatic_freq_yes = []
        self.pre_process()

    def pre_process(self):
        with open(self.auto_yest_list, 'r') as yes_list_file:
            # remove new line
            for word in yes_list_file.readlines():
                word = word.replace('\n', '')
                self.from_file_list_automatic_freq_yes.append(word)

        with open(self.auto_no_list, 'r') as no_list_file:
            for word in no_list_file.readlines():
                word = word.replace('\n', '')
                self.from_file_list_automatic_freq_no.append(word)

    # count NNP tags number
    # def func_tags_NNP(self, tag_sequence):
    #     count_nnp = 0
    #     for tup in tag_sequence:
    #         if tup[1] == 'NNP':
    #             count_nnp += 1
    #     return count_nnp

    # # count PRP tag number
    # def func_tags_PRP(self, tag_sequence):
    #     count_prp = 0
    #     for tup in tag_sequence:
    #         if tup[1] == 'PRP':
    #             count_prp += 1
    #     return count_prp

    def automatic_freq_no(self, text, no_list):
        count_words = 0

        for word in text:
            word1 = self.stemmer.stem(word.lower())
            if word1 in no_list:
                count_words += 1
        return count_words

    def automatic_freq_yes(self, text, yes_list):
        count_words = 0

        for word in text:
            word1 = self.stemmer.stem(word.lower())
            if word1 in yes_list:
                count_words += 1
        return count_words

    def bio_func_No_freq_terms(self, text):
        has_no_words = 0
        with open('no_words.txt') as file:
            no_freq_terms = file.read().splitlines()
        # print(no_freq_terms)
        for word in text:
            if word in no_freq_terms:
                has_no_words += 1
        return has_no_words

    def bio_func_Yes_freq_terms(self, text):

        has_yes_words = 0
        with open('yes_words.txt') as file:
            yes_freq_terms = file.read().splitlines()
        # print(yes_freq_terms)
        # yes_freq_terms = ['registered', 'love', 'wife', 'health', 'university', 'my', 'proud', 'lover',
        #                   'girl', 'fan', 'family', 'mental', 'daughter', 'school', 'singer', 'sister', 'food']
        for word in text:
            if word in yes_freq_terms:
                has_yes_words += 1
        return has_yes_words

    def extract(self):
        outfile = open(self.output_file, 'w', newline='')
        with open(self.file_pronouns, 'r') as f_pronouns:
            list_pronouns = word_tokenize(f_pronouns.read())
        feature_writer = csv.writer(outfile)
        feature_writer.writerow(['screen_name', 'upper_letter_count',
                                 'upper_ratio', 'followers_count',
                                 'friends_count',
                                 'bio_auto_Yes_freq_terms',
                                 'bio_auto_No_freq_terms', 'has_no_words',
                                 'has_yes_words', 'class'])
        #################################################################
        with open(self.csv_name, 'r', encoding='utf-8', errors='ignore') as annotated_file:
            annotated_reader = csv.reader(annotated_file)
            for line in annotated_reader:
                if annotated_reader.line_num == 1:
                    continue  # skip the first row
                # the third column is the bio info
                bio_string = re.sub(r'[^\x00-\x7f]', r' ', line[2])
                bio_text = word_tokenize(bio_string)
                # name_text = word_tokenize(name_string)
                bio_tag_sequence = nltk.pos_tag(bio_text)
                # name_tag_sequence = nltk.pos_tag(name_string)
                bio_pronouns_count = 0
                for token in bio_text:
                    if token in list_pronouns:
                        bio_pronouns_count += 1

                #####################################################################
                list_automatic_freq_no = self.from_file_list_automatic_freq_no[:]
                list_automatic_freq_yes = self.from_file_list_automatic_freq_yes[:]

                # print("bio frequency no:")
                # print(list_automatic_freq_no)
                # print("bio frequency yes:")
                # print(list_automatic_freq_yes)

                screen_name = line[1]
                upper_letter_count = sum(1 for c in screen_name if c.isupper())
                # lowwer_letter_count = sum(1 for c in screen_name if c.islower())
                upper_ratio = upper_letter_count / len(screen_name)
                followers_count = line[5]
                friends_count = line[6]
                # bio_pronouns_count = bio_pronouns_count
                # bio_NNP_tags = self.func_tags_NNP(bio_tag_sequence)
                # bio_PRP_tags = self.func_tags_PRP(bio_tag_sequence)
                has_yes_words = self.bio_func_Yes_freq_terms(bio_text)
                # name_Yes_freq_terms = func_Yes_freq_terms(name_text)
                has_no_words = self.bio_func_No_freq_terms(bio_text)
                # name_No_freq_terms = func_No_freq_terms(name_text)
                bio_auto_Yes_freq_terms = self.automatic_freq_yes(bio_text, list_automatic_freq_yes)
                # name_auto_Yes_freq_terms = automatic_freq_yes(name_text, name_automatic_freq_yes)
                bio_auto_No_freq_terms = self.automatic_freq_no(bio_text, list_automatic_freq_no)
                # name_auto_No_freq_terms = automatic_freq_no(name_text, name_automatic_freq_no)
                class_type = line[0]
                the_vector = []
                the_vector = [screen_name, upper_letter_count,
                              upper_ratio,
                              followers_count, friends_count, bio_auto_Yes_freq_terms,
                              bio_auto_No_freq_terms, has_no_words,
                              has_yes_words, class_type]

                feature_writer.writerow(the_vector)

    ##################################################################
        outfile.close()
        print('<<<<<<<<<<<<<DONE>>>>>>>>>>>')


def main():
    extractor1 = feature_extractor('annotated_only.csv', 'less_features_train.csv')
    extractor1.extract()
    # extractor2 = feature_extractor('not_annotated.csv', 'less_features_test2.csv')
    # extractor2.extract()


if __name__ == "__main__":
    main()

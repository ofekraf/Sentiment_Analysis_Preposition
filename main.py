from analyzer import Analyzer
from parse import Parse
from termcolor import colored
from RUNNING_VARIABLES import *
import os

def main():
    if CLEAN_TWEETS:
        clean_tweets()

    if CLEAN_MOVIE_LINES:
        clean_movie_text_lines()

    if EXTRACT_PREPOSITION_SENTENCES:
        p = Parse(CHECKED_PREPOSITIONS, DELIMITER)
        p.extract_preposition_sentences()

    list_of_files = os.listdir("sentences")
    if RUN_ANALYSER:
        analyz = Analyzer(list_of_files)
        analyz.analyze()
        analyz.plot()
    else:
        print(colored("Warning: analyzer not run!", 'red'))

def clean_tweets():
    import string
    printable = set(string.printable)

    clean_tweets = []
    with open(os.path.join("data_to_clean",'tweets_cleaned.txt'),'r', encoding='utf8') as reader:
        for line in reader:
            clean_tweets.append(''.join(filter(lambda x: x in printable, line)).replace('\n',''))
    with open(os.path.join("data_to_clean",'tweets_cleaned_final'),'w') as writer:
        for line in clean_tweets:
            writer.write(line+"\n")


def clean_movie_text_lines():
    with open(os.path.join("data_to_clean",'movie_lines_cleaned'),'w') as writer:
        with open(os.path.join("data_to_clean",'movie_lines.txt'),'r') as reader:
            for line in reader:
                writer.write(line.split("+++$+++")[-1])

if __name__ == '__main__':
    main()


# todo: Flair
# todo - parsers: https://elitedatascience.com/python-nlp-libraries

# todo:
# https://github.com/niderhoff/nlp-datasets
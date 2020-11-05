from analyzer import Analyzer
from parse import Parse
from termcolor import colored
from RUNNING_VARIABLES import *

def main():
    list_of_files = None

    if CLEAN_TWEETS:
        clean_tweets()

    if CLEAN_MOVIE_LINES:
        clean_movie_text_lines()

    if EXTRACT_PREPOSITION_SENTENCES:
        p = Parse(CHECKED_PREPOSITIONS, DELIMITER)
        list_of_files = p.extract_preposition_sentences()
        with open("list_of_files", "w") as writer:
            writer.writelines(file + "\n" for file in list_of_files)

    if RUN_ANALYSER:
        if not list_of_files:
            list_of_files = get_list_of_files(list_of_files)
        analyz = Analyzer(list_of_files)
        analyz.analyze()
        analyz.plot()
    else:
        print(colored("Warning: analyzer not run!", 'red'))



def get_list_of_files(list_of_files):
    with open("list_of_files", "r") as reader:
        list_of_files = reader.readlines()
        list_of_files = [file[:file.index('\n')] if '\n' in file else file for
                         file in list_of_files]
    return list_of_files


def clean_tweets():
    import string
    printable = set(string.printable)

    clean_tweets = []
    with open('tweets_cleaned.txt','r', encoding='utf8') as reader:
        for line in reader:
            clean_tweets.append(''.join(filter(lambda x: x in printable, line)).replace('\n',''))
    with open('tweets_cleaned_final','w') as writer:
        for line in clean_tweets:
            writer.write(line+"\n")


def clean_movie_text_lines():
    with open('movie_lines_cleaned','w') as writer:
        with open('movie_lines.txt','r') as reader:
            for line in reader:
                writer.write(line.split("+++$+++")[-1])

if __name__ == '__main__':
    main()


# todo: Flair
# todo - parsers: https://elitedatascience.com/python-nlp-libraries

# todo:
# https://github.com/niderhoff/nlp-datasets
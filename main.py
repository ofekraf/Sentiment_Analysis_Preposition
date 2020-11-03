from analyzer import Analyzer
from parse import Parse

EXTRACT_PREPOSITION_SENTENCES = False
RUN_ANALYSIS = True
CLEAN_TWEETS = False
CLEAN_MOVIE_LINES = False
PRINT_LOGS = False


DELIMITER = "###---###"
CHECKED_PREPOSITIONS = ["but", "although", "however", "even though"]


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

    if RUN_ANALYSIS:
        if not list_of_files:
            list_of_files = get_list_of_files(list_of_files)
        analyz = Analyzer(list_of_files, DELIMITER, PRINT_LOGS)
        analyz.analyze()
        analyz.plot()


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
# sentences taken from:
# https://github.com/microsoft/ML-Server-Python-Samples/tree/master/microsoftml/202/data/sentiment_analysis
# http://www.cs.cornell.edu/~cristian/Cornell_Movie-Dialogs_Corpus.html

# https://raw.githubusercontent.com/sharmaroshan/Twitter-Sentiment-Analysis/master/test_tweets.csv
# https://raw.githubusercontent.com/sharmaroshan/Twitter-Sentiment-Analysis/master/train_tweet.csv
# out of these i only took tweets that :
#      1.did not contain '#' or '@'
#      2. contained only utf8 characters (mainly, no emojis)
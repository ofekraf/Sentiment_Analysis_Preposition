from analyzer import Analyzer
from parse import Parse

EXTRACT_PREPOSITION_SENTENCES = True
RUN_ANALYSIS = True
DELIMITER = "###---###"
CHECKED_PREPOSITIONS = ["but", "although", "however"]


def main():
    list_of_files = None
    if EXTRACT_PREPOSITION_SENTENCES:
        p = Parse(CHECKED_PREPOSITIONS, DELIMITER)
        list_of_files = p.extract_preposition_sentences()
        with open("list_of_files", "w") as writer:
            writer.writelines(file + "\n" for file in list_of_files)

    if RUN_ANALYSIS:
        if not list_of_files:
            list_of_files = get_list_of_files(list_of_files)
        analyz = Analyzer(list_of_files, DELIMITER)
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

if __name__ == '__main__':
    main()
    # clean_tweets()

# sentences taken from:
# https://github.com/microsoft/ML-Server-Python-Samples/tree/master/microsoftml/202/data/sentiment_analysis

# https://raw.githubusercontent.com/sharmaroshan/Twitter-Sentiment-Analysis/master/test_tweets.csv
# https://raw.githubusercontent.com/sharmaroshan/Twitter-Sentiment-Analysis/master/train_tweet.csv
# out of these i only took tweets that :
#      1.did not contain '#' or '@'
#      2. contained only utf8 characters (mainly, no emojis)
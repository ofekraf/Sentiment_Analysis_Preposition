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


if __name__ == '__main__':
    main()


# sentences taken from:
# https://github.com/microsoft/ML-Server-Python-Samples/tree/master/microsoftml/202/data/sentiment_analysis
# https://raw.githubusercontent.com/sharmaroshan/Twitter-Sentiment-Analysis/master/test_tweets.csv
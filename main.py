from parse import Parse

EXTRACT_PREPOSITION_SENTENCES = True
RUN_ANALYSIS = False

CHECKED_PREPOSITIONS = ["but", "although", "though"]


# todo - colab link: https://colab.research.google.com/drive/1y1nkiZiWFwi4cpMftaXuTVOwAE9NKVOP#scrollTo=UqUcKkH7N_oN
# todo - https://github.com/ofekraf/Sentiment_Analysis_Preposition
def main():
    if EXTRACT_PREPOSITION_SENTENCES:
        p = Parse(CHECKED_PREPOSITIONS)
        list_of_files = p.extract_preposition_sentences()

    # if RUN_ANALYSIS:
    #     analyz = analyzer.Analyzer(list_of_files)
    #     analyz.Analyzer.analyze()


# todo - parsers:
# https://elitedatascience.com/python-nlp-libraries






if __name__ == '__main__':
    main()

import nltk
from google.cloud import language_v1

import matplotlib.pyplot as plt

# todo: Flair
# todo - parsers: https://elitedatascience.com/python-nlp-libraries

FIRST_TIME = False


class Analyzer:
    FUNCTION_POS = 0
    KWD_POS = 1
    STRETCHING_FUNC = 2

    def __init__(self, list_of_files, delimiter):
        self.list_of_files = list_of_files
        self.delimiter = delimiter
        self.sentiment_modules = {}
        self.initialize_modules()
        self.coords = {}
        self._analysis_done = False

    @classmethod
    def _get_sid(cls):
        if FIRST_TIME:
            nltk.download('vader_lexicon')
        from nltk.sentiment.vader import SentimentIntensityAnalyzer
        return SentimentIntensityAnalyzer()

    @classmethod
    def clean(self, word):
        if not word:
            return word  # nothing to strip
        for start, c in enumerate(word):
            if c.isalnum():
                break
        for end, c in enumerate(word[::-1]):
            if c.isalnum():
                break
        return word[start:len(word) - end] + "."

    def plot(self):
        if not self._analysis_done:
            print("Warning! you must first analyze before plotting! ")
            return

        self.list_of_files = ["but_sentences", "however_sentences"]

        fig, all_plots = plt.subplots(len(self.list_of_files),
                                      len(self.sentiment_modules))

        # all_plots[0, 0].set_title('Axis [0,0]') #todo
        # all_plots[0, 1].plot(x, y, 'tab:orange')
        # all_plots[0, 1].set_title('Axis [0,1]')

        for mod_idx, module in enumerate(self.sentiment_modules):
            all_plots[0, mod_idx].set_title(module)
            for prop_idx, file_name in enumerate(self.list_of_files):
                all_plots[mod_idx, prop_idx].scatter(
                    self.coords[file_name][module][0],
                    self.coords[file_name][module][1])
                all_plots[mod_idx, prop_idx].grid()
                all_plots[mod_idx, prop_idx].axis(xmin=-5, xmax=5,
                                                  ymin=-5, ymax=5)
                all_plots[mod_idx, 0].set_ylabel(file_name.split("_")[0])
                all_plots[mod_idx, 0].yaxis.set_label_position("left")

        fig.show()

    def analyze(self):
        self.list_of_files = ["but_sentences", "however_sentences"]  # todo
        for file in self.list_of_files:
            self.coords[file] = {n: ([], []) for n in
                                 self.sentiment_modules.keys()}
            try:
                with open(file, 'r') as reader:
                    for line in reader:
                        first, sec = line.split(self.delimiter)

                        first = self.clean(first)
                        sec = self.clean(sec)
                        for mod_name, module in self.sentiment_modules.items():
                            self.coords[file][mod_name][0].append(
                                self.calc_score(module, first))
                            self.coords[file][mod_name][1].append(
                                self.calc_score(module, sec))
            except ValueError as e:
                print("line is :" + line)
                raise e
        self._analysis_done = True

    @classmethod
    def calc_score(self, module, sentence):
        return module[self.STRETCHING_FUNC](
            module[self.FUNCTION_POS](sentence)[module[self.KWD_POS]])

    def initialize_modules(self):
        nltk_vader = self._get_sid()
        self.sentiment_modules["nltk"] = (
            nltk_vader.polarity_scores, 'compound', lambda x: x * 5)

        from textblob import TextBlob
        self.sentiment_modules["TextBlob"] = (
            lambda x: TextBlob(x).sentiment, 0, lambda x: x * 5)

        # client = language_v1.LanguageServiceClient()
        # self.sentiment_modules["googleCloud"] =
        # sentiment = client.analyze_sentiment(
        #     request={'document': document}).document_sentiment

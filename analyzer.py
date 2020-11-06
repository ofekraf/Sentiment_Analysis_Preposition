import nltk
import stanza
import matplotlib.pyplot as plt
import json
import os
import string
from RUNNING_VARIABLES import *

FIRST_TIME = False


class Analyzer:
    FUNCTION_POS = 0
    KWD_POS = 1
    STRETCHING_FUNC = 2

    def __init__(self, list_of_files):
        self._print_log("starting Analyzer initialization")
        self.list_of_files = list_of_files
        self.sentiment_modules = {}
        self.initialize_modules()
        self.coords = {}
        self._analysis_done = False
        self._print_log("finished Analyzer initialization")

    def _print_log(self, msg):
        if PRINT_LOGS:
            print(msg)

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

        self._print_log("starting plotting")

        fig, all_plots = plt.subplots(len(self.list_of_files),
                                      len(self.sentiment_modules))

        colors = ['red', 'blue', 'green', 'purple']
        for mod_idx, module in enumerate(self.sentiment_modules):
            all_plots[0, mod_idx].set_title(module)
            for prop_idx, file_name in enumerate(self.list_of_files):
                all_plots[prop_idx, mod_idx].scatter(
                    self.coords[file_name][module][0],
                    self.coords[file_name][module][1],
                    color=colors[prop_idx % len(colors)])
                all_plots[prop_idx, mod_idx].grid()
                all_plots[prop_idx, mod_idx].axis(xmin=-5, xmax=5,
                                                  ymin=-5, ymax=5)
                all_plots[prop_idx, 0].set_ylabel(string.capwords(file_name.split("_")[0]))
                all_plots[prop_idx, 0].yaxis.set_label_position("left")

        fig.suptitle(
            "Sentiment of first vs second part of sentences, parted  by Prepositiosn")
        fig.show()
        if UPDATE_SHOWN_IMAGE:
            fig.savefig('preposition_Sentiment_graphs.png')
        self._print_log("finised plotting")

    def analyze(self):
        self._print_log("starting analyzing")
        if not ANALYZE_DATA_FROM_SCRATCH:
            self.load_coords()
            self._analysis_done = True
            self._print_log("finished analyzing")
            return
        for file in self.list_of_files:
            self.coords[file] = {n: ([], [], []) for n in
                                 self.sentiment_modules.keys()}
            self.iterate_file_sentiment(file)
            with open(os.path.join("sentiments", file + '_sentiments.json'),
                      'w') as f:
                json.dump(self.coords[file], f)
        self._analysis_done = True
        self._print_log("finished analyzing")

    def iterate_file_sentiment(self, file):
        with open(os.path.join("sentences", file), 'r') as reader:
            for line in reader:
                first, sec = line.split(DELIMITER)

                first = self.clean(first)
                sec = self.clean(sec)
                sentence = " ".join([first, file.split("_")[0], sec])
                for mod_name, module in self.sentiment_modules.items():
                    self.coords[file][mod_name][0].append(
                        self.calc_score(module, first))
                    self.coords[file][mod_name][1].append(
                        self.calc_score(module, sec))
                    self.coords[file][mod_name][2].append(sentence)

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

        nlp = stanza.Pipeline(lang='en', processors='tokenize,sentiment')
        self.sentiment_modules["stanza"] = (
            lambda x: {'s': nlp(x).sentences[0].sentiment}, 's',
            stanza_normalizer
        )

    def load_coords(self):
        for file in self.list_of_files:
            self.coords[file] = self.get_coords_file(file)

    @staticmethod
    def get_coords_file(file):
        with open(os.path.join("sentiments",file + '_sentiments.json')) as json_file:
            return json.load(json_file)


def stanza_normalizer(sentiment):
    # negative: 0
    # neutral: 1
    # positive: 2
    switcher = {0: -3, 1: 0, 2: 3}
    return switcher[sentiment]

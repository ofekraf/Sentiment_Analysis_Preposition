import nltk
import matplotlib.pyplot as plt

# todo: Flair, Textblob
# todo - parsers: https://elitedatascience.com/python-nlp-libraries

class Analyzer:
    FUNCTION_POS = 0
    KWD_POS = 1

    def __init__(self, list_of_files, delimiter):
        self.list_of_files = list_of_files
        self.delimiter = delimiter
        self.sentiment_modules = {}
        self.initialize_modules()
        self.coords = {}
        self._analysis_done = False

    @classmethod
    def _get_sid(cls):
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
        # todo - plot


    def analyze(self):
        # for file in self.list_of_files:
        file = "however_sentences"
        self.coords[file] = ([], [])
        with open(file, 'r') as reader:
            for line in reader:
                first, sec = line.split(self.delimiter)

                first = self.clean(first)
                sec = self.clean(sec)
                #   print("first: " + first + " || sec: "+ sec)
                for _, module in self.sentiment_modules.items():
                    self.coords[file][0].append(self.calc_score(module, first))
                    self.coords[file][1].append(self.calc_score(module, sec))
        self._analysis_done = True

    @classmethod
    def calc_score(self, module, sentence):
        return module[self.FUNCTION_POS](sentence)[module[self.KWD_POS]]

    def initialize_modules(self):
        nltk_vader = self._get_sid()
        self.sentiment_modules[nltk_vader] = (
        nltk_vader.polarity_scores, 'compound')

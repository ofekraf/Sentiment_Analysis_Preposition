import nltk
import matplotlib.pyplot as plt
# todo: Flair, Textblob
# todo - parsers: https://elitedatascience.com/python-nlp-libraries

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

        print("starting plotting")

        self.list_of_files = ["but_sentences", "however_sentences"]

        fig, all_plots = plt.subplots(len(self.list_of_files), len(self.sentiment_modules))
        x = [1,2,3]
        y = [1,2,3]
        all_plots[0, 0].plot(x, y)
        all_plots[0, 0].set_title('Axis [0,0]')
        all_plots[0, 1].plot(x, y, 'tab:orange')
        all_plots[0, 1].set_title('Axis [0,1]')
        # for mod_idx, module in enumerate(self.sentiment_modules):
        #     for prop_idx, file_name in enumerate(self.list_of_files):
        #         all_plots[mod_idx][prop_idx]

        fig.show()


    def analyze(self):
        # for file in self.list_of_files:
        file = "but_sentences" #todo
        self.coords[file] = ([], [])
        with open(file, 'r') as reader:
            for line in reader:
                first, sec = line.split(self.delimiter)

                first = self.clean(first)
                sec = self.clean(sec)
                for _, module in self.sentiment_modules.items():
                    self.coords[file][0].append(self.calc_score(module, first))
                    self.coords[file][1].append(self.calc_score(module, sec))
        self._analysis_done = True

    @classmethod
    def calc_score(self, module, sentence):
        return module[self.STRETCHING_FUNC](module[self.FUNCTION_POS](sentence)[module[self.KWD_POS]])

    def initialize_modules(self):
        nltk_vader = self._get_sid()
        self.sentiment_modules[nltk_vader] = (
        nltk_vader.polarity_scores, 'compound', lambda x: x*5)

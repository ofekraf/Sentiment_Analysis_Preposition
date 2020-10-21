import nltk

# todo: Flair, Textblob
# todo - colab link: https://colab.research.google.com/drive/1y1nkiZiWFwi4cpMftaXuTVOwAE9NKVOP#scrollTo=UqUcKkH7N_oN
class Analyzer:

    def __init__(self, list_of_files, delimiter):
        self.list_of_files = list_of_files
        self.delimiter = delimiter

    @classmethod
    def _get_sid(cls):
        nltk.download('vader_lexicon')
        from nltk.sentiment.vader import SentimentIntensityAnalyzer
        return SentimentIntensityAnalyzer()


    def analyze(self):
        nltk_vader = self._get_sid()

        # for file in self.list_of_files:
        file = "however_sentences"
        with open(file,'r') as reader:
            for line in reader:
                print(line.split(self.delimiter))
                print(nltk_vader.polarity_scores(line))
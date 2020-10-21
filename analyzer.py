import nltk

# todo: Flair, Textblob
# todo - colab link: https://colab.research.google.com/drive/1y1nkiZiWFwi4cpMftaXuTVOwAE9NKVOP#scrollTo=UqUcKkH7N_oN
class Analyzer:

    def __init__(self, list_of_files):
        self.list_of_files = list_of_files

    @classmethod
    def _get_sid(cls):
        nltk.download('vader_lexicon')
        from nltk.sentiment.vader import SentimentIntensityAnalyzer
        return SentimentIntensityAnalyzer()


    def analyze(self):
        nltk_vader = self._get_sid()

        # for file in self.list_of_files:
        file = "though_sentences"
        with open(file ,'r') as reader:
            for sentence in reader:
                analysis.append(nltk_vader.polarity_scores(sentence))
            print(analysis)
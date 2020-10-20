import nltk
from textblob import TextBlob

# todo: Flair, Textblob



def


def get_sid():
    nltk.download('vader_lexicon')
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    return SentimentIntensityAnalyzer()

def main():
    nltk_vader = get_sid()
    sentences = ["this is a good sentence", "this is a bad sentence"]

    analysis = []
    for sentence in sentences:
        analysis.append(nltk_vader.polarity_scores(sentence))
    print(analysis)

if __name__ == '__main__':
    main()



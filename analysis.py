import nltk
from textblob import TextBlob

EXTRACT_PREPOSITION_SENTENCES = False
RUN_ANALYSIS = False
CHECKED_PREPOSITIONS = ["but", "although", "though"]


# todo: Flair, Textblob


def get_sid():
    nltk.download('vader_lexicon')
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    return SentimentIntensityAnalyzer()


def get_substring_propositions():
    substrings = []
    for prop in CHECKED_PREPOSITIONS:
        substrings.append(" " + prop + " ")
        substrings.append("," + prop + " ")
        substrings.append(" " + prop + ",")
        substrings.append("," + prop + ",")
        substrings.append("." + prop + " ")
    return substrings


def extract_preposition_sentences():
    preposition_split_sentences = {prep: [] for prep in CHECKED_PREPOSITIONS}
    parse_raw_sentences(preposition_split_sentences)

    for prep in preposition_split_sentences:
        with open(prep + "_sentences", 'w') as writer:
            for tup in preposition_split_sentences[prep]:
                writer.write(str(tup) + "\n")


def parse_raw_sentences(preposition_split_sentences):
    with open("RAW_SENTENCES", 'r') as reader:
        lines = reader.readlines()
        for line in lines:
            if '\t' in line:
                line = line[:line.index('\t')]
            for preposition in get_substring_propositions():
                if preposition in line.lower():
                    splited_line = tuple(line.split(preposition))
                    if len(splited_line) > 2:
                        print(line)
                        continue
                        # in the corpus of 3000 sentences, this has not occured once:
                    preposition_split_sentences[preposition[1:-1]].append(
                        splited_line)


def main():
    if EXTRACT_PREPOSITION_SENTENCES:
        extract_preposition_sentences()

    if RUN_ANALYSIS:
        nltk_vader = get_sid()
        sentences = ["this is a good sentence", "this is a bad sentence"]

        analysis = []
        for sentence in sentences:
            analysis.append(nltk_vader.polarity_scores(sentence))
        print(analysis)


if __name__ == '__main__':
    main()

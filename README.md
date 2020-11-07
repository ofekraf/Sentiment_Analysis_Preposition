# Sentiment_Analysis_Preposition
This project aims to use Sentiment analysis tools to gain perspective on the meaning of prepositions in the English language. 

## Sentiment Analysis Models used
for ease of reading, every sentiment module's returned values have been 
strecthed to scale between -5 (negative) and 5 (positive).  
To date (05/11/20) three (pre-trained) sentiment analysis models have been used:
-	[nltk_vader](https://www.nltk.org/_modules/nltk/sentiment/vader.html)
    - taking the "compound" as an aggregated sentiment. 
-	[Textblob](https://textblob.readthedocs.io/en/dev/quickstart.html#sentiment-analysis)
    - taking the "polarity" attribute.
-	[stanza](https://stanfordnlp.github.io/stanza/sentiment.html) 
    - note this only returns one of three values (mainly: positive, negative or neutral)
    this is why only 10 dots on the graph can be scaled. for ease of reading, 
    any positive sentences were given the value 3, any negative sentences were given the value (-3), 
    and any neutral sentences were given the value 0. 

##  Raw text sentences origin
To date (05/11/20) the sentences for the text analysis have been taken from the following sources: 
-	[Amazon, IMDB, yelp reviews](https://github.com/microsoft/ML-Server-PythonSamples/tree/master/microsoftml/202/data/sentiment_analysis) 
-	[Movie scripts](http://www.cs.cornell.edu/~cristian/Cornell_Movie-Dialogs_Corpus.html) 
-	[Tweets source 1](https://raw.githubusercontent.com/sharmaroshan/Twitter-Sentiment-Analysis/master/test_tweets.csv) 
-	[Tweets source 2](https://raw.githubusercontent.com/sharmaroshan/Twitter-Sentiment-Analysis/master/train_tweet.csv) 

from the tweets dataset, I only took tweets that followed these two criteria: 
1	.the tweet did not contain '#' or '@'
2.	The tweet contained only utf8 characters (mainly, no emojis)

## Graphs
###General picture
![Image of all graphs](preposition_Sentiment_graphs.png?raw=true "Image of all graphs")

For an interactive map to the graph above, please click [here](preposition_Sentiment_graphs.html?raw=true "interactive graph")


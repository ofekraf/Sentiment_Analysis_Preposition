# Preposition Meanings using Sentiment Analysis tools
This project aims to use Sentiment analysis tools to gain insight and perspective on the meaning (or at least use) of prepositions in the English language. 

##Introduction
Natural language processing (NLP) is a subfield of linguistics, computer science, and artificial intelligence concerned with the interactions between computers and human language.

The majority of studies to this date have used linguistics tools to pursue the study of computer science, that is to say: develop smarter computers, able to interact better with humans.

A minority of studies aim to do he opposite: use computers to better study how humans interact with themselves. This humble project aims to do so.   
###Goals of this project
A preposition is a word used to link nouns, pronouns, or phrases to other words within a sentence. Many such words exist 



Some prefer the use of the word 'conjunction' to  describe the  connection of two  clauses, though to avoid the confusion with the boolean meaning, i will stick to the  terminology of prepositions.


###Prepositions in Natural language

###

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

##notes about coding edge cases
1. Splitting the sentences, i only used sentences that had 2 or more words in every clause. Words here are defined as characters split by a space character - " ". 
2. some prepositions are much more common then others in the text corpora i've used. as such, i've limited the amount of points to be shown in the graph,   

## Graphs
![Image of all graphs](preposition_Sentiment_graphs.png?raw=true "Image of all graphs")

an interactive map to the graph above: please click [here](https://htmlpreview.github.io/?https://github.com/ofekraf/Sentiment_Analysis_Preposition/blob/master/preposition_Sentiment_graphs.html)
![](./preposition_Sentiment_graphs.html)

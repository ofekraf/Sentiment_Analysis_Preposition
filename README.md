# Preposition Meanings using Sentiment Analysis tools
This project aims to use Sentiment analysis tools to gain insight and perspective 
on the meaning (or at least use) of prepositions in the English language. 

<!--TBD-->
<!---
## Table of contents
- [Introduction](##introduction)
    * [Prepositions](###prepositions)
    * [Goals](###goals)
        - [Examples](####Examples)
- [Method](##Method)
    * [TL;DR](###TL;DR)
    * [Sentiment Analysis: a (very) brief overview](###Sentiment Analysis overview) 
    * [Sentiment Analysis Models](###Sentiment Analysis Models)
    * [Raw text origin](###Raw text origin)
    * [Edge cases](###Edge cases)
    * [Graph Expectations](###Edge cases)
- [Results](##Results) 
    * [Graphs](###Graphs)
- [Discussion](###Discussion)
- [Contact details](##Contact details)
--->

## Introduction
Natural language processing (NLP) is a subfield of linguistics, computer science, 
and artificial intelligence concerned with the interactions between computers 
and human language.

The majority of academic studies regarding NLP to this date have used linguistics 
tools to pursue the study of computer science, that is to say: develop smarter 
computers, able to interact better with humans.

A minority of studies aim to do the opposite: Use computers to better study 
how humans interact with themselves. This humble project aims to do so.   

### Prepositions
A preposition is a word used to link nouns, pronouns, or phrases to other words 
within a sentence. The english language has a lot of prepositions, for example: 
"both", "and", "neither" and so on.

Some prefer the use of the word 'conjunction' to  describe the  connection of 
two  clauses, though to avoid the confusion with the boolean meaning, I will 
stick to the  terminology of prepositions.

### Goals
Here, I aimed to empirically look at a specific subsection of prepositions: 
preposition that (at least intuitively) denote a contradiction of sorts. 


#### Examples
1. "I like apples, but this apple is rotten"
2. "Github is horribly unintuitive, however it is a wonderful platform"

In these two sentences, the words "but" and "however" respectively serve as 
contradicting prepositions. 
In the first sentence, the preamble 'I like apples' denotes a positive attitude 
towards apples, while the latter clause 'this apple is rotten' denotes a 
negative attitude towards a specific apple.      

This study aimes to examine the assumption that such prepositions do indeed 
denote a contradiction between the two parts of a sentence. 

## Method

### TL;DR 
Using Sentiment analysis models, I compared the sentiment of the first clause 
of a sentence, up to but not including the preposition (henceforth - "prefix"),
 and the sentiment of the latter part of the clause (henceforth - "suffix"). 
 Plotting both sentiment scores, over different prepositions and different 
 pre-trained sentiment analysis models, I plotted the
  [graph below](###Graphs). In it, the x axis represents the sentiment value 
  for the prefix of the clause, and the y axis represents the sentiment value 
  for the suffix of the clause. positive and negative values represent 
  positive and negative sentiments correspondingly.  

### Sentiment Analysis overview
Sentiment analysis is a use of natural language processing tools for text 
analysis. in particular it aims to extract, quantify, and study affective 
states and subjective information. 
Sentiment analysis is widely applied to voice of the customer materials such 
as reviews and survey responses, online and social media, and health care
materials for applications that range from marketing to customer service to 
clinical medicine.

In this study, all Sentiment analysis tools that have been used point to 
either a positive sentiment, 
or a negative one. some of the tools quantify just how "positive" negative 
the sentiment is, assigning it a numerical number. For the ease of the reader, 
I have normalized all analysis to point to the same numerical range: 
from -5 to 5, -5 being the most negative sentiment, and 5 being the most 
positive.

Most Sentiment analysis tools (among them all the tools used here) use Machine 
learning techniques to assign their values. following is a briefs description 
of how such techniques work:
First, a large corpora of text is manually tagged. usually on a sentence 
level, for positive or negative sentences. this large chunk of text is divided
into a training set, and a test set. from both, different features are 
extracted. such features may include the existence or absence of certain
words, certain grammatical structures, the presence of negation and  its
scope and so on. 
These in turn help the machine learning algorithm to associate different 
features with different positive\negative tags.
after converging on a suitable function representation for the training set, 
this function is tested on the test set. 

This short depiction of Current day Sentiment analysis is important for 
(at least) the following exclaimers:

1. Sentiment analysis models Tend to be domain specific. that is to say, 
they relay heavily on the textual domain on which they were trained. 
A sentiment analysis model that has been trained on product reviews is not 
expected to have good results on quotes from movies. 
Note I aimed to handle this by using multiple different models, trained on 
different corpora, more on this below.
    - Nltk  & Textblob - on social media 
    - Stanza - on [Universal dependency](https://universaldependencies.org/) 
    dataset which includes both Wikipedia articles and news media

2. NLP in general, and sentiment analysis in particular still face numerous 
challenges: identifying sarcasm and Cynicism, refining negation scope, 
extending modules to unrecognized domains, and so on. 
Even with these out of the way - human manual taggers usually only agree on 
approximately 80% of sentences. all the models below score around 70% accuracy. 
[[1](https://towardsdatascience.com/basic-binary-sentiment-analysis-using-nltk-c94ba17ae386)]
[[2](https://stanfordnlp.github.io/stanza/sentiment.html#available-models)]  

### Sentiment Analysis Models
For ease of reading, every sentiment module's returned values have been 
strecthed to scale between -5 (negative) and 5 (positive).  
To date (05/11/20) three (pre-trained) sentiment analysis models have been used:
-	[nltk_vader](https://www.nltk.org/_modules/nltk/sentiment/vader.html)
    - taking the "compound" as an aggregated sentiment. 
-	[Textblob](https://textblob.readthedocs.io/en/dev/quickstart.html#sentiment-analysis)
    - taking the "polarity" attribute.
-	[stanza](https://stanfordnlp.github.io/stanza/sentiment.html) 
    - note this only returns one of three values (mainly: positive, negative 
    or neutral). This is why only 10 dots on the graph can be scaled. For ease 
    of reading, any positive sentences were given the value 3, any negative 
    sentences were given the value (-3), and any neutral sentences were given 
    the value 0. 

### Raw text origin
To date (05/11/20) the sentences for the text analysis have been taken from 
the following sources: 
-	[Amazon, IMDB, yelp reviews](https://github.com/microsoft/ML-Server-PythonSamples/tree/master/microsoftml/202/data/sentiment_analysis) 
-	[Movie scripts](http://www.cs.cornell.edu/~cristian/Cornell_Movie-Dialogs_Corpus.html) 
-	[Tweets source 1](https://raw.githubusercontent.com/sharmaroshan/Twitter-Sentiment-Analysis/master/test_tweets.csv) 
-	[Tweets source 2](https://raw.githubusercontent.com/sharmaroshan/Twitter-Sentiment-Analysis/master/train_tweet.csv) 

From the tweets dataset, I only took tweets that followed these two criteria: 

1.	The tweet did not contain '#' or '@'.
2.	The tweet contained only utf8 characters (mainly, no emojis)

### Edge cases
1. Splitting the sentences, I only kept sentences that had 2 or more words in 
every clause. Words here are defined as characters split by a space 
character - " ". 

2. Some prepositions are much more common then others in the text corpora 
i've used. as such, i've limited the amount of points to be shown in the graph
 for those.

3. Any excluded sentence from the RAW_DATA can be seen in 
discarded_lines.log. Exclusion reasons can be any of the following:
    1. A line containing multiple occurrences of the same preposition
    2. A line that does not contain two words on either clause divided by a 
        preposition (for example: "Although, i'm happy")

### Graph Expectations
Under the assumptions above, shortly repeated here for brevity:
1. The checked prepositions indeed hold that 'prefix preposition B' 
denotes that prefix and suffix are (somewhat) opposites. 
2. reducing a clauses's meaning down to it's sentiment still holds a major 
part of it's 'meaning'.

I would expect to see points mostly (or even only) in the second and fourth 
quadrant. That is to say: one would expect to only see points that represent 
a 'reversal' of meaning (again, in sentiment terms). That is to say, I would 
expect that if the sentiment of the prefix was positive (ie, would receive 
a positive sentiment score), it's suffix would be negative (receive a negative 
score). this case would yield a point (representing the sentence's two scores)
in the second quadrant. A similar case with opposite sentiments (prefix 
receiving a negative score, and a suffix with a negative one).

In the [example section](####Examples) above, the first sentence would be expected to yield a 
point in the fourth quadrant, while the second sentence would yield a point in 
the fourth quadrant.

## Results 

### Graphs
![Image of all graphs](plots/preposition_Sentiment_graphs.png?raw=true "Image of all graphs")

an interactive map to the graph above: 
please click [here](https://htmlpreview.github.io/?https://github.com/ofekraf/Sentiment_Analysis_Preposition/blob/master/plots/preposition_Sentiment_graphs.html)

for in-depth interactive maps please see below:

#### although

- [although_nltk](https://htmlpreview.github.io/?https://github.com/ofekraf/Sentiment_Analysis_Preposition/blob/master/plots/although/although_nltk.html)
- [although_TextBlob](https://htmlpreview.github.io/?https://github.com/ofekraf/Sentiment_Analysis_Preposition/blob/master/plots/although/although_TextBlob.html)
- [although_stanza](https://htmlpreview.github.io/?https://github.com/ofekraf/Sentiment_Analysis_Preposition/blob/master/plots/although/although_stanza.html)

#### and yet

- [and_yet_nltk](https://htmlpreview.github.io/?https://github.com/ofekraf/Sentiment_Analysis_Preposition/blob/master/plots/and_yet/and_yet_nltk.html)
- [and_yet_TextBlob](https://htmlpreview.github.io/?https://github.com/ofekraf/Sentiment_Analysis_Preposition/blob/master/plots/and_yet/and_yet_TextBlob.html)
- [and_yet_stanza](https://htmlpreview.github.io/?https://github.com/ofekraf/Sentiment_Analysis_Preposition/blob/master/plots/and_yet/and_yet_stanza.html)

#### but

- [but_nltk](https://htmlpreview.github.io/?https://github.com/ofekraf/Sentiment_Analysis_Preposition/blob/master/plots/but/but_nltk.html)
- [but_TextBlob](https://htmlpreview.github.io/?https://github.com/ofekraf/Sentiment_Analysis_Preposition/blob/master/plots/but/but_TextBlob.html)
- [but_stanza](https://htmlpreview.github.io/?https://github.com/ofekraf/Sentiment_Analysis_Preposition/blob/master/plots/but/but_stanza.html)

#### even though

- [even_though_nltk](https://htmlpreview.github.io/?https://github.com/ofekraf/Sentiment_Analysis_Preposition/blob/master/plots/even_though/even_though_nltk.html)
- [even_though_TextBlob](https://htmlpreview.github.io/?https://github.com/ofekraf/Sentiment_Analysis_Preposition/blob/master/plots/even_though/even_though_TextBlob.html)
- [even_though_stanza](https://htmlpreview.github.io/?https://github.com/ofekraf/Sentiment_Analysis_Preposition/blob/master/plots/even_though/even_though_stanza.html)

#### however

- [however_nltk](https://htmlpreview.github.io/?https://github.com/ofekraf/Sentiment_Analysis_Preposition/blob/master/plots/however/however_nltk.html)
- [however_TextBlob](https://htmlpreview.github.io/?https://github.com/ofekraf/Sentiment_Analysis_Preposition/blob/master/plots/however/however_TextBlob.html)
- [however_stanza](https://htmlpreview.github.io/?https://github.com/ofekraf/Sentiment_Analysis_Preposition/blob/master/plots/however/however_stanza.html)

#### therefore

- [therefore_nltk](https://htmlpreview.github.io/?https://github.com/ofekraf/Sentiment_Analysis_Preposition/blob/master/plots/therefore/therefore_nltk.html)
- [therefore_TextBlob](https://htmlpreview.github.io/?https://github.com/ofekraf/Sentiment_Analysis_Preposition/blob/master/plots/therefore/therefore_TextBlob.html)
- [therefore_stanza](https://htmlpreview.github.io/?https://github.com/ofekraf/Sentiment_Analysis_Preposition/blob/master/plots/therefore/therefore_stanza.html)

## Discussion
<!--TBD-->

Before diving in, let us look at a couple of examples from each quadrant, for 
each analyzed preposition:

#### although
| module \ quadrant  | 1st | 2nd |3rd | 4th |
| -------------------| ---|---|---|---|
| Nltk |   |
| Textblob  |   |
| stanza  |   |   

#### and yet

#### but

#### even though

#### however

#### therefore


## Contact details

I am more than happy to discuss this project, feel free to contact me at:
ofek.rafaeli at mail.huji.ac.il

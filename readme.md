### Idea
Scape the news articles related to markets and bussinesses across the globe. Using this news data find the sentiments in the news.
These sentiments can be used to predict the bussinesses growth.

Problem Statment:
1) Scrap the website containing market news such as change in share price, dealing among companys
2) Extract the sentiment and summary from the extracted news articles using NLP models


### Business Case
There is lots of text data and information present on the internet and it becomes extremely difficult to read and infer the context manually. There are many organizations working in the field of share markets which can use this data to predict change in shares. 

### Data Scraping
We can download the data from this website 
We can go on to other links present in the news articles

Stpes for Language modelling
1) Preprocess the text data(lower case, stop words and other irrelevant words removal, tokenize, word embeddings and positional encoding of tokens)
2) Prepare target sentiments either manually or training the model on existing corpora
3) Train the attention based models (LSTMS, Transformers)
4) Validate the model based on metrics such as BLEU scores
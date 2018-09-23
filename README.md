# Twitter Sentiment Analysis
I scraped tweets containing five Emojis using Twitter API, labeled the tweet texts with the corresponding emojis and then removed the emojis from the texts. Cleaned the texts with python regular expression and converted the data into pandas dataframe. Created a balanced dataset through downsampling. Trained machine learning and deep learning models including KNN, Naive Bayes, SVM, LSTM to predict the emoji given the tweet text. 

## Tools:
- [Tweepy](https://tweepy.readthedocs.io/en/v3.5.0/)
- python regex
- pandas
- matplotlib
- scikit-learn
- keras

## Results:
The baseline accuracy is 20%. The accuracy of SVM reaches ~50%

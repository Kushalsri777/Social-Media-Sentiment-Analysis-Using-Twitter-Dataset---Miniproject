# Social-Media-Sentiment-Analysis-Using-Twitter-Dataset---Miniproject

**Summary**
- Got a Twitter dataset from Kaggle
- Cleaned the data
- Splitted the training and the test data
- Vectorized the tweets using the CountVectorizer library
- Built a model using different algorithms
- Achieved a good accuracy and integrated the model to a static website to input tweets for sentiment analysis 

-------------------------------------------------------------------------------------------------------

**Data Collection**

- Link to the dataset: https://www.kaggle.com/arkhoshghalb/twitter-sentiment-analysis-hatred-speech

Understanding the dataset
 - Let's read the context of the dataset to understand the problem statement. 
 - In the training data, tweets are labeled '0' if they are associated with a positive sentiment. Otherwise, tweets are labeled '1' for a negative sentiment. 

**Data Exploration**
- This is how the training and testing data looks like.
![Screenshot (406)](https://user-images.githubusercontent.com/69420616/123615268-c1fcf400-d822-11eb-8270-40883aef3736.png)
- We have to clean the special characters from the dataset, like @, #, !, and etc. We will remove these characters later in the data cleaning step.

**Data Cleaning**
 - We remove the unwanted stopwords
 ![Screenshot (407)](https://user-images.githubusercontent.com/69420616/123616197-a9d9a480-d823-11eb-9de1-434515c04a7e.png)

**Vectorize Tweets using CountVectorizer**
- Now, we will convert text into numeric form as our model won't be able to understand the human language. We will vectorize the tweets using CountVectorizer. CountVectorizer provides a simple way to both tokenize a collection of text documents and build a vocabulary of known words. 

![Screenshot (408)](https://user-images.githubusercontent.com/69420616/123616579-0dfc6880-d824-11eb-8ba8-c0b34d60b72f.png)

**Train and Test Splitting**
- Now that we have cleaned our data, we will do the test and train split using the train_test_split function.
- We will use 75% of the data as the training data and the remaining 25% as the test data.

**Model Building**
- Now that we have vectorized all the tweets, we will build a model to classify the test data. 
- We will use the supervised learning algorithms, Random Forest Classifier, Logistic Regression, Decision Tree Classifier, Support Vector Classifier and XG Boost Classifier.
- We see that the Random Forest gives the best accuracy.
![Screenshot (409)](https://user-images.githubusercontent.com/69420616/123617483-eb1e8400-d824-11eb-8aa7-cafef0641bb1.png)


**Creating a pickle file to dump the model**
![Screenshot (410)](https://user-images.githubusercontent.com/69420616/123617815-43558600-d825-11eb-80fc-d4bfb068decd.png)


**Testing the model with tweets inputs**
- Now that we have dumped the model using pickle, i have created HTML page for tweet input.
- When we enter a positive tweet, a page opens up showing that the tweet has a positive sentiment.
- And when we enter a negative tweet, a page opens up showing the tweet has a negative sentiment.

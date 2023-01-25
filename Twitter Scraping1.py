from ast import main
import datetime
import pymongo
from pymongo import MongoClient
import snscrape.modules.twitter as sntwitter
from snscrape.modules import twitter
import pandas as pd
import streamlit as st
from datetime import datetime, timedelta

st.title('Twitter Scrapping By :blue[Sakthinathan]')
search_term = st.text_input("Enter a keyword or hashtag to search for:")
tweet_limit = st.number_input("Enter the maximum number of tweets to retrieve:")
start_date = st.date_input("Enter the start date for the tweets (YYYY-MM-DD):")
end_date = st.date_input("Enter the end date for the tweets (YYYY-MM-DD):")

tweets_column_list1 = []

def tweet():



    for i,tweet in enumerate(twitter.TwitterSearchScraper("from:{search_term}").get_items()):
                            
    
        if i>tweet_limit: #number of tweets you want to scrape
         break
        tweets_column_list1.append([tweet.date, tweet.id,tweet.url, tweet.content, tweet.user.username,tweet.replyCount,tweet.retweetCount,tweet.lang,tweet.likeCount,tweet.source]) #declare the attributes to be returned
    
    # Creating a dataframe from the tweets list above 
    tweets_df1 = pd.DataFrame(tweets_column_list1, columns=['Datetime', 'Tweet Id','URL', 'Content', 'Username','replyCount','retweetCount','language','likeCount','source'])
    
    print(tweets_df1)
    st.dataframe(tweets_df1)
    return(tweets_df1)

def GUI(tweets_df1):

    #Setting up connection to MongoDB 
    client = pymongo.MongoClient("mongodb://localhost:27017")
    #Creating new DB
    db = client.twitter 
    #creating new collection
    collection =db['contents']
    #adding data frame to dic
    data = tweets_df1.to_dict("records")
    
    
    if st.button("Upload to MongoDB"):
        if data:
         collection.insert_many(data)
         st.success("Data uploaded to MongoDB!")
        else:
         st.warning("No tweets have been scraped yet.")

    if st.button("Download as CSV"):
     tweets_df1.to_csv("tweets.csv", index=False)
     st.success("CSV downloaded!")

# Download as JSON
    if st.button("Download as JSON"):
     tweets_df1.to_json("tweets.json", orient="records")
     st.success("JSON downloaded!")


def main():
    tweeetdf =tweet()
    GUI(tweeetdf)
    
    
main()


#streamlit run "F:\Pythn Scripts\Twitter Scraping1.py"
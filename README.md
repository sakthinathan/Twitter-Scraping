# Twitter-Scraping
Twitter Scraping using Python

As part of my Data science learning done this project

By using the “snscrape” Library, 
Create a dataframe with date, id, url, tweet content, user,reply count, retweet count,language, source, like count.
Store each collection of data into a document into Mongodb 
Create a GUI using streamlit that should contain the feature to enter the keyword or Hashtag to be searched, select the date range and limit the tweet count need to be scraped. 
After scraping, the data needs to be displayed in the page and need a button to upload the data into Database and download the data into csv and json format.


## 🛠 Skills
Python, MongoDB,streamlit..


## Prerequisites

import pymongo
from pymongo import MongoClient
import snscrape.modules.twitter as sntwitter
from snscrape.modules import twitter
import pandas as pd
import streamlit as st
from datetime import datetime, timedelta

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

# ============================================ CREDITS ============================================
# Author: ADOTRI Frimpong
# Mail: frimpong.adotri@efrei.net
# Streamlit App url: https://frimpong-adotri-01-nlp-project-home-l6xg5d.streamlit.app
# =================================================================================================



# ============================================ MODULES IMPORT ============================================
import streamlit as st
import plotly.express as px
from ntscraper import Nitter
import pandas as pd
from textblob import TextBlob
import numpy as np
import datetime
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from typing import Dict, Callable
import re
import nltk
import os
from nltk.corpus import stopwords

nltk.download('punkt')  # python -m nltk.downloader punkt
nltk.download('averaged_perceptron_tagger') # python -m nltk.downloader averaged_perceptron_tagger
nltk.download('brown') # python -m nltk.downloader brown
nltk.download('stopwords')  # stopwords

# ============================================ PAGE SETUP CONFIGURATION ===================================
st.set_page_config(
    page_title='Twitter NLP',
    layout="wide"
)

@st.cache_data
def stylish_page():
    st.sidebar.image("./images/twitter_icon.png")
    with open("style.css") as css:
        st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)
        st.sidebar.markdown("# <span style=\"color:white background:#48b4e3\" ><center>TWITTER FOR NLP <img src=\"https://img.icons8.com/fluency/154/verified-badge.png\" width=\"30\" height=\"30\"></img></center></span>", unsafe_allow_html=True)

# =========================================================================================================


# =========================================== FUNCTIONS ===========================================

@st.cache_data
def scrape_tweets(keywords:str, start:str, stop:str, maxTweets:int=25) -> pd.DataFrame:
    tweets_list:list = []
    scraper:Nitter = get_Nitter_scrapper()
    tweets:Dict[str:str] = scraper.get_tweets(keywords, mode="term", number=maxTweets, since=start, until=stop)["tweets"]
    for tweet in tweets:
        tweets_list.append([tweet["date"], tweet["text"], tweet["user"]["username"]])
    data:pd.DataFrame = pd.DataFrame(tweets_list, columns=['datetime', 'text', 'username'])
    return data

@st.cache_data
def get_Nitter_scrapper():
    return Nitter(log_level=1, skip_instance_check=False)

#clean up the data with a function
@st.cache_data 
def text_clean(text:str) -> str:
    text:str = text.lower()
    text = re.sub(r'@[A-za-z0-9]+','',str(text))   # Removing Mentions 
    text = re.sub(r'#','',text)        # Removing Hashtags
    text = re.sub(r'https?:\/\/\S+','',text)  # Removing Hyper links
    text = re.sub('RT[\s]+','',text)          # Removing RT
    text = re.sub('\\xa0', '', text)       # Removing Unicode \xa0 character
    text = re.sub('\\n', ' ', text)       # Removing the \n character
    text = re.sub('\\t', ' ', text)       # Removing the \t character
    pattern = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)
    text=re.sub(pattern,'',text)  #Removing emojis
    #text=re.sub('[^a-zA-ZçÇèÈÉéîïÏÎÔôùÙ\']', ' ', text)
    text = ' '.join([word for word in text.split() if word not in stopwords.words("english")])   # Removing stopwords
    #doc = en_model(text)
    #text = ' '.join([str(word) for word in doc if not word.is_punct])    # Removing punctuations
    return text


# Compute the subjectivity
getSubjectivity:Callable[[str], float] = lambda text: TextBlob(text).sentiment.subjectivity


# Compute the polarity
getPolarity:Callable[[str], float] = lambda text : TextBlob(text).sentiment.polarity


def getPolarityAnalysis(score:float) -> str:
    if score < 0:
      return 'Negative'
    elif 0 < score <=.5:
      return 'Neutral'
    else:
      return 'Positive'

def getSubjectivityAnalysis(score:float) -> str:
  if score <= .45:
      return 'Objective'
  elif .45 < score <= .55:
      return 'Neutral'
  else:
      return 'Subjective'


@st.cache_data
def sentiment_analysis(data:pd.DataFrame) -> None:
    data["text"] = data["text"].apply(text_clean)
    data["subjectivity"] = data["text"].apply(getSubjectivity)
    data['polarity'] = data['text'].apply(getPolarity)
    data['polarity_analysis'] = data['polarity'].apply(getPolarityAnalysis)
    data['subjectivity_analysis'] = data['subjectivity'].apply(getSubjectivityAnalysis)
    st.markdown("***")
    st.markdown("### **<span style=\"color:#48b4e3\">SENTIMENT ANALYSIS</span>**", unsafe_allow_html=True)
    st.markdown("")

    st.markdown("**<span style=\"color:#48b4e3\">Polarity Chart</span>**", unsafe_allow_html=True)
    bar_fig1 = px.bar(x=np.unique(data['polarity_analysis']), y=data['polarity_analysis'].value_counts()).update_layout(
                    xaxis_title_text = "Polarity",
                    yaxis_title_text = "Count",
                    font_family="Courier New"
                )
    st.write(bar_fig1)
    st.markdown("")

    st.markdown("**<span style=\"color:#48b4e3\">Subjectivity Chart</span>**", unsafe_allow_html=True)
    bar_fig2 = px.bar(x=np.unique(data['subjectivity_analysis']), y=data['subjectivity_analysis'].value_counts()).update_layout(
                    xaxis_title_text = "Subjectivity",
                    yaxis_title_text = "Count",
                    font_family="Courier New"
                )
    st.write(bar_fig2)
    st.markdown("")

    st.markdown("**<span style=\"color:#48b4e3\">Polarity as a function of Subjectivity</span>**", unsafe_allow_html=True)
    scatter_fig = px.scatter(x=data["polarity"], y=data["subjectivity"]).update_layout(
                    xaxis_title_text = "Polarity",
                    yaxis_title_text = "Subjectivity",
                    font_family="Courier New"
                )
    st.write(scatter_fig)
    
    # Wordcloud modeling from tweet's text
    allwords = ' '.join([tweet for tweet in data["text"]])
    wordcloud = WordCloud(height=500,width=800,background_color="black").generate(allwords)  # ,colormap="Set1"
    fig, ax = plt.subplots()
    ax.imshow(wordcloud,interpolation="bilinear")
    ax.axis('off')
    st.markdown("**<span style=\"color:#48b4e3\">Tweets wordcloud</span>**", unsafe_allow_html=True)
    st.pyplot(fig)
    st.markdown("")

    
    
# ===================================================================================================

# =========================================== APP CODING ===========================================
def main():
    
    stylish_page()
    st.markdown("# <span style=\"color:#48b4e3\">Home</span>", unsafe_allow_html=True)
    st.markdown("***")
    st.sidebar.markdown("***")
    st.sidebar.markdown("### <span style=\"color:#48b4e3\">LET'S SCRAPE SOME TWEETS !</span> 🙃", unsafe_allow_html=True)
    number = st.sidebar.slider("Number of tweets :", min_value=10, max_value=1000)
    keywords = st.sidebar.text_input("Type keywords :")
    start = st.sidebar.date_input("Start date :", min_value=pd.to_datetime("2007-01-01"), max_value=pd.to_datetime(datetime.datetime.today()))
    end = st.sidebar.date_input("End date :", min_value=start, max_value=pd.to_datetime(datetime.datetime.today()))

    if st.sidebar.button("Execute", key="scraping"):
        st.markdown("### **<span style=\"color:#48b4e3\">TWEETS SCRAPED</span>**", unsafe_allow_html=True)
        random_tweets = scrape_tweets(keywords, str(start), str(end), maxTweets=number)
        if keywords == "":
            st.warning("WARNING : No keyword(s) entered !", icon="⚠️")
        elif len(random_tweets) == 0:
            st.dataframe(random_tweets)
            st.warning("WARNING : No Data Found !", icon="⚠️")
        else:
            st.dataframe(random_tweets)
            sentiment_analysis(random_tweets)

        
    
# ==================================================================================================
if __name__ == "__main__":
    main()

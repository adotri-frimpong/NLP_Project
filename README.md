# NLP_Project - Sentiment analysis

<image src="https://pic.clubic.com/v1/images/1941993/raw" width=800 center>

[<img src="https://img.shields.io/badge/Python-3.11.7-yellow.svg?logo=python">]() 
[<img src="https://img.shields.io/badge/Streamlit-1.43.2-red.svg?logo=streamlit">]()   [<img src="https://img.shields.io/badge/TextBlob-0.17.1-inactive.svg?logo=pypi">]()           [<img src="https://img.shields.io/badge/Ntscraper-0.3.17-blue.svg?logo=pypi">]()
[<img src="https://img.shields.io/badge/Numpy-1.23.5-blue.svg?logo=numpy">]()
[<img src="https://img.shields.io/badge/Plotly-5.11.0-ff69b4.svg?logo=plotly">]()     [<img src="https://img.shields.io/badge/Wordcloud-1.9.4-blue.svg?logo=pypi   ">]()
  
### **Synopsis** : 
This `Streamlit App` is a prototype for exploring sentiment analysis of tweets provides by `Twitter`. It's divided in 3 components:
> **Home** : By mentionning some keywords, the user is able to scrap some tweets generated in a selected window of time. The App will generate sentiment analysis plots and a wordcloud.

> Followers Engagement : This component expose main metrics and KPIs about a specific twitter user. Some details about the user's followers engagement is also precised.

>  Credentials: The component for for special thanks, author's name and references.

***
### **Run the project** :

1. Clone the repository
```bash
$ git clone https://github.com/adotri-frimpong/NLP_Project.git
``` 

2. Install the requirements via the Makefile
```bash
$ make setup
```

3. Switch to the created python virtual environment
```bash 
$ source .venv/bin/activate
```

4. Run the app
```bash
$ streamlit run Home.py
```

5. Stop the app
Press `Ctrl+C` to stop the streamlit background server.

***
### **Troubleshooting** :
The first version of this project was based on snscrape but since Twitter turned to X, API endpoints and scrapping policies changed and snscrape became unstable. In order to find an alternative to snscrape, I decided to use `ntscraper` which is a python wrapper for the X API. But instead of scrapping X API directly, ntscraper scraps Nitter which is an open source implementation of the X API.

***



 

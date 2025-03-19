# ============================================ CREDITS ============================================
# Author: ADOTRI Frimpong
# Mail: frimpong.adotri@efrei.net
# Streamlit App url: https://frimpong-adotri-01-dataviz-lab3-uber-app-vo4lvn.streamlit.app/
# =================================================================================================



# ============================================ MODULES IMPORT ============================================
import streamlit as st

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

# =========================================== APP CODING ===========================================
def main():
    stylish_page()
    st.sidebar.markdown("***")
    st.markdown("# <span style=\"color:#2daae1\">CREDENTIALS</span>", unsafe_allow_html=True)
    st.markdown("***")
    st.markdown(f">**<span style=\"color:#2daae1\">SPECIAL THANKS TO</span>** :    **TALMATKADI Manissa**", unsafe_allow_html=True)
    st.markdown(f">**<span style=\"color:#2daae1\">AUTHOR</span>** :    **ADOTRI Frimpong**", unsafe_allow_html=True)
    st.markdown(f">**<span style=\"color:#2daae1\">RESSOURCES</span>** :", unsafe_allow_html=True)

    st.markdown(f"> >>**FROM MEDIUM : https://medium.com/machine-learning-mastery/sentiment-analysis-and-topic-modeling-of-tweets-on-ukrainerussia-war-e20a1dbca263**", unsafe_allow_html=True)
    st.markdown(f"> >>**FROM TEXTBLOB DOC :  https://textblob.readthedocs.io/en/dev/index.html**", unsafe_allow_html=True)
    st.markdown(f"> >>**FROM STREAMLIT DOC : https://docs.streamlit.io**", unsafe_allow_html=True)
    st.markdown(f"> >>**FROM GITHUB : https://github.com/Smartking1**", unsafe_allow_html=True)
    st.markdown("***")
    st.markdown(f"## <span style=\"color:#2daae1\"><center> © Copyright March 2023 </center></span>", unsafe_allow_html=True)
            

    
# ==================================================================================================
if __name__ == "__main__":
    main()
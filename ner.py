import streamlit as st
import spacy
from spacy import displacy
from newspaper import Article

# Load English tokenizer, tagger, parser, NER, and word vectors
import en_core_web_sm
nlp = en_core_web_sm.load()

st.title("Named Entity Recognizer")

st.info("This app will take a URL input or a direct text input from the user and then print the named entities")

text_input = st.text_area("Enter text:")
url_input = st.text_input("Enter a URL:")

if st.button("Submit"):
    try:
        if text_input:
            # Process the text with spaCy
            doc = nlp(text_input)
        elif url_input:
            # Instantiate Article object with the provided URL
            article = Article(url_input)
            # Download and parse the article content
            article.download()
            article.parse()
            # Process the text with spaCy
            doc = nlp(article.text)
        else:
            st.warning("Please enter either text or a URL.")
            st.stop()

        # Render named entity visualization
        ent_html = displacy.render(doc, style="ent", jupyter=False)
        # Display the entity visualization in the browser
        st.markdown(ent_html, unsafe_allow_html=True)
    except Exception as e:
        st.error("An error occurred: {}".format(str(e)))

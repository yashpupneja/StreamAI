import streamlit as st
from flair.models import TextClassifier
from flair.data import Sentence
import numpy as np
global tagger

def load_flair():
	return TextClassifier.load('en-sentiment')

def main():
	tagger = load_flair()

	st.markdown("<h1 style = 'textalign:center; color:yellow;'> Sentiment Detection </h1>", unsafe_allow_html = True)
	st.write("Sentiment Detection from text is a classical problem. This is used when you try to predict the sentiment of comments on a restaurant. This app analyzes the sentiment of the user, whether it's Postive or Negative.")

	input_sent = st.text_input("Input Sentence", "Although not well rated, the food in this restaurant was tasty and I enjoyed the meal!")

	s = Sentence(input_sent)
	tagger.predict(s)
	st.write("### Your Sentence is ", str(s.labels))

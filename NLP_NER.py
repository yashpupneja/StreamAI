#Core Pkgs
import streamlit as st

#NLP Pkgs
import spacy_streamlit
import spacy
nlp = spacy.load('en')

#Web Scraping Pkgs
from bs4 import BeautifulSoup
from urllib.request import urlopen

@st.cache
def get_text(raw_url):
	page = urlopen(raw_url)
	soup = BeautifulSoup(page)
	fetched_text = " ".join(map(lambda p:p.text, soup.find_all('p')))
	return fetched_text


def main():
	"""A Simple NLP App with Spacy-Streamlit"""
	st.title("Named Entity Recogintion")
	st.markdown("Named Entity Recognition is the process by which the system identify named entities (persons, organisations, governments, money, etc.) using a mix of deep learning and probabilistic approach. This type of algorithm is generally trained on large corpuses e.g. in wikipedia . We have implemented this algorithm using a state-of-the-art library known as SpaCy. BeautifulSoup is used as a web scrapping tool to extract the text from a URL provided.")

	menu = ["NER", "NER for URL"]
	choice = st.sidebar.radio("Pick a choice", menu)


	if choice == "NER":
		st.subheader("Named Entity Recognition")
		raw_text = st.text_area("Your Text","")
		if raw_text != "":
			docx = nlp(raw_text)
			spacy_streamlit.visualize_ner(docx, labels = nlp.get_pipe('ner').labels)

	elif choice == "NER for URL":
		st.subheader("Analyze text from URL")
		raw_url = st.text_input("Enter URL","")
		text_length = st.slider("Length to Preview", 50,200)
		if raw_url != "":
			result = get_text(raw_url)
			len_of_full_text = len(result)
			len_of_short_text = round(len(result)/text_length)
			st.subheader("Text to be analyzed:")
			st.write(result[:len_of_short_text])
			preview_docx = nlp(result[:len_of_short_text])
			spacy_streamlit.visualize_ner(preview_docx, labels = nlp.get_pipe('ner').labels)

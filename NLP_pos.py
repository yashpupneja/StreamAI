#Core Pkgs
import streamlit as st

#NLP Pkgs
import spacy
# Load English tokenizer, tagger, parser, NER and word vectors 
nlp = spacy.load("en_core_web_sm") 
from spacy import displacy
HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem; margin-bottom: 2.5rem">{}</div>"""


#To extract the pos tags
def pos(raw_text):
	if raw_text != "":
		st.subheader("Part-of-speech Tags")
		# Process whole documents 
		doc = nlp(raw_text) 
		# Token and Tag 
		for token in doc: 
			st.write(token, token.pos_) 


#To visualize pos tags
def visualize(raw_text):
	if raw_text != "":
		doc = nlp(raw_text) 
		if "parser" in nlp.pipe_names:
		    st.subheader("Dependency Parse & Part-of-speech tags")
		    st.sidebar.header("Dependency Parse")
		    split_sents = st.sidebar.checkbox("Split sentences", value=True)
		    collapse_punct = st.sidebar.checkbox("Collapse punctuation", value=True)
		    collapse_phrases = st.sidebar.checkbox("Collapse phrases")
		    compact = st.sidebar.checkbox("Compact mode")
		    options = {
		        "collapse_punct": collapse_punct,
		        "collapse_phrases": collapse_phrases,
		        "compact": compact,
		    }
		    docs = [span.as_doc() for span in doc.sents] if split_sents else [doc]
		    for sent in docs:
		        html = displacy.render(sent, options=options)
		        # Double newlines seem to mess with the rendering
		        html = html.replace("\n\n", "\n")
		        if split_sents and len(docs) > 1:
		            st.markdown(f"> {sent.text}")
		        st.write(HTML_WRAPPER.format(html), unsafe_allow_html=True)


def main():
	"""A Simple NLP-POS App"""
	st.title("Parts-of-Speech Tagging")
	st.markdown("Part-Of-Speech Tagging is the process by which we can tag each word of a sentence with its corresponding grammatical function (determinant, noun, adjective) using a mix of deep learning and probabilistic approach as in Named Entity Recognition.It also uses the library named as SpaCy.")

	raw_text = st.text_area("Your Text","")
	pos(raw_text)
	visualize(raw_text)
	
		

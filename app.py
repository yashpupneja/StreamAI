import streamlit as st

#Component Pkgs
import streamlit.components.v1 as components 

#Pkgs - Files
import Html
import Css
import imagecontrast


def main():
	"""STREAM AI - A Hub for NLP Apps, Computer Vision Apps, Data Science Apps, ML Apps, DL Apps, """
	Css.local_css("style.css")
	Css.side_background()

	choice = st.sidebar.selectbox("Select Activity", ["About", "Applications", "Blogs"])

	if choice == 'About':
		Html.html_heading()
		st.markdown(Html.html_heading(), unsafe_allow_html = True)
		components.html(Html.html_about(), height=1000)

	elif choice == 'Applications':
		categories = ["Natural Language Processing","Computer Vision", "Speech Processing", "Data Visualization", "Generative Models"]
		category_choice = st.sidebar.radio("Pick a Domain",categories)

		if category_choice == "Natural Language Processing":
			apps_nlp = st.sidebar.radio("Algorithm",('Named Entity Recognition', 'Part-of-Speech Tagging', 'Sentiment Detection', 'Question Answering'))
			if apps_nlp == 'Named Entity Recognition':
				st.success("NLP: Named Entity Recognition App")

			elif apps_nlp == 'Part-of-Speech Tagging':
				st.success("NLP: Part-of-Speech Tagging App")

			elif apps_nlp == 'Sentiment Detection':
				st.success("NLP: Sentiment Detection App")

			elif apps_nlp == 'Question Answering':
				st.success("NLP: Question Answering App")

		elif category_choice == 'Computer Vision':
			apps_cv = st.sidebar.radio("Algorithm",['Image Contrasting','Face Detection', 'Eyes Detection','Smile Detection','Cannize','Cartoonize','Style Detection','Pose Detection', 'Semantic Segmentation', 'Object Detection'])
			if apps_cv == 'Image Contrasting':
				imagecontrast.main()
			if apps_cv == 'Face Detection':
				st.success("CV: Face Detection App")

			elif apps_cv == 'Eyes Detection':
				st.success("CV: Eyes Detection App")

			elif apps_cv == 'Smile Detection':
				st.success("CV: Smile Detection App")

			elif apps_cv == 'Style Detection':
				st.success("CV: Style Detection App")

			elif apps_cv == 'Cannize':
				st.success("CV: Cannizing an Image App")

			elif apps_cv == 'Cartoonize':
				st.success("CV: Cartoonizing an Image App")

			elif apps_cv == 'Pose Detection':
				st.success("CV: Pose Detection App")

			elif apps_cv == 'Semantic Segmentation':
				st.success("CV: Semantic Segmentation App")

			elif apps_cv == 'Object Detection':
				st.success("CV: Object Detection App")



		elif category_choice == 'Speech Processing':
			apps_sp = st.sidebar.radio("Algorithm",['Voice Based Gender Detection'])
			if apps_sp == 'Voice Based Gender Detection':
				st.success("SP: Voice Based Gender Detection App")


		elif category_choice == 'Data Visualization':
			apps_ds = st.sidebar.radio("Algorithm",['DataSet Explorer'])
			if apps_ds == 'DataSet Explorer':
				st.success("DS: DataSet Explorer App")

		elif category_choice == 'Generative Models':
			pass


	elif choice == 'Blogs':
		pass



if __name__ == '__main__':
	main()

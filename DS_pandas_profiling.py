# Core Pkgs
import streamlit as st

#Other Pkgs
#EDA Pkgs
import pandas as pd
import codecs
from pandas_profiling import ProfileReport

#Component Pkgs
import streamlit.components.v1 as components  #v1 is version1 : If new features are added, then it will not break your app
from streamlit_pandas_profiling import st_profile_report

#Custom Component Functions
import sweetviz as sv

def st_display_sweetviz(report_html, width=1000,height = 500):
	report_file = codecs.open(report_html, 'r')  #codecs help in reading html file
	page = report_file.read()
	components.html(page,width= width, height=height, scrolling=True)

def main():
	"""A Simple EDA App with Streamlit Components (Using Pandas Profiling and Sweetviz in Streamlit)"""

	menu = ["Pandas Profile", "Sweetviz"]
	choice = st.sidebar.selectbox("Menu", menu)

	if choice == "Pandas Profile":
		st.subheader("Automated Exploratory Data Analsis (with Pandas Profile)")
		st.write("EDA is the task of analyzing data from statistics, simple plotting tools, linear algebra and other techniques to understand what the dataset is, before we go to actual machine learning.")
		st.write("Pandas Profile generates profile reports from a pandas DataFrame. Pandas Profiling extends the pandas DataFrame for quick data analysis.")
		st.set_option('deprecation.showfileUploaderEncoding', False)
		data_file = st.file_uploader("Upload CSV", type = ['csv'])
		if data_file is not None:
			df = pd.read_csv(data_file)
			st.dataframe(df.head())
			profile = ProfileReport(df)
			st_profile_report(profile)

	elif choice == "Sweetviz":
		st.subheader("Automated Exploratory Data Analysis (with Sweetviz)")
		st.write("Sweetviz is an open source Python library that generates beautiful, high-density visualizations to kickstart EDA (Exploratory Data Analysis). Output is a fully self-contained HTML application.The system is built around quickly visualizing target values and comparing datasets. Its goal is to help quick analysis of target characteristics, training vs testing data, and other such data characterization tasks.")
		data_file = st.file_uploader("Upload CSV", type = ['csv'])
		st.set_option('deprecation.showfileUploaderEncoding', False)
		if data_file is not None:
			df = pd.read_csv(data_file)
			st.dataframe(df.head())
			#Normal Workflow for sweetviz
			report = sv.analyze(df)
			report.show_html()
			st_display_sweetviz("SWEETVIZ_REPORT.html")


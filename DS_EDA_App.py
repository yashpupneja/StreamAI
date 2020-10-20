import streamlit as st

#EDA
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


#EDA
my_dataset = 'iris.csv'

#Fxn to Load Dataset
@st.cache(persist = True)   #save data in cache form so that it can be loaded faster.
def explore_data(dataset):
	df = pd.read_csv(os.path.join(dataset))
	return df

def main():

#Title/Text
	st.title("Iris Exploratory Data Analysis")
	st.write("EDA is the task of analyzing data from statistics, simple plotting tools, linear algebra and other techniques to understand what the dataset is, before we go to actual machine learning.")
	st.write("")
	st.subheader("Dataset:")

	data = explore_data(my_dataset)

	menu =  st.sidebar.radio('Options', ('Preview Dataset',"Show Entire Dataset", 'Show Column Names', 'Show Dimensions of Dataset', 'Show Summary of Dataset'))

	#Preview dataset
	if menu == 'Preview Dataset':
		choice = st.selectbox("",("Head", "Tail"))
		#data = explore_data(my_dataset)
		if choice == "Head":
			st.write(data.head())
		elif choice == "Tail":
			st.write(data.tail())
		else:
			st.write(data.head(2))

	#Show Entire Dataset
	if menu == "Show Entire Dataset":
		#st.write(data)   #MASTER FXN
		st.dataframe(data)


	#Show Column Name
	if menu == "Show Column Names":
		st.write(data.columns)
		#Select A Column
		col_option = st.selectbox("Select Column",("sepal_length","sepal_width", "petal_length", "petal_width", "species"))
		if col_option == 'sepal_width':
			st.write(data['sepal_width'])
		elif col_option == 'sepal_length':
			st.write(data['sepal_length'])
		elif col_option == 'petal_width':
			st.write(data['petal_width'])
		elif col_option == 'petal_length':
			st.write(data['petal_length'])
		elif col_option == 'species':
			st.write(data['species'])
		else:
			st.write("Slect Column")


	#Show Dimensions
	if menu == "Show Dimensions of Dataset":
		data_dim = st.radio("What Dimensions Do You Want to See", ("Rows", "Columns", "All"))
		if data_dim == "Rows":
			st.text("Showing Rows")
			st.write(data.shape[0])
		elif data_dim == "Columns":
			st.text("Showing Columns")
			st.write(data.shape[1])
		else:
			st.text("Showing Shape of Dataset")
			st.write(data.shape)	


	#Show Summary
	if menu == "Show Summary of Dataset":
		st.write(data.describe())



	#Plot
	st.write("")
	#Bar Plot
	st.sidebar.text("")
	st.sidebar.text("Select the Plot:")
	if st.sidebar.checkbox("Show Bar Plot with Matplotlib"):
		st.subheader("Bar Plot:")
		st.write(data.plot(kind = 'bar'))
		st.pyplot()

	#Correlation Plot
	if st.sidebar.checkbox("Show Correlation Plot with Matplotlib"):
		#st.write(plt.matshow(data.corr()))
		st.subheader("Correlation Plot (with Matplotlib):")
		plt.matshow(data.corr())
		st.pyplot()

	#Seaborn Plot
	if st.sidebar.checkbox("Show Correlation Plot with Seaborn"):
		st.subheader("Correlation Plot (with Seaborn:")
		st.write(sns.heatmap(data.corr()))
		st.pyplot()

	#Group 
	if st.sidebar.checkbox("Show Bar Chart Plot"):
		st.subheader("Bar Chart Plot:")
		v_group = data.groupby("species")
		st.bar_chart(v_group)


	if st.sidebar.checkbox("Show Line Plot"):
		st.subheader("Line Plot:")
		st.line_chart(data)

	#Group 
	if st.sidebar.checkbox("Show Area Chart Plot"):
		st.subheader("Area Chart Plot:")
		v_group = data.groupby("species")
		st.area_chart(v_group)

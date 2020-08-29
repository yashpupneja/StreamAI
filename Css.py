import streamlit as st

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)  

def side_background():
	side_temp = """
	<style>
	.sidebar .sidebar-content {
	    background-image: linear-gradient(#e1b382,#c89666);
	    color: white;
	}
	</style>
	"""
	return st.markdown(side_temp, unsafe_allow_html = True)
	

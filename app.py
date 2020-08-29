import streamlit as st

#Component Pkgs
import streamlit.components.v1 as components 


#Custom Footer
header = """
	 <!-- CSS  -->
	  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
	  <link href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css" type="text/css" rel="stylesheet" media="screen,projection"/>
	  <link href="static/css/style.css" type="text/css" rel="stylesheet" media="screen,projection"/>
	   <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.5.0/css/all.css" integrity="sha384-B4dIYHKNBt8Bc12p+WXckhzcICo0wtJAoU8YZTY5qE0Id1GSseTk6S+L3BlXeVIU" crossorigin="anonymous">
	 <footer class="page-footer grey darken-4">
	    <div class="container" id="aboutapp">
	      <div class="row">
	        <div class="col l6 s12">
	          <h5 class="white-text">About</h5>
	          <p class="grey-text text-lighten-4">
	          StreamAI app involves the combination of several domains of artificial intelligence like Natural Language Processing, Computer Vision, Data Science etc. on a single platform. <br>
	          The app aims at making it feasible to use various functionalities of AI from a single application rather than from various different applications intended for different functionalities.
			  Technologies, Libraries used:<br>
			  <i><ol><li> Python for coding </li> <li> Streamlit for UI.</li>
			  <li>Python Libraries: NumPy, Matplotlib, OpenCV, Pandas, Pillow, Scikit-Learn, Joblib, Spacy, BioPython, NeatBio, Pandas Profiling, Sweetviz</li></ol></i></p>
	        </div>
	      
	   <div class="col l3 s12">
	          <h5 class="white-text">Connect With Us</h5>
	          <ul>
	          <a href="https://gh.linkedin.com/in/srishtii24" target="_blank" class="white-text">
	            <i class="fab fa-linkedin fa-4x"></i>
	          </a>	         
	           <a href="https://github.com/srishtii24/" target="_blank" class="white-text">
	            <i class="fab fa-github-square fa-4x"></i>
	          </a>
	          </ul>
	        </div>
	      </div>
	    </div>
	    <div class="footer-copyright">
	      <div class="container">
	      Made by <p class="white-text text-lighten-3">Srishti Gupta and Yashaswi Pupneja</p><br/>
	      </div>
	    </div>
	  </footer>
	"""
def local_css(file_name):
	with open(file_name) as f:
		st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)
def main():
	"""STREAM AI - A Hub for NLP Apps, Computer Vision Apps, Data Science Apps, ML Apps, DL Apps, """    
	local_css("style.css")
	remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')
	# sidebar background settings
	st.markdown(
    	"""
		<style>.sidebar .sidebar-content {
    	background-image: linear-gradient(#e1b382,#c89666);
    	color: white;
		}
		</style>
		""",
    unsafe_allow_html=True,)

	st.sidebar.title("StreamAI")

	activities = ["Category", "About","Blogs"]
	choice = st.sidebar.selectbox("Select Activity", activities)

	if choice == 'Category':
		categories = ["Natural Language Processing","Computer Vision", "Speech Processing", "Data Visualization/Data Science"]
		category_choice = st.sidebar.radio("Pick a Domain",categories)
		if category_choice=="Natural Language Processing":
			nlp_algo=["Named Entity Detection","Part-of-speech Tagging","Sentimental Detection","Question Answering"]
			nlp=st.sidebar.radio("Algorithm:",nlp_algo)
		elif category_choice=='Computer Vision':
			cv_algo=["Detection","Cannize","Cartonize","Semantic Segmentation"]
			cv=st.sidebar.radio("Algorithm:",cv_algo)
			if cv=="Detection":
				detect_choice=["Face","Smile","Eyes","Style","Pose","Object"]
				detect=st.sidebar.selectbox("Detection of : ",detect_choice)

	
	elif choice == 'About':
		html_temp = """
		<div style = "background-color:tomato; padding:15px;">
		<h1><center> StreamAI</center></h1>
		</div>
		"""

		st.markdown(html_temp, unsafe_allow_html = True)

		components.html(header, height=1000)



if __name__ == '__main__':
	main()
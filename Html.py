def html_about():
	#Custom Footer
	footer_temp = """
		 <!-- CSS  -->
		  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
		  <link href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css" type="text/css" rel="stylesheet" media="screen,projection"/>
		  <link href="static/css/style.css" type="text/css" rel="stylesheet" media="screen,projection"/>
		   <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.5.0/css/all.css" integrity="sha384-B4dIYHKNBt8Bc12p+WXckhzcICo0wtJAoU8YZTY5qE0Id1GSseTk6S+L3BlXeVIU" crossorigin="anonymous">
		 <footer class="page-footer grey darken-4">
		    <div class="container" id="aboutapp">
		      <div class="row">
		        <div class="col l6 s12">
		          <h3 class="white-text">About StreamAI</h3>
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
			  <a href="https://github.com/yashaswipupneja/" target="_blank" class="white-text">
		            <i class="fab fa-github-square fa-4x"></i>
		          </a>
		          </a>	         
		           <a href="https://github.com/srishtii24/" target="_blank" class="white-text">
		            <i class="fab fa-github-square fa-4x"></i>
			   <a href="https://github.com/yashpupneja/" target="_blank" class="white-text">
		            <i class="fab fa-github-square fa-4x"></i>
			   </a>
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
	return footer_temp

def html_heading():
	html_temp = """
		<div style = "background-color:tomato; padding:15px;">
		<h1><center> StreamAI</center></h1>
		</div>
		"""
	return html_temp

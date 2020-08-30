# Core packages
import streamlit as st
import cv2
from pil import Image,ImageEnhance
import numpy as np
import os
import warnings
# import io

@st.cache
def load_image(img):
	im=Image.open(img)
	return im

def main():
	"""Face Detection App"""

	st.title("Image Constraction App")
	st.text("Build with streamlit and opencv")
	activities=["Contrast Type","About"]
	choice = st.selectbox("Select Activity: ",activities)
	if(choice=='Contrast Type'):
		#st.subheader("")
		image_file=st.file_uploader("Upload Image",type=['jpg','png','jpeg'])
		warnings.filterwarnings('ignore')
		st.set_option('deprecation.showfileUploaderEncoding', False)
		if image_file is not None:
			our_image = Image.open(image_file)
			st.text("Original Image")
			# st.write(type(our_image))
			st.image(our_image)

		enhance_type = st.sidebar.radio("Enhance Type",["Original","Gray Scale","Contrast","Blurring"])
		if enhance_type == 'Gray Scale':
			# Converting the image into array of RGB
			new_img = np.array(our_image.convert('RGB'))
			# Converting RGB To Grayscale
			gray=cv2.cvtColor(new_img,cv2.COLOR_BGR2GRAY)
			#gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
			# st.write(new_img)
			st.image(gray)

		if enhance_type=='Contrast':
			# Contrastor range is provided
			c_rate = st.sidebar.slider("Constrast",1.0,3.5)
			enhancer = ImageEnhance.Contrast(our_image)
			img_output = enhancer.enhance(c_rate)
			st.image(img_output)

		# if enhance_type=='Brightness':
		# 	# Brightness range is provided
		# 	c_rate = st.sidebar.slider("Brightness",0.5,3.5)
		# 	enhancer = ImageEnhance.Brightness(our_image)
		# 	img_output = enhancer.enhance(c_rate)
		# 	st.image(img_output)		
		
		if enhance_type == 'Blurring':
			# Converting the image into array of RGB
			new_img = np.array(our_image.convert('RGB'))
			# Converting RGB To Grayscale
			blur_rate = st.sidebar.slider("Blurring",0.5,3.5)
			img=cv2.cvtColor(new_img,1)
			blur=cv2.GaussianBlur(img,(11,11),blur_rate)
			# st.write(new_img)
			st.image(blur)

	elif(choice=='About'):
		st.subheader("About")

if __name__=="__main__":
	main()

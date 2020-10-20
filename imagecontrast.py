# Core packages
import streamlit as st
import cv2
from PIL import Image,ImageEnhance
import numpy as np
import os
import warnings
import matplotlib.pyplot as plt
# import io

@st.cache
def load_image(img):
	im=Image.open(img)
	return im

def contrast(our_image):
	new_img = np.array(our_image.convert('RGB'))
	img = cv2.cvtColor(new_img,1)
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	st.markdown("#### Original Image")
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

	if enhance_type == 'Blurring':
		# Converting the image into array of RGB
		new_img = np.array(our_image.convert('RGB'))
		# Converting RGB To Grayscale
		blur_rate = st.sidebar.slider("Blurring",0.5,3.5)
		img=cv2.cvtColor(new_img,1)
		blur=cv2.GaussianBlur(img,(11,11),blur_rate)
		# st.write(new_img)
		st.image(blur)

def main():
	"""Face Detection App"""

	st.title("Image Constraction App")
	st.text("Image Constraction is the app through which the contrast of different images can be known.")
	activities=("Show Demo","Browse Image")
	choice = st.radio("Select Activity: ",activities)
	if(choice=='Browse Image'):
		#st.subheader("")
		warnings.filterwarnings('ignore')
		st.set_option('deprecation.showfileUploaderEncoding', False)
		image_file=st.file_uploader("Upload Image",type=['jpg','png','jpeg'])
		if image_file is not None:
			our_image = Image.open(image_file)
			st.text("Original Image")
			# st.write(type(our_image))
			st.image(our_image)
			contrast(our_image)
		

	elif choice == "Show Demo":
		our_image = Image.open("images/girl_image.jpg")
		contrast(our_image)

if __name__=="__main__":
	main()

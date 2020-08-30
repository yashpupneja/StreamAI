import streamlit as st
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os


face_cascade = cv2.CascadeClassifier('frecog/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('frecog/haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('frecog/haarcascade_smile.xml')

def cannize_image(our_image):
	new_img = np.array(our_image.convert('RGB'))
	img = cv2.cvtColor(new_img,1)
	img = cv2.GaussianBlur(img, (11, 11), 0)
	

	st.markdown("#### Original Image")
	#st.image(our_image, width = 800)
	plt.figure(figsize = (12,8))
	plt.imshow(our_image)
	st.pyplot()


	threshold1 = st.sidebar.slider("Threshold 1", 10, 110,50,20)
	threshold2 = st.sidebar.slider("Threshold 2", 80, 200, 150, 20)

	canny = cv2.Canny(img, threshold1, threshold2)

	st.markdown("#### Cannized Image")
	plt.figure(figsize = (12,8))
	plt.imshow(canny)
	st.pyplot()


def cannize_main():
	"""Cannize an Image APP"""

	st.title("Cannizing an Image")
	
	choice = st.radio("", ("Show Demo", "Browse an Image"))
	st.write("")

	if choice == "Browse an Image":
		st.set_option('deprecation.showfileUploaderEncoding', False)
		image_file = st.file_uploader("Upload Image", type=['jpg','png','jpeg'])

		if image_file is not None:
			our_image = Image.open(image_file)  
			cannize_image(our_image)
			
	elif choice == "Show Demo":
		our_image = Image.open("images/girl_image.jpg")
		cannize_image(our_image)



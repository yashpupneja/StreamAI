import streamlit as st
import cv2
import numpy as np
import matplotlib.pyplot as plt
from pil import Image
import os


face_cascade = cv2.CascadeClassifier('frecog/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('frecog/haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('frecog/haarcascade_smile.xml')

def cartoonize_image(our_image):
	new_img = np.array(our_image.convert('RGB'))
	img = cv2.cvtColor(new_img,1)
	gray = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
	

	st.markdown("#### Original Image")
	#st.image(our_image, width = 800)
	plt.figure(figsize = (12,8))
	plt.imshow(our_image)
	st.pyplot()
	

	# Edges
	gray = cv2.medianBlur(gray, 5)
	edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
	#Color
	color = cv2.bilateralFilter(img, 9, 300, 300)
	#Cartoon
	cartoon = cv2.bitwise_and(color, color, mask=edges)



	st.markdown("#### Cartoonized Image")
	plt.figure(figsize = (12,8))
	plt.imshow(cartoon)
	st.pyplot()


def cartoonize_main():
	"""Cannize an Image APP"""

	st.title("Cartoonizing an Image")
	
	choice = st.radio("", ("Show Demo", "Browse an Image"))
	st.write("")

	if choice == "Browse an Image":
		st.set_option('deprecation.showfileUploaderEncoding', False)
		image_file = st.file_uploader("Upload Image", type=['jpg','png','jpeg'])

		if image_file is not None:
			our_image = Image.open(image_file)  
			cartoonize_image(our_image)
			
	elif choice == "Show Demo":
		our_image = Image.open("images/girl_image.jpg")
		cartoonize_image(our_image)



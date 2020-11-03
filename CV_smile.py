import streamlit as st
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

face_cascade = cv2.CascadeClassifier('frecog/haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('frecog/haarcascade_smile.xml') 



def detect_smiles(our_image):
	st.set_option('deprecation.showPyplotGlobalUse', False)
	new_img = np.array(our_image.convert('RGB'))
	img = cv2.cvtColor(new_img,1)
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	st.markdown("#### Original Image")
	#st.image(our_image, width = 800)
	plt.figure(figsize = (12,8))
	plt.imshow(our_image)
	st.pyplot()


	scaleFactor = st.sidebar.slider("Scale Factor", 1.13, 1.20)
	minNeighbors = st.sidebar.slider("Number of neighbors", 1, 15, 5, 1)
	minSize = st.sidebar.slider("Minimum Size", 10,50,20,1)

	# Detect Faces
	faces = face_cascade.detectMultiScale(gray,scaleFactor=scaleFactor,minNeighbors=minNeighbors,flags = cv2.CASCADE_SCALE_IMAGE)
	
	for (x, y, w, h) in faces:
		roi_gray = gray[y:y+h, x:x+h]
		roi_color = img[y:y+h, x:x+h]
		# Detect Smiles
		smiles = smile_cascade.detectMultiScale(roi_gray,1.7,20,flags = cv2.CASCADE_SCALE_IMAGE)
		# Draw rectangle around the Smiles
		for (sx, sy, sw, sh) in smiles:
			cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (255, 0, 0), 5)
	
	st.markdown("#### Detected Smiles")
	plt.figure(figsize = (12,8))
	plt.imshow(img, cmap = 'gray')
	st.pyplot()


def smiles_main():
	"""SMILE DETECTION APP"""

	st.title("Smile Detection")
	st.write("Smile detection is a central algorithm in computer vision used to detect smiles using OpenCV . The algorithm implemented below is a Haar-Cascade Classifier.")

	choice = st.radio("", ("Show Demo", "Browse an Image"))
	st.write("")

	if choice == "Browse an Image":
		st.set_option('deprecation.showfileUploaderEncoding', False)
		image_file = st.file_uploader("Upload Image", type=['jpg','png','jpeg'])

		if image_file is not None:
			our_image = Image.open(image_file)  
			detect_smiles(our_image)
			
	elif choice == "Show Demo":
		our_image = Image.open("images/smiling.jpg")
		detect_smiles(our_image)



import streamlit as st
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

face_cascade = cv2.CascadeClassifier('frecog/haarcascade_frontalface_default.xml')

def detect_faces(our_image):
	st.set_option('deprecation.showPyplotGlobalUse', False)
	new_img = np.array(our_image.convert('RGB'))
	img = cv2.cvtColor(new_img,1)
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	st.markdown("#### Original Image")
	#st.image(our_image, width = 800)
	plt.figure(figsize = (12,8))
	plt.imshow(our_image)
	st.pyplot()

	scaleFactor = st.sidebar.slider("Scale Factor", 1.02,1.15,1.1,0.01)
	minNeighbors = st.sidebar.slider("Number of neighbors", 1, 15, 5, 1)
	minSize = st.sidebar.slider("Minimum Size", 10,50,20,1)

	#Detect Faces
	faces = face_cascade.detectMultiScale(gray,scaleFactor=scaleFactor,minNeighbors=minNeighbors,flags = cv2.CASCADE_SCALE_IMAGE)
	#Draw Rectangle
	for (x,y,w,h) in faces:
		if w > minSize:
			cv2.rectangle(gray, (x,y), (x+w,y+h), (255,255,255), 5)

	st.markdown("#### Detected Faces")
	plt.figure(figsize = (12,8))
	plt.imshow(gray, cmap = 'gray')
	st.pyplot()
	if len(faces)>1:
		st.subheader("Found {} faces".format(len(faces)))
	else:
		st.subheader("Found {} face".format(len(faces)))



def face_main():
	"""FACE DETECTION APP"""

	st.title("Face Detection")
	st.write("Face detection is a central algorithm in computer vision. The algorithm implemented below is a Haar-Cascade Classifier. It detects several faces using OpenCV.")

	choice = st.radio("", ("Show Demo", "Browse an Image"))
	st.write()

	if choice == "Browse an Image":
		st.set_option('deprecation.showfileUploaderEncoding', False)
		image_file = st.file_uploader("Upload Image", type=['jpg','png','jpeg'])

		if image_file is not None:
			our_image = Image.open(image_file)  
			detect_faces(our_image)
			
	elif choice == "Show Demo":
		our_image = Image.open("images/girl_image.jpg")
		detect_faces(our_image)



#import imutil
import time
import os
import subprocess
import cv2 as cv
#from imutil import paths
import streamlit as st
import matplotlib.pyplot as plt
import glob


def resize_img(img, width=None, height=None, inter=cv.INTER_AREA):
    dim = None
    h, w = img.shape[:2]

    if width is None and height is None:
        return img
    elif width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    elif height is None:
        r = width / float(w)
        dim = (width, int(h * r))

    resized = cv.resize(img, dim, interpolation=inter)
    return resized

def detect_style():
	st.markdown("<h1>Neural Style Transfer</h1>", unsafe_allow_html=True)
	st.write("Neural Style Transfer Using OpenCV")
	modelPaths = []
	for m in os.listdir("./models/instance_norm"):
		modelPaths.append("./models/instance_norm/" + m)
	# print("**************", modelPaths)
	# modelPaths = sorted(list(modelPaths))
	print(modelPaths)
	for modelPath in modelPaths:
		# load the neural style transfer model from disk
		print("[INFO] loading {}...".format(modelPath))
		net = cv.dnn.readNetFromTorch(modelPath)

		# load the input image, resize it to have a width of 600 pixels,
		# then grab the image dimensions
		image = cv.imread("images/smile.jpeg")
		print("image read")
		image = resize_img(image, width = 600)
		(h, w) = image.shape[:2]

		# construct a blob from the image, set the input, and then
		# perform a forward pass of the network
		#blobFromImage Parameters: input image, scale factor,size, mean(of RGB), 
		blob = cv.dnn.blobFromImage(image, 1.0, (w, h),
			(103.939, 116.779, 123.680), swapRB=False, crop=False)
		# set the input to the pre-trained deep learning network and obtain
        # the output predicted probabilities for each of the 1,000 ImageNet
        # classes
		net.setInput(blob)
		output = net.forward()

		# reshape the output tensor, add back in the mean subtraction,
		# and then swap the channel ordering
		output = output.reshape((3, output.shape[2], output.shape[3]))
		output[0] += 103.939
		output[1] += 116.779
		output[2] += 123.680
		output /= 255.0
		output = output.transpose(1, 2, 0)
		# Printing the inference time
		# if FLAGS.print_inference_time:
		# 	print ('[INFO] The model ran in {:.4f} seconds'.format(end-start))


		st.markdown("*Segmented Image:*")
		#st.image(image,width = 500)
		plt.figure(figsize=(12,8))
		plt.imshow(image)
		st.pyplot()

		st.markdown("*Legend:*")
		#st.image(output,width = 500)
		plt.figure(figsize=(12,8))
		plt.imshow(output)
		st.pyplot()

	# # show the image
	# if FLAGS.show_original_image:
	#     cv.imshow('Input Image', img)
	# cv.imshow('Stylized image', out)
	# print ('[INFO] Hit Esc to close!')
	# cv.waitKey(0)

	# if FLAGS.save_image_with_name is not None:
	#     cv.imwrite(FLAGS.save_image_with_name, out)

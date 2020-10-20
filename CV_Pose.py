import cv2 as cv 
import numpy as np 
import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image,ImageEnhance

def detect_pose():
    BODY_PARTS = { "Nose": 0, "Neck": 1, "RShoulder": 2, "RElbow": 3, "RWrist": 4,
               "LShoulder": 5, "LElbow": 6, "LWrist": 7, "RHip": 8, "RKnee": 9,
               "RAnkle": 10, "LHip": 11, "LKnee": 12, "LAnkle": 13, "REye": 14,
               "LEye": 15, "REar": 16, "LEar": 17, "Background": 18 }

    POSE_PAIRS = [ ["Neck", "RShoulder"], ["Neck", "LShoulder"], ["RShoulder", "RElbow"],
               ["RElbow", "RWrist"], ["LShoulder", "LElbow"], ["LElbow", "LWrist"],
               ["Neck", "RHip"], ["RHip", "RKnee"], ["RKnee", "RAnkle"], ["Neck", "LHip"],
               ["LHip", "LKnee"], ["LKnee", "LAnkle"], ["Neck", "Nose"], ["Nose", "REye"],
               ["REye", "REar"], ["Nose", "LEye"], ["LEye", "LEar"] ]
    
    net = cv.dnn.readNetFromTensorflow("graph_opt.pb")

    image = cv.imread("images/pose.jpg")
    
    inWidth = image.shape[0]
    inHeight = image.shape[1]

    image_display = image[:, :, [2, 1, 0]] # BGR -> RGB

    st.markdown("*Original image:*")
    plt.figure(figsize=(12,8))
    plt.imshow(image_display)
    st.pyplot()

    net.setInput(cv.dnn.blobFromImage(image, 1.0, (inWidth, inHeight), (127.5, 127.5, 127.5), swapRB=True, crop=False))
    out = net.forward()
    out = out[:, :19, :, :]  # MobileNet output [1, 57, -1, -1], we only need the first 19 elements
    # assert(len(BODY_PARTS) == out.shape[1])

    points = []
    for i in range(len(BODY_PARTS)):
        # Slice heatmap of corresponging body's part.
        heatMap = out[0, i, :, :]

        # Originally, we try to find all the local maximums. To simplify a sample
        # we just find a global one. However only a single pose at the same time
        # could be detected this way.
        _, conf, _, point = cv.minMaxLoc(heatMap)
        print(conf)
        x = (inWidth * point[0]) / out.shape[3]
        y = (inHeight * point[1]) / out.shape[2]
        # Add a point if it's confidence is higher than threshold.
        points.append((int(x), int(y))if conf > 0.1 else None)

    for pair in POSE_PAIRS:
        partFrom = pair[0]
        partTo = pair[1]
        assert(partFrom in BODY_PARTS)
        assert(partTo in BODY_PARTS)

        idFrom = BODY_PARTS[partFrom]
        idTo = BODY_PARTS[partTo]

        if points[idFrom] and points[idTo]:
            cv.line(image, points[idFrom], points[idTo], (0, 255, 0), 3)
            cv.ellipse(image, points[idFrom], (3, 3), 0, 0, 360, (0, 0, 255), cv.FILLED)
            cv.ellipse(image, points[idTo], (3, 3), 0, 0, 360, (0, 0, 255), cv.FILLED)

    t, _ = net.getPerfProfile()
    freq = cv.getTickFrequency() / 1000
    cv.putText(image, '%.2fms' % (t / freq), (10, 20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))

    # cv.imshow('OpenPose using OpenCV', frame)
    print("Ran Successfully...!!!")
    image_display = image[:, :, [2, 1, 0]] # BGR -> RGB

    st.markdown("*Pose Detected in Image:*")
    plt.figure(figsize=(12,8))
    plt.imshow(image_display)
    st.pyplot()
def main():
    """POSE DETECTION APP"""

    st.title("Pose Detection")
    st.write("Pose estimation is a computer vision technique that predicts and tracks the location of a person or object. This is done by looking at a combination of the pose and the orientation of a given person/object. ")

    choice = st.radio("", ("Show Demo", "Browse an Image"))
    st.write()

    # if choice == "Browse an Image":
    #     st.set_option('deprecation.showfileUploaderEncoding', False)
    #     image_file = st.file_uploader("Upload Image", type=['jpg','png','jpeg'])

    #     if image_file is not None:
    #         our_image = Image.open(image_file)  
    #         detect_pose(our_image)
            
    # elif choice == "Show Demo":
    #     our_image = Image.open("images/girl_image.jpg")
    detect_pose()


if __name__=='__main__':
    main()
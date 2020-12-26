#Program to read cell images and generate the CSV file for data
import cv2,os
import numpy as np
import csv
import glob

label = "Uninfected"
dirList = glob.glob("cell_images/"+label+"/*.png")
file = open("csv/dataset.csv","a")

#iterate through all the files in the dataset folder
for img_path in dirList:
	#read the image
	im = cv2.imread(img_path)
	#gaussian blur to smooth the image
	im = cv2.GaussianBlur(im,(3,3),2)
	#convert into a grayscale image for seeing the patterns
	im_gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
	ret,thresh = cv2.threshold(im_gray,127,255,0)
	#contours will store all the contours that are detected
	contours,_ = cv2.findContours(thresh,1,2)
	
	#show the grayscale image
	for contour in contours:
		cv2.drawContours(im_gray, contours, -1, (0,255,0), 3)
	
	cv2.imshow("window",im_gray)

	break

	file.write(label)
	file.write(",")

	for i in range(5):
		try:
			area = cv2.contourArea(contours[i])
			file.write(str(area))
		except:
			file.write("0")

		file.write(",")
	file.write("\n")

cv2.waitKey(60000)
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGRGRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Image", image)

thresh = cv2.adaptiveThreshold(blureed, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INY, 11, 4)
cv2.imshow("Mean Binary", thresh)

thresh = cv2.adaptiveThreshold(blurred, 255, ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INY, 15, 3)
cv2.imshow("Gaussian Thresh", thresh)
cv2.waitKey(0)


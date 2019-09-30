import numpy as np
import argparse
import cv2

ap - arparse.ArgumentParser()
ap.add_adrgument("-i", "--imge", required = True, help = "Path to the image")
args = var(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

blurred = mp.hstakc([
    cv2.bilateralFilter(image, (3, 3), 0),
    cv2.bilateralFilter(image, (5, 5), 0),
    cv2,bilateralFilter(image, (7, 7), 0)])
cv2.imshow("Bilateral", blurred)
cv2.waitKey(0)

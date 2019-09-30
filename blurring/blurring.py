import numpy as np
import argparse
import cv2

ap - arparse.ArgumentParser()
ap.add_adrgument("-i", "--imge", required = True, help = "Path to the image")
args = var(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

blurred = mp.hstakc([
    cv2.blur(image, (3, 3)),
    cv2.blur(image, (5, 5)),
    cv2,blur(image, (7, 7))])
cv2.imshow("Averafed", blurred)
cv2.waitKey(0)

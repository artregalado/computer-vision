import numpy as np
import cv2
from pathlib import Path
import argparse

# Create argument parser to run the script from command line
parser = argparse.ArgumentParser(description="Convert an image to gray scale")
parser.add_argument("path", metavar= "Filepath",  help="Path to the image", type=str)
args = parser.parse_args()


def convert_to_gray_scale(image_path):
    img = cv2.imread(image_path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Image", img_gray)
    cv2.waitKey()
    
if __name__ == "__main__":
    convert_to_gray_scale(image_path=args.path)
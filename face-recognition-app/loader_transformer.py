
import numpy as np
import matplotlib.pyplot as plt
import cv2
from pathlib import Path
import random

# Pseudocode
# Make data to apply transformations. 
# Create a list of tuples that contain each opencv image object and its label. 
# The label for each image will be the name of the file. 
# Using pathlib.Path traverse the directory structure to find all the files.
# use the name of each directory as name for the image and add the loop count.

counter = 1
image_name = []
image_objects = []

for filepath in Path("./face-recognition-app/training").rglob("*.jpg"):
    print(filepath)
    name: str = filepath.parent.name + "_" + str(counter)
    img_object: np.ndarray = cv2.imread(str(filepath))
    counter += 1
    image_name.append(name)
    image_objects.append(img_object)

images = list(zip(image_name, image_objects))
del image_name, image_objects

print("No. of images loaded and stored:" + " " +  str(len(images)))

# Print a random sample of 15 images to check if the data is correct.
sample =  random.sample(images, 15)
for image in sample:
    gray_image: np.ndarray = cv2.cvtColor(image[1], cv2.COLOR_BGR2GRAY)
    cv2.imshow(image[0], gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
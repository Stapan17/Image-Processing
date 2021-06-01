import glob
import cv2


images = glob.glob("Input Images/*.jpg")


for image in images:
    new_image = image[13:]
    print(new_image)

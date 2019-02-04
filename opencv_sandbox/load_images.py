#Reference :Bret B's A2
import cv2
import os
def load_images(directory):
    images = []
    image_files = os.listdir(os.getcwd() + "/" + directory)
    for image in sorted(image_files):
        if image.lower().endswith(".jpg"):
            print("Loading: " + directory+"/"+image)
            #correct for bgr and crop image down
            temp_photo = cv2.cvtColor(cv2.imread(directory+"/"+image, cv2.IMREAD_COLOR), cv2.COLOR_RGB2BGR)
            images.append(temp_photo)
    return images
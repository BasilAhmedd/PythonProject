import cv2
import numpy as np
from numpy.ma.core import compressed


def rle_encode(data):
    encoding = []
    prev_value = data[0]
    count = 1

    for value in data[1:]:
        if value == prev_value:
            count += 1
        else:
            encoding.extend([prev_value,count])
            prev_value = value
            count = 1

    encoding.extend([prev_value,count])
    return encoding
def rle_decode(encoded_data,shape):
    decoded_data = []
    for i in range(0,len(encoded_data),2):
        value = encoded_data[i]
        count = encoded_data[i+1]
        decoded_data.extend([value] * count)
    return  np.array(decoded_data).reshape(shape)


image_path = r"C:\Users\basel.abdella\Desktop\shit.bmp"

image = cv2.imread(image_path)

gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

width = int(gray_image.shape[1] * 0.5)
height = int(gray_image.shape[0] * 0.5)
dim = (width,height)
resized_image = cv2.resize(gray_image,dim,interpolation=cv2.INTER_AREA)


pixels = resized_image.flatten()


compressed_data=rle_encode(pixels)

comp_path = r"C:\Users\basel.abdella\Desktop\compressedlololo.bmp"
np.save("compressed_image.npy",np.array(compressed_data,dtype=np.uint16))

print("compression completed")


decompressed_data = rle_decode(compressed_data,resized_image.shape)
cv2.imwrite(comp_path,decompressed_data)

print(" decompressed successfully")





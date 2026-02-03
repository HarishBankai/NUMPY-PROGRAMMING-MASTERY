import numpy as np  
import imageio.v3 as iio
import matplotlib.pyplot as plt

raw_path = input("Enter the path name for the image : ")
imagepath = raw_path.replace('"', '').replace("'", "")

try:
    image = iio.imread(imagepath)
except Exception as e:
    print(f"Error loading image: {e}")
    exit()

filter_image=input("ENTER THE FILTER UPON THE IMAGE : ")

if filter_image == "grayscale":
    result=np.dot(image[...,:3], [0.299, 0.587, 0.114])
    plt.imshow(result)
    plt.title("GRAYSCALE IMAGE")
elif filter_image == "negative":
    result=255 - image
    plt.imshow(result)
    plt.title("NEGATIVE IMAGE")
elif filter_image == "brightness":
    result=np.clip(image + 50, 0, 255)
    plt.imshow(result)
    plt.title("Brightness Image")
elif filter_image == "contrast":
    result=np.clip(1.5 * image, 0, 255)
    plt.imshow(result)
    plt.title("Contrast Image")
else:
    print("Invalid light")

if result is not None:
    plt.figure(figsize=(8, 6))
    
    if filter_image == "grayscale":
        plt.imshow(result, cmap='gray')
    else:
        plt.imshow(result)
        
    plt.title(filter_image.upper())
    plt.axis('off')
    plt.show()
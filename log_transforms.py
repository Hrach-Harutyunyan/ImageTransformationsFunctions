# ----- Example Python program for logarithmic transformation of a Digital Image -----

# import Pillow modules
from PIL import Image
import math

"""
    s=T(r) = c * log(r+1)
    's' is the output image
    'r' is the input image
    ‘c’ is the scaling constant. 
    
    c = 255 / log(1 + Maximum pixel value from the input image).

    - When logarithmic transformation is applied onto a digital image, 
    the darker intensity values are given brighter values thus making
    the details present in darker or gray areas of the image more visible to human eyes.
    - The logarithmic transformation also scales down the brighter intensity values to lower values.
    - However, the brighter intensity values are not scaled down to the extent the darker intensity values are scaled up.
    - For a digital image with intensity values ranging from 0 to 255
    the transformation log(r+1) produces value in the range of 0 to 2.41.
"""


# Compute log
def log_transform(c, f):
    g = c * math.log(float(1 + f), 10)
    return g


# Apply logarithmic transformation for an image
def log_transform_image(image, output_max=255, input_max=255):
    c = output_max / math.log(input_max + 1, 10)

    # Read pixels and apply logarithmic transformation
    for i in range(0, img.size[0] - 1):

        for j in range(0, img.size[1] - 1):
            # Get pixel value at (x,y) position of the image
            f = img.getpixel((i, j))

            # Do log transformation of the pixel
            red_pixel = round(log_transform(c, f[0]))
            green_pixel = round(log_transform(c, f[1]))
            blue_pixel = round(log_transform(c, f[2]))

            # Modify the image with the transformed pixel values
            img.putpixel((i, j), (red_pixel, green_pixel, blue_pixel))
    return image


# Display the original image
image_fileName = "Lenna.png"
img = Image.open(image_fileName)
img.show()

# Display the image after applying the logarithmic transformation
log_transformed_image = log_transform_image(img)
log_transformed_image.show()

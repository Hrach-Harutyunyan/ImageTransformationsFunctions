#----- Example Python program for negative transformation of a Digital Image ----
# import Pillow modules
from PIL import Image
# from PIL import ImageFilter

"""
    - The output of image inversion is a negative of a digital image.
    - In a digital image the intensity levels vary from 0 to L-1.
    - When an image is inverted, each of its pixel value ‘r’ is subtracted
      from the maximum pixel value L-1 and the original pixel is replaced 
      with the result ‘s’.
    - Image inversion or Image negation helps finding the details from the
      darker regions of the image.

      s = L - 1 - r.
"""

# Load the image
img = Image.open("Lenna.png")

# Display the original image
img.show()

# Read pixels and apply negative transformation
for i in range(0, img.size[0]-1):
    for j in range(0, img.size[1]-1):
        # Get pixel value at (x,y) position of the image
        pixel_color_vals = img.getpixel((i, j))
        # Invert color

        # Negate red pixel
        red_pixel = 255 - pixel_color_vals[0]
        # Negate green pixel
        green_pixel = 255 - pixel_color_vals[1]
        # Negate blue pixel
        blue_pixel = 255 - pixel_color_vals[2]

        # Modify the image with the inverted pixel values
        img.putpixel((i, j), (red_pixel, green_pixel, blue_pixel))

# Display the negative image
img.show()

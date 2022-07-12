from PIL import Image

"""
    - An alpha channel in an image introduces transparency to the Image.
    - Alpha blending combines two images by applying an alpha value to the images.
    - Pillow –Python Image Processing Library provides blend() method as part of the 
    Image class implementation.
    - When Image1 and Image2 are blended using alpha value 0, Image1 is returned as 
    and vice versa when the alpha value is 1.
    - When the alpha value varies from 0 to 1 and beyond, interpolation is used to determine the color value given by the formula
    
    out = ((int) input1[x] + alpha * ((int) input2[x] - (int) input1[x]));
"""


# Function to change the image size
def change_image_size(max_width, max_height, image):
    width_ratio = max_width/image.size[0]
    height_ratio = max_height/image.size[1]

    new_width = int(width_ratio * image.size[0])
    new_height = int(height_ratio * image.size[1])

    new_image = image.resize((new_width, new_height))
    return new_image


# Take two images for blending them together
image1 = Image.open("horse.png")
image2 = Image.open("Lenna.png")

# Make the images of uniform size
image3 = change_image_size(800, 500, image1)
image4 = change_image_size(800, 500, image2)

# Make sure images got an alpha channel
image5 = image3.convert("RGBA")
image6 = image4.convert("RGBA")

# Display the images
image5.show()
image6.show()

# alpha-blend the images with varying values of alpha
alphaBlended1 = Image.blend(image5, image6, alpha=.2)
alphaBlended2 = Image.blend(image5, image6, alpha=.4)

# Display the alpha-blended images
alphaBlended1.show()
alphaBlended2.show()
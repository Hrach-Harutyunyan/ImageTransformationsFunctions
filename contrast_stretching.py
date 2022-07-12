from PIL import Image

"""
    - Contrast stretching of an image modifies the pixel values of the image 
      in such a way that the intensities are transformed into a bigger range.
    - Contrast stretching is a linear operation which means the value of the 
      new pixel linearly varies based on the value of original pixel.

    I_output = (I_input - Min_i) * (((Max_o - Min_o) / (Max_i - Min_i)) + Min_o)
    I_output - Output pixel value
    I_input - Input pixel value
    Min_i - Minimum pixel value in the input image
    Max_i  - Maximum pixel value in the input image
    Min_o  - Minimum pixel value in the output image
    Max_o - Maximum pixel value in the output image 
    
"""


# Method to process the red band of the image
def normalize_red(intensity):
    intensity_input = intensity
    min_input = 86
    max_input = 230
    min_output = 0
    max_output = 255
    image_output = (intensity_input-min_input) *\
                   (((max_output-min_output)/(max_input-min_input)) + min_output)
    return image_output


# Method to process the green band of the image
def normalize_green(intensity):
    intensity_input = intensity
    min_input = 90
    max_input = 225
    min_output = 0
    max_output = 255
    image_output = (intensity_input-min_input) *\
                   (((max_output-min_output)/(max_input-min_input)) + min_output)
    return image_output


# Method to process the blue band of the image
def normalize_blue(intensity):
    intensity_input = intensity
    min_input = 100
    max_input = 210
    min_output = 0
    max_output = 255
    image_output = (intensity_input-min_input) *\
                   (((max_output-min_output)/(max_input-min_input)) + min_output)
    return image_output


# Create an image object

imageObject = Image.open("Lenna.png")

# Split the red, green and blue bands from the Image

multiBands = imageObject.split()

# Apply point operations that does contrast stretching on each color band

normalizedRedBand = multiBands[0].point(normalize_red)

normalizedGreenBand = multiBands[1].point(normalize_green)

normalizedBlueBand = multiBands[2].point(normalize_blue)


# Create a new image from the contrast stretched red, green and blue brands

normalizedImage = Image.merge("RGB", (normalizedRedBand, normalizedGreenBand, normalizedBlueBand))


# Display the image before contrast stretching

imageObject.show()


# Display the image after contrast stretching

normalizedImage.show()



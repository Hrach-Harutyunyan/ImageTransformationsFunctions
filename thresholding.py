# Example Python Program for thresholding

from PIL import Image


# Method to process the red band
def pixel_proc_red(intensity):
    return 0


# Method to process the blue band
def pixel_proc_blue(intensity):
    return intensity


# Method to process the green band
def pixel_proc_green(intensity):
    return 0


# Create an image object
imageObject = Image.open("horse.png")


# Split the red, green and blue bands from the Image
multiBands = imageObject.split()


# Apply point operations that does thresholding on each color band
redBand = multiBands[0].point(pixel_proc_red)

greenBand = multiBands[1].point(pixel_proc_green)

blueBand = multiBands[2].point(pixel_proc_blue)


# Display the individual band after thresholding
redBand.show()

greenBand.show()

blueBand.show()


# Create a new image from the thresholded red, green and blue brands
newImage = Image.merge("RGB", (redBand, greenBand, blueBand))


# Display the merged image after thresholding
newImage.show()

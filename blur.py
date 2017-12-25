# Import the modules
from PIL import Image, ImageFilter

try:
    # Load an image from the hard drive
    original = Image.open("../py/rs.png")

    # Blur the image
    blurred = original.filter(ImageFilter.BLUR)

    # save the new image
    blurred.save("blurred.png")
    print(original.size)
    print (blurred.size)

except:
    print ("Unable to load image")

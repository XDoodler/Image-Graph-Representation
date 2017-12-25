# Import the modules
from PIL import Image, ImageFilter

try:
    # Load an image from the hard drive
    original = Image.open("../dog.png")
    print("PIXELS:::::")
    print(original.size)
   

except:
    print ("Unable to load image")

import pytesseract
from PIL import Image


def readImage(imageLocation):
    return(pytesseract.image_to_string(Image.open(imageLocation)))

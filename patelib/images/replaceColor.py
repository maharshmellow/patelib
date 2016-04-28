from PIL import Image
import sys


def replaceColor(image, oldColor, newColor):
    """
    image = location to image
    oldColor = (r, g, b)
    newColor = (r, g, b)
    """
    img = Image.open(image)
    img = img.convert("RGBA")

    pixdata = img.load()

    for y in range(img.size[1]):
        for x in range(img.size[0]):
            if pixdata[x, y] == (oldColor[0], oldColor[1], oldColor[2], 255):
                pixdata[x, y] = (newColor[0], newColor[1], newColor[2], 255)

    img.save(image)

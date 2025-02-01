# Author: Davi Carvalho de Souza
# numpy
import numpy as np

# image reader
import matplotlib.pylab as plt

# web page opener
import webbrowser

# logger file
from log import Log

# image processor file
import processor

# reader file
import reader

###############################
# STEPS
#
# 1. Acess the image
#   1.1. Use plt.imread(<path>) to read the image as a numpy array
#   1.2. Convert the numpy array to a list using nparray.tolist()
# 2. Get the center row (assuming the image contains a valid bar code)
#   2.1. matplotlib reads images in the form (height, width, channels), so rows and columns.
# 3. Convert the color list into a list of 0s and 1s
# 4. Find the first guard bar
#   4.1. Assume every pixel that's not completly black, (0,0,0) to (80,80,80), is white (some images have gray in some spots instead of white)
# 5. Get the width of the first black bar (register its width as 1 unit)
# 6. Resize the array
# 7. Break the array into parts based on the guard bars (10101 pattern)
# 8. Identify each side of the code bar
# 9. Fix eventual upside down readings
# 10. Identify each digit
# 11. Check the digits read with the check digit formula
# 12. Fix up to one missread digit
# 13. Indentify the product
#   13.1. Open page webbrowser.open('https://www.barcodelookup.com/<code>')
################################

# main function
@Log.log
def main(imagepath : str) -> None:
    # 1.
    img = plt.imread(imagepath)     # 1.1.
    img = img.tolist()              # 1.2.
    imgHeight = len(img)

    # 2.
    centerRow : list[list[int]] = img[int(imgHeight/2)]
    
    # 3.
    centerRow : list[int] = processor.listlist2list(centerRow)
    centerRow : list[int] = processor.colorlist2binarylist(centerRow, 30)

    # 4., 5. and 6.
    code : list[int] = reader.resizeBinaryList(centerRow)

    # 7.
    codeSides : list[list[list[int]]] = reader.breakCodeIntoSides(code)

    # checking the validity of the code sides
    if len(codeSides[0]) % 6 != 0 or len(codeSides[1]) % 6 != 0:
        print("There was an error while attempting to read the code")
        return

    # 8. and 9. 
    # The codes are valid from here on
    encodedNumbers : list[str] = reader.fixSides(codeSides)

    # 10.
    # decoding the numbers
    decodedNumbers : list[int] = reader.decode(encodedNumbers)

    # 11.
    # checking the amount of unknown digits
    if reader.countUnknowns(decodedNumbers) >= 2:
        print("Too many digits couldn't be read")
        return 

    # checking the validity of the code
    if not(reader.isCodeValid(decodedNumbers)):
        print("The code is unvalid")
        return

    # 12.
    # fixing missing digits
    if not(reader.isCodeComplete(decodedNumbers)):
        decodedNumbers = reader.fixUnknown(decodedNumbers)

    # The code is valid from now on
    numberString : str = reader.numberString(decodedNumbers)
    
    # 13.
    # opening product page on the browser
    webbrowser.open(f"https://www.barcodelookup.com/{numberString}")

# checking main
if __name__ == "__main__":
    images = [
        "076950450479.jpg",     # does not work (gray noise)
        "705632441947.jpg",     # does not work (gray noise)
        "binaryex.jpg",         # works
        "binaryex2.jpg",        # works
        "binaryexRev.jpg",      # works         (upside down)
        "broken1.jpg",          # works         (one damaged pixel)
        "tooBroken.jpg"         # does not work (too damaged)
    ]

    main(f"images/{images[5]}")
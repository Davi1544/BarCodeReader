# numpy
import numpy as np

# image reader
import matplotlib.pylab as plt

# web page opener
import webbrowser

# logger file
import log

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
    codeSides : list[list[int]] = reader.breakCodeIntoSides(code)

    # checking the validity of the code sides
    if len(codeSides[0]) % 7 != 0 or len(codeSides[1]) % 7 != 0:
        print("There was an error while attempting to read the code.")
        return

    # the codes are valid from here on
    print(len(codeSides[0]) % 7)
    print(len(codeSides[1]) % 7)

# checking main
if __name__ == "__main__":
    images = [
        "076950450479.jpg",
        "705632441947.jpg",
        "binaryex.jpg",
        "binaryex2.jpg"
    ]

    main(f"images/{images[0]}")
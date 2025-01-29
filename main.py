# numpy
import numpy as np

# image reader
import matplotlib.pylab as plt

# web page opener
import webbrowser

# logger file
import log

# helper file
import helper

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
#   4.1. Assume every pixel that's not completly black, (0,0,0) to (10,10,10), is white (some images have gray in some spots instead of white)
# 5. Get the width of the first black bar (register its width as 1 unit)
# 6. Resize the array and turn it into a string
# 7. Pass the string to the reader
# 8. Break the string into parts based on the guard bars (01010 pattern)
# 9. Identify each side of the code bar
# 10. Fix eventual upside down readings
# 11. Identify each digit
# 12. Check the digits read with the check digit formula
# 13. Fix up to one missread digit
# 14. Indentify the product
#   14.1. Open page webbrowser.open('https://www.barcodelookup.com/<code>')
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
    centerRow : list[int] = helper.listlist2list(centerRow)
    centerRow : list[int] = helper.colorlist2binarylist(centerRow)

# checking main
if __name__ == "__main__":
    main("images/076950450479.jpg")
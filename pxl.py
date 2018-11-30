import sys
import math
from PIL import Image
from PIL import ImageColor

import palettes

# Usage: python pxl.py <square size> <color options> <method> <file>

# Available Methods:
# 0 - Limit each band to a certain number of values. (i.e. 5 red, 5 green, 5 blue possiblities)
# 1 - Get a color from from an existing palette based on euclidean distance between the actual color and the palette colors.

def main():
    pSize = int(sys.argv[1])
    colors = int(sys.argv[2])
    method = int(sys.argv[3])
    f = sys.argv[4]

    paletteRGB = map(ImageColor.getrgb, palettes.endsega)

    if method == 0:
        run(f, pSize, colors, method)
    elif method == 1:
        run(f, pSize, paletteRGB, method)

def run(file, pSize, colors, method):
    """ Run the filter for a file with a certain square size and number of possible colors """
    original = Image.open(file)
    new = pixelate(original, pSize, colors, method)
    new.show()

def pixelate(original, pSize, colors, method):
    """ Pixelates an image with a certain square size and number of possible colors"""
    newImage = Image.new("RGB", (original.size))
    oPixels = original.load()
    nPixels = newImage.load()

    bCol = 0
    while bCol < original.size[0]:
        bRow = 0
        while bRow < original.size[1]:
            rs = []
            gs = []
            bs = []

            # Gets the colors of each pixel in this square
            for pCol in range(bCol, bCol + pSize):
                for pRow in range(bRow, bRow + pSize):
                    if pCol >= original.size[0] or pRow >= original.size[1]:
                        continue

                    pix = oPixels[pCol, pRow]
                    rs.append(pix[0])
                    gs.append(pix[1])
                    bs.append(pix[2])

            # Get the average color of this square
            avgR = sum(rs)/len(rs)
            avgG = sum(gs)/len(gs)
            avgB = sum(bs)/len(bs)

            if method == 0:
                color = getColorByRoundingBands((avgR, avgG, avgB), colors)
            elif method == 1:
                color = getColorFrompalette((avgR, avgG, avgB), colors)

            # Build this square in the new image.
            for pCol in range(bCol, bCol + pSize):
                for pRow in range(bRow, bRow + pSize):
                    if pCol >= original.size[0] or pRow >= original.size[1]:
                        continue
                    nPixels[pCol, pRow] = color

            bRow += pSize
        bCol += pSize

    return newImage

def getColorByRoundingBands(color, colorCount):
    """ Generates a color based on the average color. This will limit the possible colors per band to `colorCount` """
    def getClosest(val):
        size = 255 / colorCount
        cur = 255 - size

        while cur >= 0:
            if val > cur:
                return cur

            cur -= size

        return 0

    r = getClosest(color[0])
    g = getClosest(color[1])
    b = getClosest(color[2])

    return (r, g, b)

def getColorFrompalette(color, palette):
    """ Generates a color by finding the most similar color from a specified color palette """
    def get_diffs(c):
        return (euclidean_difference(c, color), c)

    diffs = map(get_diffs, palette)
    return min(diffs, key = lambda t: t[0])[1]

def euclidean_difference(c1, c2):
    return math.sqrt( ((c2[0] - c1[0]) ** 2) + ((c2[1] - c1[1]) ** 2) + ((c2[2] - c1[2]) ** 2) )

if __name__ == '__main__':
    main()

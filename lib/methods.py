import math
from PIL import ImageColor
from . import palettes

def generateLimitBands(colorCount):
    def getColor(color):
        """ Limits the possible colors per band to `colorCount`. """
        span = 255.0 / colorCount
        firstSeparator = span / 2

        separators = [firstSeparator + (i * span) for i in range(colorCount)]

        def getClosest(val):
            for (j, sep) in enumerate(separators):
                if val < sep:
                    return int(j * span)

            return 255

        r = getClosest(color[0])
        g = getClosest(color[1])
        b = getClosest(color[2])

        return (r, g, b)

    return getColor

def generateToPalette(paletteName, mode):
    def getColor(color):
        """ Generates a color by finding the most similar color from a specified color palette. """

        def euclideanDifference(c1, c2):
            return math.sqrt( ((c2[0] - c1[0]) ** 2) + ((c2[1] - c1[1]) ** 2) + ((c2[2] - c1[2]) ** 2) )

        def weightedEuclideanDifference(c1, c2):
            return math.sqrt( (((c2[0] - c1[0]) * 0.3) ** 2) + (((c2[1] - c1[1]) * 0.59) ** 2) + (((c2[2] - c1[2]) * 0.11) ** 2) )

        def closestValue(c1, c2):
            v1 = (c1[0] + c1[1] + c1[2]) / 3.0
            v2 = (c2[0] + c2[1] + c2[2]) / 3.0
            return abs(v2 - v1)

        def get_diffs(c):
            if mode == 'color':
                return (weightedEuclideanDifference(c, color), c)
            if mode == 'value':
                return (closestValue(c, color), c)

        if paletteName in palettes.palettes:
            palette = palettes.palettes[paletteName]
            paletteRGB = map(ImageColor.getrgb, palette)
            diffs = map(get_diffs, paletteRGB)
            return min(diffs, key = lambda t: t[0])[1]
        else:
            raise InvalidPaletteException(paletteName)

        return (0, 0, 0)

    return getColor

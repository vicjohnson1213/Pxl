import math
from PIL import ImageColor
from ..exceptions import InvalidPaletteException

from palettes import palettes

def generateGetColor(paletteName):
    def getColor(color):
        """ Generates a color by finding the most similar color from a specified color palette """

        def euclideanDifference(c1, c2):
            return math.sqrt( ((c2[0] - c1[0]) ** 2) + ((c2[1] - c1[1]) ** 2) + ((c2[2] - c1[2]) ** 2) )

        def weightedEuclideanDifference(c1, c2):
            return math.sqrt( (((c2[0] - c1[0]) * 0.3) ** 2) + (((c2[1] - c1[1])*0.59) ** 2) + (((c2[2] - c1[2])*0.11) ** 2) )

        def get_diffs(c):
            return (weightedEuclideanDifference(c, color), c)

        if paletteName in palettes:
            palette = palettes[paletteName]
            paletteRGB = map(ImageColor.getrgb, palette.colors)
            diffs = map(get_diffs, paletteRGB)
            return min(diffs, key = lambda t: t[0])[1]
        else:
            raise InvalidPaletteException(paletteName)

        return (0, 0, 0)

    return getColor

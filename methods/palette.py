import math
from PIL import ImageColor

import palettes

def generateGetColor(paletteName):
    def getColor(color):
        """ Generates a color by finding the most similar color from a specified color palette """

        availablePalettes = {
            'endsega': palettes.endsega,
            'sweetie': palettes.sweetie
        }

        def euclidean_difference(c1, c2):
            return math.sqrt( ((c2[0] - c1[0]) ** 2) + ((c2[1] - c1[1]) ** 2) + ((c2[2] - c1[2]) ** 2) )

        def get_diffs(c):
            return (euclidean_difference(c, color), c)

        if paletteName in availablePalettes:
            palette = availablePalettes[paletteName]
            paletteRGB = map(ImageColor.getrgb, palette.colors)
            diffs = map(get_diffs, paletteRGB)
            return min(diffs, key = lambda t: t[0])[1]

        return (0, 0, 0)

    return getColor

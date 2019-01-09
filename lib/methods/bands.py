def generateGetColor(colorCount):
    def getColor(color):
        """ Generates a color based on the average color. This will limit the possible colors per band to `colorCount` """
        span = 255.0 / colorCount
        firstSeparator = span / 2

        separators = map(lambda i: firstSeparator + (i * span), range(colorCount))

        def getClosest(val):
            for (i, sep) in enumerate(separators):
                if val < sep:
                    return int(i * span)

            return 255

        r = getClosest(color[0])
        g = getClosest(color[1])
        b = getClosest(color[2])

        return (r, g, b)

    return getColor

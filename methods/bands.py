def generateGetColor(colorCount):
    def getColor(color):
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

    return getColor

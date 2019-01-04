class InvalidPaletteException(Exception):
    def __init__(self, palette):
        self.palette = palette

    def __str__(self):
        return "Invalid palette: '{0}'".format(self.palette)

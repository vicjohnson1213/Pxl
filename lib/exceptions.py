class PxlException(Exception):
    pass

class FileDoesNotExistException(PxlException):
    def __init__(self, filepath):
        self.filepath = filepath

    def __str__(self):
        return "Invalid filepath: '{0}'".format(self.filepath)

class InvalidPaletteException(PxlException):
    def __init__(self, palette):
        self.palette = palette

    def __str__(self):
        return "Invalid palette: '{0}'".format(self.palette)

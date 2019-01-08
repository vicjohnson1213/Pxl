class FileDoesNotExistException:
        def __init__(self, filepath):
            self.filepath = filepath

        def __str__(self):
            return "Invalid filepath: '{0}'".format(self.filepath)

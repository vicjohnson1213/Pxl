import sys
import argparse

import lib.exceptions as exceptions
from lib import pixelate as pxl
from lib.methods.palettes import palettes

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    parser.add_argument('output')
    parser.add_argument('size', type=int)

    subparsers = parser.add_subparsers(dest='command')

    bandsParser = subparsers.add_parser('bands')
    bandsParser.add_argument('-c', '--count', type=int)

    paletteParser = subparsers.add_parser('palette')
    paletteParser.add_argument('-p', '--palette')

    options = parser.parse_args()

    try:
        pxl.pixelate(options)
    except exceptions.InvalidPaletteException as ex:
        print "Invalid palette: '{0}'".format(ex.palette)
        print ''
        print 'Available palettes:'

        for palette in palettes:
            print '    {0}'.format(palette)
        sys.exit(1)

    except exceptions.FileDoesNotExistException as ex:
        print "Invalid filepath: '{}'".format(ex.filepath)
        sys.exit(1)

if __name__ == '__main__':
    main()

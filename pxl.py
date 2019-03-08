import sys
import argparse

from lib import exceptions
from lib import PXL
from lib import palettes

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    parser.add_argument('output')
    parser.add_argument('size', type=int)

    subparsers = parser.add_subparsers(dest='command')

    bandsParser = subparsers.add_parser('limitBands')
    bandsParser.add_argument('count', type=int)

    paletteParser = subparsers.add_parser('toPalette')
    paletteParser.add_argument('palette')
    paletteParser.add_argument('-m', '--mode', default='color')

    options = parser.parse_args()

    try:
        PXL.pixelate(options)
    except exceptions.InvalidPaletteException as ex:
        print("Invalid palette: '{0}'".format(ex.palette))
        print('')
        print('Available palettes:')

        for palette in palettes.palettes:
            print('    {0}'.format(palette))
        sys.exit(1)

    except exceptions.FileDoesNotExistException as ex:
        print("Invalid filepath: '{}'".format(ex.filepath))
        sys.exit(1)


if __name__ == '__main__':
    main()

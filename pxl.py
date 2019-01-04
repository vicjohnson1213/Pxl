import argparse
from lib import pixelate
from lib.exceptions import InvalidPaletteException
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
        pixelate(options)
    except InvalidPaletteException as ex:
        print "Invalid palette: '{0}'".format(ex.palette)
        print ''
        print 'Available palettes:'

        for palette in palettes:
            print '    {0}'.format(palette)

if __name__ == '__main__':
    main()

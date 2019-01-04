import argparse
from lib import pixelate as PXL

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
    PXL.pixelate(options)

if __name__ == '__main__':
    main()

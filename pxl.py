import argparse
from PIL import Image

import methods

def pixelate(filepath, pixelSize, getColor):
    original = Image.open(filepath)

    newImage = Image.new("RGB", (original.size))
    originalPixels = original.load()
    newPixels = newImage.load()

    blockColumn = 0
    while blockColumn < original.size[0]:
        blockRow = 0
        while blockRow < original.size[1]:
            reds = []
            greens = []
            blues = []

            # Gets the colors of each pixel in this square
            for pixelColumn in range(blockColumn, blockColumn + pixelSize):
                for pixelRow in range(blockRow, blockRow + pixelSize):
                    if pixelColumn >= original.size[0] or pixelRow >= original.size[1]:
                        continue

                    pix = originalPixels[pixelColumn, pixelRow]
                    reds.append(pix[0])
                    greens.append(pix[1])
                    blues.append(pix[2])

            # Get the average color of this square
            avgR = sum(reds)/len(reds)
            avgG = sum(greens)/len(greens)
            avgB = sum(blues)/len(blues)

            filteredColor = getColor((avgR, avgG, avgB))

            # Build this square in the new image.
            for pixelColumn in range(blockColumn, blockColumn + pixelSize):
                for pixelRow in range(blockRow, blockRow + pixelSize):
                    if pixelColumn >= original.size[0] or pixelRow >= original.size[1]:
                        continue
                    newPixels[pixelColumn, pixelRow] = filteredColor

            blockRow += pixelSize
        blockColumn += pixelSize

    newImage.show()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    parser.add_argument('-s', '--size', type=int)
    parser.add_argument('-o', '--output')

    subparsers = parser.add_subparsers(dest='command')

    bandsParser = subparsers.add_parser('bands')
    bandsParser.add_argument('-c', '--count', type=int)

    paletteParser = subparsers.add_parser('palette')
    paletteParser.add_argument('-p', '--palette')

    args = parser.parse_args()

    if args.command == 'bands':
        pixelate(args.input, args.size, methods.bands.generateGetColor(args.count))
    elif args.command == 'palette':
        pixelate(args.input, args.size, methods.palette.generateGetColor(args.palette))

if __name__ == '__main__':
    main()

from PIL import Image

from exceptions import FileDoesNotExistException
import methods

def pixelate(options):
    if options.command == 'bands':
        getColor = methods.bands.generateGetColor(options.count)
    elif options.command == 'palette':
        getColor = methods.palette.generateGetColor(options.palette)

    try:
        originalImage = Image.open(options.input)
    except IOError as ex:
        raise FileDoesNotExistException(options.input)

    newImage = Image.new("RGB", (originalImage.size))
    originalPixels = originalImage.load()
    newPixels = newImage.load()

    blockColumn = 0
    while blockColumn < originalImage.size[0]:
        blockRow = 0
        while blockRow < originalImage.size[1]:
            averages = getAverageForBlock(blockColumn, blockRow, options.size, originalImage.size, originalPixels)
            filteredColor = getColor(averages)

            for pixelColumn in range(blockColumn, blockColumn + options.size):
                for pixelRow in range(blockRow, blockRow + options.size):
                    if pixelColumn >= originalImage.size[0] or pixelRow >= originalImage.size[1]:
                        continue
                    newPixels[pixelColumn, pixelRow] = filteredColor

            blockRow += options.size
        blockColumn += options.size

    newImage.save(options.output)

def getAverageForBlock(columnStart, rowStart, pixelSize, size, originalPixels):
    reds = []
    greens = []
    blues = []

    # Gets the colors of each pixel in this square
    for pixelColumn in range(columnStart, columnStart + pixelSize):
        for pixelRow in range(rowStart, rowStart + pixelSize):
            if pixelColumn >= size[0] or pixelRow >= size[1]:
                continue

            pix = originalPixels[pixelColumn, pixelRow]
            reds.append(pix[0])
            greens.append(pix[1])
            blues.append(pix[2])

    avgR = sum(reds)/len(reds)
    avgG = sum(greens)/len(greens)
    avgB = sum(blues)/len(blues)

    return (avgR, avgG, avgB)

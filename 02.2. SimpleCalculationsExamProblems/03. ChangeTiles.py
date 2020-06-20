width = float(input())
tileWidth = float(input())
tileLength = float(input())
benchWidth = float(input())
benchLength = float(input())

fullArea = width * width
tileArea = tileWidth * tileLength
benchArea = benchWidth * benchLength

tilesCount = (fullArea - benchArea) / tileArea
time = tilesCount * 0.2
print(tilesCount)
print(time)

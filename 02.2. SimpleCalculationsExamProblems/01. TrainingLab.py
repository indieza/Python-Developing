import math

l = float(input()) * 100
w = float(input()) * 100

rows = math.trunc(l / 120)
cols = math.trunc((w - 100) / 70)

print(math.trunc(rows * cols - 3))

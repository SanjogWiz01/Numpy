import numpy as np
import imageio.v3 as iio
img = iio.imread('cat.png')

print("Max:", img.max())
print("Min:", img.min())
print("Mean:", img.mean())
import imageio.v3 as iio
import matplotlib.pyplot as plt

img = iio.imread('Advance numpy operation\cat.png')
plt.imshow(img)
plt.axis('off') 
plt.title("Curious Raccoon")
plt.show()
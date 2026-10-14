import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
from skimage.transform import iradon


def main():
    sinogram = imread("source/sinogram.png").astype(float) # (radial bins, angles)
    image = reconstruct(sinogram)

    # np.save("image.npy", image)
    plt.imsave("image.png", image, cmap="gray")

def reconstruct(sinogram):
    # TODO
    img = sinogram

    return img

if __name__ == "__main__":
    main()

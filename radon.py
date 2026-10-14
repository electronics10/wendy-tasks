import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.transform import radon


def main():
    image = np.load("image.npy") #imread("image.png").astype(float)
    if image.ndim == 3:
        image = rgb2gray(image[..., :3])
    sinogram = project(image)

    plt.imsave("sino.png", sinogram, cmap="gray")

def project(image):
    theta = np.linspace(0.0, 180.0, int(max(image.shape)), endpoint=False)
    sinogram = radon(image, theta=theta, circle=True)

    return sinogram

if __name__ == "__main__":
    main()

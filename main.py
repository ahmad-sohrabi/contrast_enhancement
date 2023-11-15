import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

from functions import *
from tkinter import *


if __name__ == '__main__':
    my_image = cv.imread("ldr1.jpg")
    rgb_image = cv.cvtColor(my_image, cv.COLOR_BGR2GRAY)
    # plt.hist(rgb_image)
    plt.imshow(rgb_image, cmap="gray")
    plt.show()
    total_pixels_number = rgb_image.shape[0] * rgb_image.shape[1]
    """print(f"image depth: {rgb_image.shape}")

    histg = cv.calcHist([rgb_image], [0], None, [256], [0, 256])
    plt.plot(histg)
    plt.show()

    cropped_image = image_crop(rgb_image, (0, 0), (500, 500))
    plt.imshow(cropped_image, cmap="gray")

    equalized_image_histogram = calculate_equalized_histogram(histg)
    plt.plot(equalized_image_histogram)
    print(equalized_image_histogram.shape)

    equalized_image = rgb_image.copy()
    for i in range(rgb_image.shape[0]):
        for j in range(rgb_image.shape[1]):
            equalized_image[i, j] = equalized_image_histogram[rgb_image[i, j]]
    plt.imshow(equalized_image, cmap="gray")

    histg = cv.calcHist([equalized_image], [0], None, [256], [0, 256])
    plt.plot(histg)
    plt.show()

    print(f"min is {np.amax(rgb_image)}")

    stretched_image = linear_stretch(rgb_image, 0, 255)
    plt.imshow(stretched_image, cmap="gray")
    print(np.amin(stretched_image))"""

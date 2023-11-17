import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv


def load_image(file_address):
    my_image = cv.imread(file_address)
    main_image = cv.cvtColor(my_image, cv.COLOR_BGR2RGB)
    return main_image


def load_image_gray_scale(file_address):
    my_image = cv.imread(file_address)
    gray_image = cv.cvtColor(my_image, cv.COLOR_BGR2GRAY)
    return gray_image


def calc_sum(hist, k, total_pixels_number):
    sum = 0
    for i in range(k + 1):
        sum += hist[i]

    sum = sum / total_pixels_number
    return sum


def calculate_equalized_histogram(histogram, total_pixels_number):
    equalized_histogram = np.array([])
    for i in range(256):
        sum = calc_sum(histogram, i, total_pixels_number)
        sum = int(sum * 255)
        equalized_histogram = np.append(equalized_histogram, sum)
    return equalized_histogram


def image_crop(image, startPoint, endPoint):
    shape_length = len(image.shape)
    if shape_length == 2:
        cropped_image = image[startPoint[0]:endPoint[0], startPoint[1]:endPoint[1]]
    else:
        cropped_image = image[startPoint[0]:endPoint[0], startPoint[1]:endPoint[1], :]
    return cropped_image


def linear_stretch(image, min_range, max_range):
    max_pixel = np.amax(image)
    min_pixel = np.amin(image)
    slope = (max_range - min_range) / (max_pixel - min_pixel)
    bias = min_range - slope * min_pixel
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            image[i, j] = slope * image[i, j] + bias
    return image

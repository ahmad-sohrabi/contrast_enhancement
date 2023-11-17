from functions import *

if __name__ == '__main__':
    """ 
    Loading & Showing the main Image using load_image Function
    Arguments of load_image(file_address) function are:
    1st argument: image file address
    """
    image_file = "ldr1.jpg"
    main_image = load_image(file_address=image_file)
    plt.figure(1).set_figheight(35)
    plt.figure(1).set_figwidth(20)
    plt.subplot(711)
    plt.imshow(main_image)
    main_image_rgb = cv.cvtColor(main_image, cv.COLOR_BGR2RGB)
    cv.imwrite("Main_Image.jpg", main_image_rgb)
    plt.title("Main Image")

    """
    Loading & Showing the Gray scale of Image using load_image_gray_scale Function
    Arguments of load_image_gray_scale(file_address) function are:
    1st argument: image file address
    """
    gray_image = load_image_gray_scale(file_address=image_file)
    cv.imwrite("Gray_Scale_Image.jpg", gray_image)
    plt.subplot(712)
    plt.imshow(gray_image, cmap="gray")
    plt.title("Gray Scale Image")

    """ 
    Cropping the image using image_crop Function
    Arguments of image_crop(image, startPoint, endPoint) function are:
    1st argument: image itself
    2nd argument: start point of cropping rectangle as a set e.g (0,0)
    3rd argument: start point of cropping rectangle as a set e.g (500,500)
    """
    image_width = gray_image.shape[0]
    image_height = gray_image.shape[1]
    cropped_image = image_crop(gray_image, (0, 0), (int(image_width / 2), int(image_height / 2)))
    cv.imwrite("Cropped_Image.jpg", cropped_image)
    plt.subplot(713)
    plt.imshow(cropped_image, cmap="gray")
    plt.title("Cropped Image")

    """ 
    Calculating Image Histogram and Equalized Histogram of the image using calculate_equalized_histogram Function
    Arguments of calculate_equalized_histogram(image_histogram, total_pixels_number) function are:
    1st argument: main image histogram
    2nd argument: total number of pixels (width * height)
    """
    total_pixels_number = image_width * image_height
    image_histogram = cv.calcHist([gray_image], [0], None, [256], [0, 256])
    plt.subplot(714)
    plt.hist(gray_image.ravel(), 256, [0, 256])
    plt.title("Image Histogram")

    equalized_image_histogram = calculate_equalized_histogram(image_histogram, total_pixels_number)
    equalized_image = gray_image.copy()
    for i in range(gray_image.shape[0]):
        for j in range(gray_image.shape[1]):
            equalized_image[i, j] = equalized_image_histogram[gray_image[i, j]]
    cv.imwrite("Equalized_Image.jpg", equalized_image)
    plt.subplot(715)
    plt.imshow(equalized_image, cmap="gray")
    plt.title("Equalized Image")

    plt.subplot(716)
    plt.hist(equalized_image.ravel(), 256, [0, 256])
    plt.title("Equalized Histogram")

    """ 
    Calculating stretched image using linear_stretch Function
    Arguments of linear_stretch(image, min_range, max_range) function are:
    1st argument: main image 
    2nd argument: minimum value for new expected dynamic range
    3rd argument: maximum value for new expected dynamic range
    """
    stretched_image = linear_stretch(gray_image, 0, 255)
    cv.imwrite("Stretched_Image.jpg", stretched_image)
    plt.subplot(717)
    plt.imshow(stretched_image, cmap="gray")
    plt.title("Stretched Image")
    plt.show()

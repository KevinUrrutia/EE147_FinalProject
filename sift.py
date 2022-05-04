import cv2 as cv
import numpy as np
from numba import jit
from itertools import product

def gen_gaussian_kernel(k_size, sigma):
    center = k_size // 2
    x, y = np.mgrid[0 - center : k_size - center, 0 - center : k_size - center]
    g = 1 / (2 * np.pi * sigma) * np.exp(-(np.square(x) + np.square(y)) / (2 * np.square(sigma)))
    return g

@jit()
def gaussian_filter(img, k_size, sigma):
    [rows, cols] = img.shape

    #create a resulting image to return from the function
    blur_img = np.zeros([rows, cols])

    #apply equal padding to all sides of the image to accomodate the kernel size
    padded_image = np.zeros([rows + 4, cols + 4])
    padded_image[int(2):int(-1 * 2), int(2):int(-1 * 2)] = img

    kernel = gen_gaussian_kernel(k_size, sigma)
    print(kernel)
    # iterate through the image to do the convolution
    for y in range(cols):
        for x in range(rows):
            blur_img[x, y] = ((kernel * padded_image[x: x+5, y: y + 5]).sum()) / 256

    return blur_img


def main():
    img = cv.imread("assets/pumpkins.jpg", cv.IMREAD_GRAYSCALE)
    cv.imshow("orig", img)

    # gaussian3x3 = gaussian_filter(img, 3, sigma=1)
    gaussian5x5 = gaussian_filter(img, 5, sigma=0.8)
    #create the scaled space for the image
        #entails blurring the image and shrinking the image for a number of octaves

    # cv.imshow("gaussian filter with 3x3 mask", gaussian3x3)
    cv.imshow("gaussian filter with 5x5 mask", gaussian5x5)

    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()

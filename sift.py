import cv2 as cv
import numpy as np
from numba import jit

@jit()
def gaussian_blur(img):
    #the kernel has the convoluted with every pixel in the image
    #The convolution operation is by specifying a central pixel coordinate and multiplying all of its nieghbors with the kernel. Then adding up all of the resulting multiplications and
    #placing those values in the original pixel location
    #There needs to be boundary condition checks when doing the covolution

    kernel = np.array([[1, 4, 6, 4, 1],
                       [4, 16, 24, 16, 4],
                       [6, 24, 36, 24, 6],
                       [4, 16, 24, 16, 4],
                       [1, 4, 6, 4, 1]])

    [rows, cols] = img.shape

    #create a resulting image to return from the function
    blur_img = np.zeros([rows, cols])

    #apply equal padding to all sides of the image to accomodate the kernel size
    padded_image = np.zeros([rows + 4, cols + 4])
    padded_image[int(2):int(-1 * 2), int(2):int(-1 * 2)] = img

    #iterate through the image to do the convolution
    for y in range(cols):
        for x in range(rows):
            print(padded_image[x: x + 5, y: y + 5])
            blur_img[x, y] = ((kernel * padded_image[x: x+5, y: y + 5]).sum()) / 256

    print(blur_img)
    return blur_img

def main():
    img = np.array([[1, 4, 6, 4, 1],
                   [4, 16, 24, 16, 4],
                   [6, 24, 36, 24, 6],
                   [4, 16, 24, 16, 4],
                   [1, 4, 6, 4, 1]])

    # img = cv.imread("assets/pumpkins.jpg", cv.IMREAD_GRAYSCALE)
    # cv.imshow("orig", img)

    # dst = cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)

    blur_img = gaussian_blur(img)
    # cv.imshow('blurred', blur_img)
    #create the scaled space for the image
        #entails blurring the image and shrinking the image for a number of octaves

    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()

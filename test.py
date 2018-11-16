import cv2
import numpy as np
from skimage.measure import compare_psnr, compare_mse

a = cv2.imread('lena.png')
b = cv2.imread('4:1:1_lena.png')
c = cv2.imread('4:2:0_lena.png')
d = cv2.imread('4:2:2_lena.png')
e = cv2.imread('4:4:4_lena.png')
	
ab = a == b


	
def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err


print(compare_mse(a,b),compare_psnr(a,b))
print(compare_mse(a,c),compare_psnr(a,c))
print(compare_mse(a,d),compare_psnr(a,d))
print(compare_mse(a,e),compare_psnr(a,e))
# print(b)
# print(c)





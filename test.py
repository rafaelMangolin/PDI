import cv2
import numpy as np

a = cv2.imread('beico.jpeg')
b = cv2.imread('4:1:1_beico.jpeg')
c = cv2.imread('4:2:0_beico.jpeg')
d = cv2.imread('4:2:2_beico.jpeg')
e = cv2.imread('4:4:4_beico.jpeg')
	
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


print(mse(a,b))
print(mse(a,c))
print(mse(a,d))
print(mse(a,e))
# print(b)
# print(c)





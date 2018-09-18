import numpy as np
import cv2

img = cv2.imread('image.jpg')

img_2 = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

Y, Cr, Cb = cv2.split(img_2)

# print(len(Y),len( Cb),len( Cr))

cb = Cb[::2,::2]
cr = Cr[::2,::2]

cb_2 = np.repeat(cb,2,axis=1)
cb_3 = np.repeat(cb_2,2,axis=0)
cb_4 = cb_3[:len(Y),:len(Y[0])]

cr_2 = np.repeat(cr,2,axis=1)
cr_3 = np.repeat(cr_2,2,axis=0)
cr_4 = cr_3[:len(Y),:len(Y[0])]

img_3 = cv2.merge([Y,cr_4,cb_4])

img_4 = cv2.cvtColor(img_3, cv2.COLOR_YCrCb2BGR)


cv2.imshow('imagem',img_4)

cv2.waitKey(0)
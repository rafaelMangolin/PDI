import numpy as np
import cv2
from PIL import Image

imagem = 'lena.png'


def chroma_subsampling(j,a,b):
	original = cv2.imread(imagem)
	img_1 = cv2.cvtColor(original, cv2.COLOR_BGR2YCrCb)
	Y, Cr, Cb = cv2.split(img_1)
	
	x = int(j/a)
	y = None
	if(int(b) == 0):
		y = 2
	else:
		y = 1

	cb = Cb[::y,::x]
	cb = np.repeat(cb,x,axis=1)
	cb = np.repeat(cb,y,axis=0)
	cb = cb[:len(Y),:len(Y[0])]

	cr = Cr[::y,::x]
	cr = np.repeat(cr,x,axis=1)
	cr = np.repeat(cr,y,axis=0)
	cr = cr[:len(Y),:len(Y[0])]

	img = cv2.merge([Y,cr,cb])
	img = cv2.cvtColor(img, cv2.COLOR_YCrCb2BGR)
	cv2.imwrite('{}:{}:{}_{}'.format(j,a,b,imagem),img)


chroma_subsampling(4,4,4)
chroma_subsampling(4,2,2)
chroma_subsampling(4,2,0)
chroma_subsampling(4,1,1)
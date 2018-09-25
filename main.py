import numpy as np
import cv2
from PIL import Image

imagem = 'beico.jpeg'



# print(len(Y),len( Cb),len( Cr))

# cb = Cb[::2,::2]
# cr = Cr[::2,::2]

# cb_2 = np.repeat(cb,2,axis=1)
# cb_3 = np.repeat(cb_2,2,axis=0)
# cb_4 = cb_3[:len(Y),:len(Y[0])]

# cr_2 = np.repeat(cr,2,axis=1)
# cr_3 = np.repeat(cr_2,2,axis=0)
# cr_4 = cr_3[:len(Y),:len(Y[0])]

# img_3 = cv2.merge([Y,cr_4,cb_4])

# img_4 = cv2.cvtColor(img_3, cv2.COLOR_YCrCb2BGR)


# cv2.imshow('imagem',img_4)

# cv2.waitKey(0)

def chroma_subsampling(j,a,b):
	original = cv2.imread(imagem)
	img_1 = cv2.cvtColor(original, cv2.COLOR_BGR2YCrCb)
	Y, Cr, Cb = cv2.split(img_1)
	
	x = int(j/a)
	y = None
	if(int(b) in [0,4]):
		y = 1
	else:
		y = 2

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
	img_1 = cv2.cvtColor(img_1, cv2.COLOR_YCrCb2BGR)
	print(np.array_equal(img_1,original))
	cv2.imwrite('{}:{}:{}_{}'.format(j,a,b,imagem),img)



def imga():
	x = Image.open('beico.jpeg')
	a = x.convert('YCbCr')
	b = a.convert('RGB')

	x = np.array(x) 
	b = np.array(b)

	print(np.array_equal(x,b))


imga()
# chroma_subsampling(4,4,4)
# chroma_subsampling(4,2,2)
# chroma_subsampling(4,2,0)
# chroma_subsampling(4,1,1)
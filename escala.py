import cv2
import numpy as np
from math import cos, radians, sin


def mul_dot(x,y,mtr):
	ponto = np.array([[x],[y],[1]])
	return np.matmul(mtr,ponto).astype(int)


def escala(imagem, shape):
	original = cv2.imread(imagem)
	height   = len(original)
	width    = len(original[0])

# Matrizes para rotacao
	escala = [[shape[0],		 0, 0],
	          [		  0,  shape[1], 0],
	          [		  0, 		 0, 1]]
	rot = escala
# Enquadrar a imagem toda
	p = mul_dot(width,height,rot)
	print(p)
	maxx = p[0,0]
	maxy = p[1,0]

# Imagem vazia
	new = np.zeros((maxy,maxx,3), np.uint8)

# Rotacao da imagem
	for i in range(len(original)):
		for j in range(len(original[0])):
			res = mul_dot(i,j,rot)
			new[res[0],res[1]] = original[i,j]

	# cv2.imshow('Imagem resultante', new)
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()
	cv2.imwrite('escala_{}x{}_{}'.format(shape[0],shape[1],imagem),new)

escala('beico.jpeg',(2,2))
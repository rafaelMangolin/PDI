import cv2
import numpy as np
from math import cos, radians, sin


def mul_dot(x,y,mtr):
	ponto = np.array([[x],[y],[1]])
	return np.matmul(mtr,ponto).astype(int)

def get_matriz_escala(x,y):
	return [[x, 0, 0],
     		[0, y, 0],
	 		[0, 0, 1]]

def escala(imagem, shape):
	original = cv2.imread(imagem)
	height   = len(original)
	width    = len(original[0])

	# Matrizes para rotacao
	escala = get_matriz_escala(shape[0], shape[1])
	# Enquadrar a imagem toda
	p = mul_dot(width,height,escala)
	maxx = p[0,0]
	maxy = p[1,0]

	# Imagem vazia
	new = np.zeros((maxx,maxy,3), np.uint8)

	# Escala da imagem
	for i in range(len(original)):
		for j in range(len(original[0])):
			res = mul_dot(i,j,escala)
			new[res[0],res[1]] = original[i,j]

	escala_inv = get_matriz_escala(1/shape[0],1/shape[1])
	
	# cv2.imshow('Imagem', new.copy())

	for i in range(len(new)):
		for j in range(len(new[0])):
			res = mul_dot(i,j,escala_inv)
			new[i,j] = original[res[0],res[1]]

	# cv2.imshow('Imagem resultante', new)
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()
	cv2.imwrite('escala_{}x{}_{}'.format(shape[0],shape[1],imagem),new)

escala('beico.jpeg',(2,.5))
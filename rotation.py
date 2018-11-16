import cv2
import numpy as np
from math import cos, radians, sin


def mul_dot(x,y,mtr):
	ponto = np.array([[x],[y],[1]])
	return np.matmul(mtr,ponto).astype(int)


def matriz_rotacao(angulo):
	return [[cos(angulo), -sin(angulo), 0],
	        [sin(angulo),  cos(angulo), 0],
	        [		   0, 			 0, 1]]

def matriz_translacao(x,y):
	return [[1, 0, x],
	        [0, 1, y],
	        [0, 0, 1]]

def rotacao(imagem, ang):
	original = cv2.imread(imagem)
	angulo   = radians(ang)
	height   = len(original)
	width    = len(original[0])
	dy = int(len(original)/2)
	dx = int(len(original[0])/2)

# Matrizes para rotacao
	mul = matriz_rotacao(angulo)

	ida = matriz_translacao(-dx, -dy)

	volta = matriz_translacao(dx, dy)

	rot = np.matmul(mul,ida)
	rot = np.matmul(volta,rot)

# Enquadrar a imagem toda
	p1 = mul_dot(0,0,rot)
	p2 = mul_dot(0,height,rot)
	p3 = mul_dot(width,0,rot)
	p4 = mul_dot(width,height,rot)

	xs = [p1[0],p2[0],p3[0],p4[0]]
	ys = [p1[1],p2[1],p3[1],p4[1]]

	maxx = max(xs)[0]
	minx = min(xs)[0]

	maxy = max(ys)[0]
	miny = min(ys)[0]

	nh = int(maxy-miny)
	nw = int(maxx-minx)

	iy = int((nh - height) * .5)
	ix = int((nw - width) * .5)

# Imagem vazia
	new = np.zeros((nh+1,nw+1,3), np.uint8)

# Rotacao da imagem
	for i in range(len(original)):
		for j in range(len(original[0])):
			res = mul_dot(i,j,rot)
			new[res[0]+ix,res[1]+iy] = original[i,j]


	height_old = height
	width_old = width
	height   = len(new)
	width    = len(new[0])
	dy = int(len(new)/2)
	dx = int(len(new[0])/2)

# Matrizes para rotacao
	mul = matriz_rotacao(radians(-ang))

	ida = matriz_translacao(-dx, -dy)

	volta = matriz_translacao(dx, dy)

	rot = np.matmul(mul,ida)
	rot = np.matmul(volta,rot)



	for i in range(len(new)):
		for j in range(len(new[0])):
			res = mul_dot(i,j,rot)
			x = res[0]-ix 
			y = res[1]-iy
			if(x >= 0 and x < width_old and y >= 0 and y < height_old):
				new[i,j] = original[x,y]


	cv2.imshow('Imagem resultante', new)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	# cv2.imwrite('angulo_{}_{}'.format(ang,imagem),new)

rotacao('beico.jpeg',45)
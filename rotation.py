import cv2
import numpy as np
from math import cos, radians, sin


def mul_dot(x,y,mtr):
	ponto = np.array([[x],[y],[1]])
	return np.matmul(mtr,ponto).astype(int)


def rotacao(imagem, ang):
	original = cv2.imread(imagem)
	angulo   = radians(ang)
	height   = len(original)
	width    = len(original[0])
	dy = int(len(original)/2)
	dx = int(len(original[0])/2)

# Matrizes para rotacao
	mul = [ [cos(angulo), -sin(angulo), 0],
	        [sin(angulo),  cos(angulo), 0],
	        [		   0, 			 0, 1]]
	mul = np.array(mul)
	ida = [ [1, 0, -dx],
	        [0, 1, -dy],
	        [0, 0,   1]]
	ida = np.array(ida)
	volta = [ [1, 0, dx],
	          [0, 1, dy],
	          [0, 0,  1]]
	volta = np.array(volta)
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

	iy = int((nh - height) * .5)-1
	ix = int((nw - width) * .5)-1

# Imagem vazia
	new = np.zeros((nh,nw,3), np.uint8)

# Rotacao da imagem
	for i in range(len(original)):
		for j in range(len(original[0])):
			res = mul_dot(i,j,rot)
			new[res[0]+ix,res[1]+iy] = original[i,j]


	cv2.imwrite('angulo_{}_{}'.format(ang,imagem),new)

rotacao('beico.jpeg',45)
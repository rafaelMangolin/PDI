import cv2
import numpy as np
from math import cos, radians, sin


def multiplicar_ponto_matriz(x,y,mtr):
	ponto = np.array([x,y,1])
	return np.matmul(mtr,ponto).astype(int)


def matriz_rotacao(angulo):
	return [[cos(angulo), -sin(angulo), 0],
	        [sin(angulo),  cos(angulo), 0],
	        [		   0, 			 0, 1]]

def matriz_translacao(x,y):
	return [[1, 0, x],
	        [0, 1, y],
	        [0, 0, 1]]

def parametros_rotacao(largura,altura,mtz_rot):
	p1 = multiplicar_ponto_matriz(0,0,mtz_rot)
	p2 = multiplicar_ponto_matriz(0,largura,mtz_rot)
	p3 = multiplicar_ponto_matriz(altura,0,mtz_rot)
	p4 = multiplicar_ponto_matriz(altura,largura,mtz_rot)

	xs = [p1[0],p2[0],p3[0],p4[0]]
	ys = [p1[1],p2[1],p3[1],p4[1]]

	maxx = max(xs)
	minx = min(xs)

	maxy = max(ys)
	miny = min(ys)

	alt_img_rot = int(maxy-miny)
	lar_img_rot = int(maxx-minx)

	sobra_y = int((alt_img_rot - altura) * .5)
	sobra_x = int((lar_img_rot - largura) * .5)
	return alt_img_rot, lar_img_rot, sobra_y, sobra_x

def rotacao(imagem_nome, ang):
	imagem   = cv2.imread(imagem_nome)
	angulo   = radians(ang)
	altura   = len(imagem)
	largura  = len(imagem[0])
	dy 	     = int(len(imagem)/2)
	dx 	     = int(len(imagem[0])/2)

	mul 	= matriz_rotacao(angulo)
	ida 	= matriz_translacao(-dx, -dy)
	volta   = matriz_translacao(dx, dy)
	mtz_rot = np.matmul(mul,ida)
	mtz_rot = np.matmul(volta,mtz_rot)

	alt_img_rot, lar_img_rot, sobra_y, sobra_x = parametros_rotacao(largura,altura,mtz_rot)
	imagem_nova = np.zeros((alt_img_rot+1,lar_img_rot+1,3), np.uint8)
	for i in range(len(imagem)):
		for j in range(len(imagem[0])):
			res = multiplicar_ponto_matriz(i,j,mtz_rot)
			imagem_nova[res[0]+sobra_y,res[1]+sobra_x] = imagem[i,j]

	alt_img_rot = len(imagem_nova)
	lar_img_rot = len(imagem_nova[0])
	dy 			= int(len(imagem_nova)/2)
	dx 			= int(len(imagem_nova[0])/2)

	mul 	= matriz_rotacao(radians(-ang))
	ida 	= matriz_translacao(-dx, -dy)
	volta 	= matriz_translacao(dx, dy)
	mtz_rot = np.matmul(mul,ida)
	mtz_rot = np.matmul(volta,mtz_rot)

	for i in range(len(imagem_nova)):
		for j in range(len(imagem_nova[0])):
			res = multiplicar_ponto_matriz(i,j,mtz_rot)
			x = res[0]-sobra_x 
			y = res[1]-sobra_y
			if(x >= 0 and x < altura and y >= 0 and y < largura):
				imagem_nova[i,j] = imagem[x,y]


	cv2.imwrite('angulo_{}_{}'.format(ang,imagem_nome),imagem_nova)

rotacao('lena.png',45)
rotacao('lena.png',-45)
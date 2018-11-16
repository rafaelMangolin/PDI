import cv2
import numpy as np
from math import cos, radians, sin


def multiplicar_ponto_matrix(x,y,mtr):
	ponto = np.array([x,y,1])
	return np.matmul(mtr,ponto).astype(int)

def matriz_escala(x,y):
	return [[x, 0, 0],
     		[0, y, 0],
	 		[0, 0, 1]]

def escala(nome_imagem, formato):
	imagem  = cv2.imread(nome_imagem)
	altura  = len(imagem)
	largura = len(imagem[0])
	mtz_esc = matriz_escala(formato[0], formato[1])

	ponto = multiplicar_ponto_matrix(largura,altura,mtz_esc)
	x_max = ponto[0]
	y_max = ponto[1]

	new = np.zeros((x_max,y_max,3), np.uint8)
	for i in range(len(imagem)):
		for j in range(len(imagem[0])):
			res = multiplicar_ponto_matrix(i,j,mtz_esc)
			new[res[0],res[1]] = imagem[i,j]

	mtz_esc_inv = matriz_escala(1/formato[0],1/formato[1])
	for i in range(len(new)):
		for j in range(len(new[0])):
			res = multiplicar_ponto_matrix(i,j,mtz_esc_inv)
			new[i,j] = imagem[res[0],res[1]]

	cv2.imwrite('escala_{}x{}_{}'.format(formato[0],formato[1],nome_imagem),new)

if __name__ == '__main__':
	escala('lena.png',(2,2))
# -*- coding: utf-8 -*-
import numpy as np
import cv2
import colorsys

h = 80
s = 0
v = 100

# rgb_clr = colorsys.hsv_to_rgb(h,s,v)
print(rgb_clr)

w_h = np.linspace(h, h, 128)
w_s = np.linspace(0, 100, 128)
w_v = np.linspace(100, 100, 128)

h_b = np.linspace(h, h, 128)
s_b = np.linspace(100, 100, 128)
v_b = np.linspace(100, 0, 128)

p_h = w_h+h_b
p_s = w_s+s_b
p_v = w_v+v_b

p_h1 = np.tile( p_h.reshape(256,1), 256 )
p_h2 = np.tile( p_s.reshape(256,1), 256 )
p_v3 = np.tile( p_v.reshape(256,1), 256 )


# # Função para gerar a peleta de cores com um início e fim de cor definida pelo usuário
# def gerar_paleta( b1, g1, r1):
    
#     # Função: np.linspace(A, B, X)
#     # Descrição: gera um vetor com X valores entre A e B.
#     b = np.linspace(b1, b2, 256)
#     g = np.linspace(g1, g2, 256)
#     r = np.linspace(r1, r2, 256)
        
#     # Função: a.reshape(alt, largura)
#     # Descrição: Da uma nova forma a uma lista. Neste caso, criamos uma altura de 256 e 1 de largura
#     # Função: np.tile(array, X)
#     # Descrição: Repete um array X vezes. Aqui, repetindo o mesmo valor no eixo da largura para ficar com 256 de largura    
#     p1 = np.tile( b.reshape(256,1), 256 )
#     p2 = np.tile( g.reshape(256,1), 256 )
#     p3 = np.tile( r.reshape(256,1), 256 )
       
#     # Função: np.uint8(num)
#     # Descrição: converter números para 8 bits
#     p1 = np.uint8(p1)
#     p2 = np.uint8(p2)
#     p3 = np.uint8(p3)
        
#     # Função: np.dstack( (v1, v2) )
#     # Descrição: Faz a concatenação dos dois vetores, por exemplo.
#     paleta = np.dstack( (np.dstack( (p1,p2) ), p3) )
            
#     return paleta
#     # Fim da função

# # Definindo uma cor inicial
# b1 = 79
# g1 = 79
# r1 = 47
# # Definindo uma cor final
# b2 = 134
# g2 = 230
# r2 = 240

# # Gerando uma paleta de cores da inicial até a final    
# paleta = gerar_paleta(b1, g1, r1, b2, g2, r2)

# # Abrir a imagem original em tons de cinza, por isso o parâmetro 0
# img = cv2.imread('./Imagens/original.jpg', 0)

# # Criar uma nova matriz com o mesmo tamanho que a imagem, porém com uma terceira dimensão para armazenar as cores BGR
# # Função: np.zeros ( (x,y,z) , dtype=np.int8/16/32/... )
# # img.shape[0] = altura, 1 = largura, 2 = profundidade, etc (conforme existir)
# img_colorida = np.zeros( (img.shape[0], img.shape[1], 3) )

# # Como a peleta possui as mesmas cores RGB no eixo da largura, podemos sempre pegar a posição 0
# # O for percorre a altura e a largura da nova matriz criada para representar a imagem colorida, e recebe a cor de acordo com a imagem original e o tom de cinza
# for i in range(img.shape[0]):
#     for j in range(img.shape[1]):
#         img_colorida[i][j] = paleta [ img[i][j] ][0]

# # Converte os números da matriz para 8 bits
# img_colorida = np.uint8(img_colorida)

# # Mostrar uma imagem
# cv2.imshow('Paleta de cores', paleta)
# cv2.imshow('Imagem Original', img)
# cv2.imshow('Imagem resultante', img_colorida)

# # Funções para o funcionamento correto do python no Windows.
# cv2.waitKey(0)
# cv2.destroyAllWindows()
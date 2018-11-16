# -*- coding: utf-8 -*-
import numpy as np
import cv2
import colorsys
import imageio

def print_img(img, count):
    cv2.imshow('paleta{}'.format(count), img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def apply_pallet(img, pallet): 
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    new = np.zeros((len(img_gray),len(img_gray[0]),3), np.uint8)
    for i in range(len(img_gray)):
        for j in range(len(img_gray[0])):
            new[i,j] = pallet[img_gray[i,j],0]
    return new

def create_pallet(hue):
    black_saturation    = np.linspace(255, 255, 128)
    black_intensity     = np.linspace(0, 255, 128)

    saturation_white    = np.linspace(255, 0, 128)
    intensity_white     = np.linspace(255, 255, 128)

    palet_hue           = np.linspace(hue, hue, 256)
    palet_saturation    = np.concatenate((black_saturation, saturation_white))
    palet_intensity     = np.concatenate((black_intensity, intensity_white))

    palet_hue           = np.tile(palet_hue.reshape((256,1)), 256)
    palet_saturation    = np.tile(palet_saturation.reshape((256,1)), 256)
    palet_intensity     = np.tile(palet_intensity.reshape((256,1)), 256)

    img = cv2.merge([palet_hue,palet_saturation,palet_intensity])
    img = np.uint8(img)

    return cv2.cvtColor(img, cv2.COLOR_HSV2BGR)

if __name__ == "__main__":
    # img = cv2.imread('beico2.jpg')
    img_name = 'mundo.gif'
    gif = imageio.mimread(img_name)
    new_gif = [] 
    colors = np.linspace(0, 180, len(gif))

    for i in range(len(colors)):
        color = colors[i]
        frame = gif[i]
        new_gif.append(apply_pallet(frame,create_pallet(color)))


    gif = imageio.mimwrite('colorization_{}'.format(img_name),new_gif,'gif')
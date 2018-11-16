# -*- coding: utf-8 -*-
import numpy as np
import cv2
import colorsys
import imageio

def apply_palette(img, palette): 
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    new = np.zeros((len(img_gray),len(img_gray[0]),3), np.uint8)
    for i in range(len(img_gray)):
        for j in range(len(img_gray[0])):
            new[i,j] = palette[img_gray[i,j],0]
    return new

def create_palette(hue):
    black_saturation      = np.linspace(255, 255, 128)
    black_intensity       = np.linspace(0, 255, 128)

    saturation_white      = np.linspace(255, 0, 128)
    intensity_white       = np.linspace(255, 255, 128)

    palette_hue           = np.linspace(hue, hue, 256)
    palette_saturation    = np.concatenate((black_saturation, saturation_white))
    palette_intensity     = np.concatenate((black_intensity, intensity_white))

    palette_hue           = np.tile(palette_hue.reshape((256,1)), 256)
    palette_saturation    = np.tile(palette_saturation.reshape((256,1)), 256)
    palette_intensity     = np.tile(palette_intensity.reshape((256,1)), 256)

    img = cv2.merge([palette_hue,palette_saturation,palette_intensity])
    img = np.uint8(img)

    return cv2.cvtColor(img, cv2.COLOR_HSV2BGR)

def colorization(gif_name, start_hue, end_hue):
    gif = imageio.mimread(gif_name)
    new_gif = [] 
    colors = np.linspace(start_hue, end_hue, len(gif))
    for i in range(len(colors)):
        color = colors[i]
        frame = gif[i]
        new_gif.append(apply_palette(frame,create_palette(color)))
    gif = imageio.mimwrite('colorization_{}'.format(img_name),new_gif,'gif')

if __name__ == "__main__":
    img_name = 'mundo.gif'
    colorization(img_name,0,180)
    
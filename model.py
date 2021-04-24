#!/usr/bin/python3
"""This module performs different operations using OpenCV
to images, and saves the image.

Usage:
    Copy this module in a root directory containing a directories
    with images with the .jpg extension, change the variable "dir_path" to match
    the directory to perform operations in, the images will be saved in that directory
    with the name on the variable "name_img" + "c".
"""
import numpy as np
import cv2
from tensorflow.python.platform import gfile
import os.path

if __name__ == "__main__":
    file_list = []
    dir_path = '/example/'
    name_img = 'new_image'
    file_glob = os.path.join(dir_path, '*.jpg')
    file_list.extend(gfile.Glob(file_glob))
    c = 1
    for image in file_list:
        img = cv2.imread(image)
        # Rotación 180 grados:
        rows, cols, depth = img.shape
        M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 180, 1)
        dst = cv2.warpAffine(img, M, (cols, rows))
        cv2.imwrite(dir_path + name_img + str(c) + '.jpg', dst)
        c = c + 1
        # Rotación 270 grados escalado 0.5:
        rows, cols, depth = img.shape
        M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 270, 0.5)
        dst = cv2.warpAffine(img, M, (cols, rows))
        cv2.imwrite(dir_path + name_img + str(c) + '.jpg', dst)
        c = c + 1
        # Distorsión gaussiana:
        blur = cv2.GaussianBlur(img, (9, 9), 0)
        cv2.imwrite(dir_path + name_img + str(c) + '.jpg', blur)
        c = c + 1
        # Distorsión gaussiana operacion rotación y escalado anterior:
        blur = cv2.GaussianBlur(dst, (9, 9), 0)
        cv2.imwrite(dir_path + name_img + str(c) + '.jpg', blur)
        c = c + 1
        # Ruido gaussiano distribución normal:
        noise = np.zeros(img.shape)
        m = (0, 0, 0)
        s = (99, 99, 99)
        cv2.randn(noise, m, s)
        cv2.imwrite(dir_path + name_img + str(c) + '.jpg', noise + img)
        c = c + 1
        # Ruido gaussiano distribución uniforme:
        noise = np.zeros(img.shape)
        m = (0, 0, 0)
        s = (99, 99, 99)
        cv2.randu(noise, m, s)
        cv2.imwrite(dir_path + name_img + str(c) + '.jpg', noise + img)
        c = c + 1
        # Filtro Laplaciano:
        laplacian = cv2.Laplacian(img, cv2.CV_64F)
        cv2.imwrite(dir_path + name_img + str(c) + '.jpg', laplacian + img)
        c = c + 1
        # Flip vertical:
        flip = cv2.flip(img, 1)
        cv2.imwrite(dir_path + name_img + str(c) + '.jpg', flip)
        c = c + 1
        # Flip horizontal:
        flip = cv2.flip(img, 0)
        cv2.imwrite(dir_path + name_img + str(c) + '.jpg', flip)
        c = c + 1
        # Flip ambos:
        flip = cv2.flip(img, -1)
        cv2.imwrite(dir_path + name_img + str(c) + '.jpg', flip)
        c = c + 1

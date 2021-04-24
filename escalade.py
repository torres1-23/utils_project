#!/usr/bin/python3
"""This module performs escalade operation using OpenCV
to images, and saves the image.

Usage:
    Copy this module in a root directory containing a directory
    named 1 with images with the .jpg extension, thee images will be saved in
    the same directory.
"""
import numpy as np
import cv2
from tensorflow.python.platform import gfile
import os.path

if __name__ == "__main__":
    file_list = []
    file_glob = os.path.join('1', '*.jpg')
    file_list.extend(gfile.Glob(file_glob))
    c = 2
    for image in file_list:
        img = cv2.imread(image)
        flip = cv2.flip(img, -1)
        cv2.imwrite('1/s' + str(c) + '.jpg', flip)
        c = c + 1

#!/usr/bin/env pathon3
# _*_ coding: utf-8 _*_
# Author: Gaiping Liu gaipingliu@outlook.com

import tesserocr
import os
import locale
locale.setlocale(locale.LC_ALL, "C")

print(os.path.exists(r"C:/Program Files/Python36/tessdata"))
tessdatapath = r"E:/SelfImprovement/Python/PythonLearning/GaipingLiu/ProjectTest/TesserOcr/"

print(tesserocr.file_to_text(r'image.png', path=tessdatapath))
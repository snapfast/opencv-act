import os
import numpy as np
import cv2 as cv
from django.core.files.storage import FileSystemStorage


def face_detection(filepath):
    face_cascade = cv.CascadeClassifier('xml/haarcascade_frontalface_default.xml')
    eye_cascade = cv.CascadeClassifier('xml/haarcascade_eye.xml')

    img = cv.imread(filepath)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        img = cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        #for (ex, ey, ew, eh) in eyes:
        #    cv.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 2)

    # save file to rotated directory
    folderpath, tail = os.path.split(filepath)
    new_file = "/facedetect-" + tail
    new_file_path = folderpath + new_file
    status = cv.imwrite(new_file_path, img)
    print(status, ": status of writing the file")
    return "media" + new_file
    # cv.imshow('img', img)
    # cv.waitKey(0)
    # cv.destroyAllWindows()


# this function marks outline of image
def black_art_opencv(filepath):
    img = cv.imread(filepath, 0)
    rows, cols = img.shape
    # cols-1 and rows-1 are the coordinate limits.
    edge_img = cv.Canny(img, 100, 200)
    cv.imshow("Detected Edges", edge_img)
    dst = cv.warpAffine(img, M, (cols, rows))
    # cv.imshow('img', dst)
    # cv.waitKey(0)
    # cv.destroyAllWindows()

    # save file to rotated directory
    folderpath, tail = os.path.split(filepath)
    new_file = "/rotate-" + tail
    new_file_path = folderpath + new_file
    status = cv.imwrite(new_file_path, dst)
    print(status, ": status of writing the file")
    return "media" + new_file


# this function rotates the image by 90 degrees
def rotate(filepath, filename):
    img = cv.imread(filepath, 0)
    rows, cols = img.shape
    # cols-1 and rows-1 are the coordinate limits.
    M = cv.getRotationMatrix2D(((cols - 1) / 2.0, (rows - 1) / 2.0), 90, 1)
    dst = cv.warpAffine(img, M, (cols, rows))
    # cv.imshow('img', dst)
    # cv.waitKey(0)
    # cv.destroyAllWindows()

    # save file to rotated directory
    folderpath, tail = os.path.split(filepath)
    new_file = "/rotate-" + tail
    new_file_path = folderpath + new_file
    status = cv.imwrite(new_file_path, dst)
    print(status, ": status of writing the file")
    return "media" + new_file

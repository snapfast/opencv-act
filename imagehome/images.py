import os
import cv2


def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def black_art_opencv(filepath):
    img = cv2.imread(filepath)
    edge_img = cv2.Canny(img, 100, 200)
    cv2.imshow("Detected Edges", edge_img)
    cv2.waitKey(0)

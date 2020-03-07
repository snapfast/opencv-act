import os
import cv2 as cv
from django.core.files.storage import FileSystemStorage


def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def black_art_opencv(filepath):
    img = cv.imread(filepath)
    edge_img = cv.Canny(img, 100, 200)
    cv.imshow("Detected Edges", edge_img)
    # cv2.waitKey(0)
    return 0


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

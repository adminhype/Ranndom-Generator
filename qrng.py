import cv2, hashlib

class QRNG:
    def __init__(self):
        self.cam = cv2.VideoCapture(1, cv2.CAP_DSHOW)
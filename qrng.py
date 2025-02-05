import cv2, hashlib

class QRNG:
    def __init__(self):
        self.cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    def hashgen(self):
        _, img = self.cam.read()
        return hashlib.md5(img).hexdigest()
    
    def range(self, n):
        random_hash = self.hashgen()
        return (int(random_hash, 16) % n)
    
    def close(self):
        self.cam.release()
        cv2.destroyAllWindows()
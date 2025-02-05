from qrng import QRNG

if __name__ == "__main__":
    qrng = QRNG()
    print(qrng.range(10))
    qrng.close()
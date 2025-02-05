from qrng import QRNG

if __name__ == "__main__":
    stats = {}
    qrng = QRNG()

    for _ in range(1000):
        rand = qrng.range(10)
        if rand in stats:
            stats[rand] += 1
        else:
            stats[rand] = 1
    
    print(dict(sorted(stats.items())))
    qrng.close()
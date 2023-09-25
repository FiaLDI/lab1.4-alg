
def maxi(a):
    d = 0
    for i in range(len(a)):
        if a[i] > d:
            d = a[i]
    return d

if __name__ == '__main__':
    import time
    d = 0
    for j in range(1000, 10000, 1000):
        for r in range(10000):
            a = [i for i in range(j)]
            start = time.perf_counter()
            p = maxi(a)
            end = time.perf_counter()
            d += end - start
        print(f"{(d/(10000-1)):.10f}")
import time


#ile = 0


def XdopotengiN(x,n):
    #global ile
    #ile += 1
    if x == 0:
        return 0
    if n == 0:
        return 1
    if n % 2:
        return x*XdopotengiN(x,n-1)
    else:
        return XdopotengiN(x,n/2)**2


def potegamnozenie(x,n):
    #global ile
    #ile += 1
    r = 1
    for i in range(n, 0, -1):
       r *= x
    return r


#! O = log2(n)+1
def XdopotengiN2(x,n):
    #global ile
    #ile += 1
    if n == 1: 
        return x
    if x == 0:
        return 0
    if n == 0:
        return 1
    polowaN = XdopotengiN2(x, n//2)
    if n % 2:
        return x*polowaN*polowaN
    return polowaN*polowaN


def measuretime():
    #global ile
    #ile += 1
    w,z,g = {}, {}, {}
    h = [100, 1000, 10000, 1000000]
    for i,j in zip(h, range(len(h))):
        start = time.time()
        a = XdopotengiN(2,i)
        koniec = time.time()
        u = 34
        w[j+1] = koniec - start
    for i,j in zip(h, range(len(h))):
        start = time.time()
        b = potegamnozenie(2,i)
        koniec = time.time()
        u = 34
        z[j+1] = koniec - start
    for i,j in zip(h, range(len(h))):
        start = time.time()
        c = XdopotengiN2(2,i)
        koniec = time.time()
        u = 34
        g[j+1] = koniec - start
    print(f"Fast:  {w}")
    print(f"Slow:  {z}")
    print(f"Fast2: {g}")
    

measuretime()

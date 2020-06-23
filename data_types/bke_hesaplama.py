"""
Kullanicidan aldiginiz boy ve kilo degerlerine gore kullanicinin bedeb kitle endeksini bulun.

Beden Kitle Endeksi: Kilo/Boy(m)*Boy(m)

"""
"""
Cozum 1:

k = int(input("Kilonuz kac?: "))
b = float(input("Boyunuz kac?: "))
print("Beden Kitle Endeksi: ", k/(b ** 2))

"""

"""
Cozum 2:
"""

k = int(input("Kilonuz kac?: "))
b = float(input("Boyunuz kac?: "))
e = k/(b ** 2)

print("Kilonuz: {}\nBoyunuz: {}\nBeden Kitle Endeksiniz: {}".format(k,b,e))

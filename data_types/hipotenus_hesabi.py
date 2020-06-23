"""
Pisagor Teoremi

Bir dik ucgende, dik açıya bağlı olan iki kenarın uzunluklarının kareleri toplamı hipotenüs uzunluğunun karesine eşittir.

Yani bir dik kenar a, diger dik kenar b olsun. a^2 + b^2 = h^2

Kullanicidan bir dik ucgenin dik olan iki kenarini (a,b) alin ve hipotenusu bulun.
"""
print("Pisagor Bagintisi - Dik Ucgende Hipotenus Bulma")
d1 = int(input("Birinci dik kenarin uzunlugunu yaziniz: "))
d2 = int(input("Ikinci dik kenarin uzunlugunu yaziniz: "))
h = (d1 ** 2 + d2 ** 2) ** 0.5

print("Birinci dik kenar: {}\nIkinci dik kenar: {}\nHipotenus: {}".format(d1, d2, h))



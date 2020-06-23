"""
Kullanicidan alinan boy ve kilo degerlerine gore beden kitle endeksini hesaplayin
ve asagidaki kosullara gore ekrana yazdirin:

Beden Kitle Endeksi: Kilo / Boy(m) * Boy(m)

BKE 18.5'un altindaysa ------> Zayif
BKE 18.5 ile 25 arasindaysa ------> Normal
BKE 25 ile 30 arasindaysa ------> Fazla Kilolu
BKE 30'un uzerindeyse ------> Obez

"""

k = float(input("Kilonuzu giriniz: "))
b = float(input("Boyunuzu metre cinsinden giriniz: "))
bke = k / (b * b)

if (bke <= 18.5):
    print("Beden kitle endeksiniz 18.5 altinda oldugu icin zayifsiniz.")
elif (bke > 18.5 and bke < 25):
    print("Beden kitle endeksiniz 18.5 ile 25 araliginda oldugu icin normal kilodasiniz.")
elif (bke >= 25 and bke < 30):
    print("Beden kitle endeksiniz 25 ile 30 araliginda oldugu icin fazla kilodasiniz.")
elif (bke >= 30):
    print("Beden kitle endeksiniz 30'un uzerinde oldugu icin malesef obezsiniz.")
else:
    print("Gecersiz bir bilgi girdiniz.")



"""
Kullanicinin girdigi vize1, vize2, final notlarina gore harf notunu hesaplayin.

Vize1 toplam notun %30'una etki edecek.

    Vize2 toplam notun %30'una etki edecek.

    Final toplam notun %40'ına etki edecek.

    Toplam Not >=  90 -----> AA
    Toplam Not >=  85 -----> BA
    Toplam Not >=  80 -----> BB
    Toplam Not >=  75 -----> CB
    Toplam Not >=  70 -----> CC
    Toplam Not >=  65 -----> DC
    Toplam Not >=  60 -----> DD
    Toplam Not >=  55 -----> FD
    Toplam Not <  55 -----> FF
"""

vize1 = float(input("Birinci vize notunuzu giriniz: "))
vize2 = float(input("Ikinci vize notunuzu giriniz: "))
final = float(input("Final notunuzu giriniz: "))

hesap = ((vize1 + vize2) * 30 / 100) + final * 40 / 100
print("Aldiginiz Puan: {}".format(hesap))

if (hesap >= 90):
    print("Notunuz: AA")
elif (hesap >= 85):
    print("Notunuz: BA")
elif (hesap >= 80):
    print("Notunuz: BB")
elif (hesap >= 75):
    print("Notunuz: CB")
elif (hesap >= 70):
    print("Notunuz: CC")
elif (hesap >= 65):
    print("Notunuz: DC")
elif (hesap >= 60):
    print("Notunuz: DD")
elif (hesap >= 55):
    print("Notunuz: FD")
elif (hesap >= 50):
    print("Notunuz FF")
else:
    print("Basarisiz...")
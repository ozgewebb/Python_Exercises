print("""*************************
Hesap Makinesi Programi

Islemler:

1. Toplama Islemi
2. Cikarma Islemi
3. Carpma Islemi
4. Bolme Islemi

***************************
""")

a = int(input("Birinci Sayi: "))
b = int(input("Ikinci Sayi: "))

islem = input("Yapmak istediginiz islemin numarasini giriniz: ")

if islem == "1":
    print("{} ile {} sayilarinin toplama sonucu: {}".format(a,b,a+b))
elif islem == "2":
    print("{} ile {} sayilarinin cikarma sonucu: {}".format(a,b,a-b))
elif islem == "3":
    print("{} ile {} sayilarinin carpma sonucu: {}".format(a,b,a * b))
elif islem == "4":
    print("{} ile {} sayilarinin bolme sonucu: {}".format(a,b,a / b))
else:
    print("Gecersiz islem!")



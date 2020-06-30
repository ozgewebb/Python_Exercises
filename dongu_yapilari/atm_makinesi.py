print("""
*******************************
ABC BANKASINA HOSGELDINIZ...

Islemler:

Bakiye Sorgulama: 1
Para Yatirma: 2
Para Cekme: 3

Sanal bankadan cikmak icin 'q'ya basiniz.

*******************************
""")

bakiye = 1000

while True:
    islem = input("Yapmak istediginiz islemin numarasini giriniz: ")

    if (islem == "q"):
        print("Sistemden cikiyorsunuz. Tekrar bekleriz...")
        break

    elif (islem == "1"):
        print("Bakiyeniz {} TL'dir. ".format(bakiye))

    elif (islem == "2"):
        miktar = int(input("Yatirmak istediginiz miktari giriniz: "))
        bakiye += miktar
        print("Para yatirma isleminiz basariyla gerceklesmistir. Bakiyeniz {} TL'dir. ".format(bakiye))

    elif (islem == "3"):
        miktar = int(input("Cekmek istediginiz miktari giriniz: "))
        if (bakiye - miktar < 0):
            print("Cekmek istediginiz miktari hesabiniz karsilamamaktadir.")
            continue
        bakiye -= miktar
        print("Para cekme isleminiz basariyla gerceklesmistir. Bakiyeniz {} TL'dir. ".format(bakiye))

    else:
        print("Gecersiz islem!")
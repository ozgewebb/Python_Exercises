"""
Ilk olarak kullanicidan, ucgenin mi dortgenin mi tipini bulmak istedigi sorun.
Kullanici "dortgen" cevabini verirse, dort tane kenar olcusu isteyip bu dortgenin, kare mi,
dikdortgen mi yoksa siradan bir dortgen mi oldugunu bulun.
Kullanici "ucgen" cevabini verirse, uc tane kenar olcusu isteyip, bu ucgenin ikizkenar mi, eskenar mi,
yoksa siradan bir ucgen mi oldugunu bulun.
Eger verilen kenarlar bir ucgen belirtmiyorsa, "Ucgen belirtmiyor." mesaji yazdirin ekrana.

NOT: Bu problemde mutlak deger bulma ihtiyaciniz olacak. Bunun icin Python'da hazir bir fonksiyon olan
abs() fonksiyonunu kullanabilirsiniz.
"""

sekil = input("Ucgen tipini bulmak icin ucgen, dortgen tipini bulmak icin dortgen yaziniz ve kucuk harfler kullaniniz:")

if (sekil == "ucgen"):
    print("Lutfen sirayla uc kenar uzunlugu giriniz: ")
    a = int(input("1.Kenar: "))
    b = int(input("2.Kenar: "))
    c = int(input("3.Kenar: "))
    if (abs(a + b) > c and abs(a + c) > b and abs(b + c) > a):
        if (a == b and a == c):
            print("Eskenar Ucgen...")
        elif ((a == b and a != c) or (a == c and a != b) or (b == c and b != a)):
            print("Ikizkenar Ucgen...")
        else:
            print("Cesitkenar Ucgen...")
    else:
        print("Ucgen belirtmiyor...")

elif (sekil == "dortgen"):
    print("Lutfen sirayla dort kenar uzunlugu giriniz: ")
    a = int(input("1.Kenar: "))
    b = int(input("2.Kenar: "))
    c = int(input("3.Kenar: "))
    d = int(input("4.Kenar: "))
    if (a == b and a == c and a == d):
        print("Kare...")
    elif (a == c and b == d):
        print("Dikdortgen...")
    else:
        print("Dortgen...")

else:
    print("Gecersiz sekil...")
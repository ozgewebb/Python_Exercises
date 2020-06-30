print("""
*******************
Faktoriyel Bulma Programı

Programdan çıkmak için 'q' ya basın.
*******************
""")

while True:
    sayi = input("Sayi giriniz: ")
    if (sayi == "q"):
        print("Program sonlandiriliyor...")
        break

    else:
        sayi = int(sayi)
        faktoriyel = 1
        for i in range(2,sayi+1):
            faktoriyel *= i
            print(faktoriyel)
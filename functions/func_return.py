"""def toplama(a,b,c):
    print("Toplamlari: ",a+b+c)
fonksiyonu print yapmakla bu fonksiyonu kullanmis olmuyoruz.
Fonksiyonu dis dunyaya gonderebilmemiz, bir deger dondurebilmemiz,
fonksiyonu gerekli yerlerde kullanabilmemiz icin return ifadesine
ihtiyac vardir.
"""
"""
def toplama(a,b,c):
    return a+b+c
def ikiylecarp(a):
    return a*2

toplam = toplama(3,4,5) #toplam degiskeni 12 cikiyor.
print(ikiylecarp(toplam)) #12 degerini alan toplam degiskenine bu defa ikiylecarp fonksiyonu uygulaniyor.

"""

def uclecarp(a):
    print("uclecarp fonksiyonu calisti.")
    return a*3

def ikiyletopla(a):
    print("ikiyletopla fonksiyonu claisti.")
    return a+2

def dordebol(a):
    print("dordebol fonksiyonu calisti.")
    return a/4

print("Uc fonksiyonun sirayla calismasi sonucu elde edilen deger: ", dordebol(ikiyletopla(uclecarp(5))))
#ilk olarak parantez icinde en icte - sorulan degere en yakin olan fonksiyon calisiyor, sonra sirayla disa dogru calisiyor...

#return, fonksiyonu sonlandiran bir islem, fonksiyonda returnden sonra bir islem ornegin print yazmissaniz calismaz.

#return kullanilmayan fonksiyonlara void deniliyor.

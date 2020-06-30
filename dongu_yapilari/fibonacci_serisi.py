"""
Fibonacci Serisi, yeni bir sayiyi onceki iki sayinin toplami seklinde olusturur.
Boylece, sonsuza kadar giden bir Fibonacci Serisi olusmus olur.

1,1,2,3,5,8,13,21,34,...............

"""

a = 1
b = 1

fibonacci = [a,b]

for i in range(20):
    #a,b = b,a diye bir gosterim ogrenmistik baslarda, burada ona yakin bir islem yapacagiz.
    a,b = b,a+b #Burada, a'ya b'nin eski degerini, b'ye de a+b degerini atamis oluyoruz.

    fibonacci.append(b)

print(fibonacci)
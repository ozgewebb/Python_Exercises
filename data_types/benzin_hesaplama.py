"""
Bir aracin kilometre basina ne kadar yaktigi ve kac km yol yaptigi bilgilerini alin ve surucunun toplam ne kadar benzin masrafi oldugunu yazdirin.
"""
litre = int(input("Araciniz km basina ne kadar benzin yakar?: "))
km = int(input("Kac km yol gittiniz?: "))
toplam_masraf = litre * km

print("Km Basina Benzin Yakma Miktari: {}\nToplamda Gidilen Yol: {}\nToplam Masraf: {}".format(litre, km, toplam_masraf))



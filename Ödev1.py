# Veri tipler nelerdir? 
# int. => tam sayi olan numirik ifadeler icin kullanilan degisken tipidir
# str. => harf ifadeler icin kullanilan degisken tipidir
# float. => ondalikli veya tamsayi olmayan numirik ifadeler icin kullanilan degisken tipidir
# bool. => iki degisken arasinda dogru veya yanlis seklinde ifade etmek icin kullanilan degisken tipidir 

# sik sorulan sorular kisiminda degisken turleri icin bir kac ornek verilebilir bunlardan bazilari:
# bu kisimda metin olarak yazilan soru ve cevaplar her biri birer str. olarak algilayabiliriz onun
# disinda yayin saati olarak yazilan 21.00 hem int. olarak hemde flo. olarak algilayabiliriz

# sart bloklarin bir ornegi "kurslarim " kisminda verilebilir:
tamamlandi = 0
ders_programi = 25
degerlendirme = 50
odev_1 = 75
odev_2 = 100
if tamamlandi < ders_programi:
    print(f"%{ders_programi} TAMAMLANDI")
elif tamamlandi < degerlendirme:
    print(f"%{degerlendirme} TAMAMLANDI")
elif tamamlandi < odev_1:
    print(f"%{odev_1} TAMAMLANDI")
else:
    print(f"%{odev_2} TAMAMLANDI")
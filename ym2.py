from math import sqrt
import math
import os


# Bir yere yakin yorunge (LEO) uydusu Dunya etrafinda dairesel yorungededir.
# Uydunun yorunge duzleminde bulunan bir yer istasyonu ile uydu haberlesmektedir.
# Burada uydu ve yer istasyonu arasindaki en uzun haberlesme suresi (ufuktan ufuga) = 920 saniyedir.
# Uydunun irtifasinin bulunmasi :


#Derececeleri belirlemek icin ornekler (Kodu anlamak icin gerekli)
def ornekler() :
    print(math.degrees(0))                       #0 radians == 0 degrees
    print(math.degrees(math.pi/2)      )         #pi/2 radians is 90 degrees
    print(math.degrees(math.pi))                 #pi radians is 180 degrees
    print(math.degrees(math.pi+(math.pi/2)))     #pi+pi/2 radians is 270 degrees
    print(math.degrees(math.pi+math.pi))         #2*pi radians is 360 degrees
    print(math.acos(0.5)*math.degrees(math.pi/3.14159))     #arc cos ile derece arasindaki iliski ornegi

ornekler()


#Manuel iterasyon islemleri
while True:
    os.system("cls")
    print("[1]Islemler\n[q]Cikis")
    secim=input("Islemini Sec: ")

    if secim == "1":
        #Islemler
        h = float(input("İterayon icin yukseklik gir ="))
        t = 2 * (math.acos( (6.37814 * 10**(6)) / (6.37814 * 10**(6) + h ))) \
            * sqrt( ( 6.37814 * 10**(6) + h )**(3) / ( 3.9859734 * 10**(14) ) )
        print("En uzun haberleşme süresi = {} [saniye] Ve Uydunun Irtifasi = {} [metre]".format(t, h))

    elif secim == "q":
        print("Cikiliyor")
        quit()

    else :
        print("Hatali secim")
        print("Islem tamamlandi. Ana menuye donmek icin entera bas")
        input()

# -*- coding: utf-8 -*-
"""
@author: IdrisIbrahimERTEN
"""

sayidan_alfabe={0:"a", 1:"b", 2:"c", 3:"ç", 4:"d", 5:"e", 6:"f", 7:"g", 8:"ğ", 9:"h", 10:"ı",
11:"i", 12:"j", 13:"k", 14:"l", 15:"m", 16:"n", 17:"o", 18:"ö", 19:"p", 20:"r",
21:"s", 22:"ş", 23:"t", 24:"u", 25:"ü", 26:"v", 27:"y", 28:"z"}

alfabeden_sayi={"a":0, "b":1, "c":2, "ç":3, "d":4, "e":5, "f":6, "g":7, "ğ":8, "h":9, "ı":10, "i":11,
"j":12, "k":13, "l":14, "m":15, "n":16, "o":17, "ö":18, "p":19, "r":20,
"s":21, "ş":22, "t":23, "u":24, "ü":25, "v":26, "y":27, "z":28 }

"""
for key, value in alfabe.items():
	print(key, value)
"""

def sifrele(metin,anahtar):
    sonuc = ""
    for i in metin:
        if i in alfabeden_sayi:
          sayi = alfabeden_sayi[i]
          sayi=(sayi+anahtar)%29
          sonuc=sonuc+sayidan_alfabe[sayi]
        elif i==" ":
            sonuc=sonuc+i
        else:
            sonuc += i
    return sonuc
      
      

def sifrecoz(metin):
    for i in range(1,29):
        a=sifrele(metin,i)
        print(a)


def main():

    bayrak=True
    while bayrak:
        a = (input(":Sezar şifresi programı - lütfen seçiniz:\n"
                                                    "1. Şifreleme \n2. Şifre çözme\n"))
        try:
            if (int(a) == 1):
                bayrak=False
                
                metin = (input("lütfen şifrelenecek metni giriniz:\n"))
                metin=metin.lower()
                anahtar = int(input("lütfen şifreleyecek anahtarı giriniz:\n"))
                sonuc=sifrele(metin,anahtar)
                print(sonuc)
                   
                        
            elif (int(a) == 2):
                bayrak=False
                metin = (input("lütfen şifresi çözülecek metni giriniz:\n"))
                sonuc=sifrecoz(metin) 
        except :
            bayrak=True
            print("yanlış giriş") 
            
if __name__ == '__main__' : 
	main()
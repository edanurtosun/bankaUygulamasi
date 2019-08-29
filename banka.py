import random
baslangic = 1000
musteriler = list()

def kayitYap(isimSoyisim, kimlikNumarasi, parola, mail, iban):
    hesap = {
        'isim':isimSoyisim,
        'tc':kimlikNumarasi,
        'parola':parola,
        'email':mail,
        'iban':iban

    }
    musteriler.append(hesap)
    print(musteriler)
    print(musteriler[0]['isim'])
    return hesap



girisYapildiMi = False
yapilanIslem = None
kontrol = True

while kontrol:
    print("""
    Python Bank'a Hoşgeldiniz
    Yapmak istediginiz islemi secin : 
    1.Giris
    2.Kayit
    3.Cikis icin q'ya basiniz
    """)
    yapilanIslem = (input("Seciminiz : "))

    if yapilanIslem == "1": #giris

        kullaniciKimligi = input("Kullanici kimligini giriniz : ")
        kullaniciParola = input("Parolanizi giriniz : ")

        for i in range(0,len(musteriler)):
                if musteriler[i]['tc'] == kullaniciKimligi and musteriler[i]['parola'] == kullaniciParola:
                    while True:
                        print("Sisteme giris yapildi")
                        print("""
                        1.Para Yatirma
                        2.Para Cekme
                        3.Bakiye Sorgu
                        4.Transfer
                        """)

                        giristeSecilenIslem = int(input("Yapmak istediginiz islem : "))

                        if giristeSecilenIslem == 1:
                            print("Hesabinizdaki para {}'dir".format(baslangic))
                            yatirilacakMiktar = int(input("Kac tl yatirmak istiyorsunuz ? : "))
                            baslangic = baslangic + yatirilacakMiktar
                            print("Hesabinizdaki son miktar {} tl'dir".format(baslangic))
                            break
                        elif giristeSecilenIslem == 2:
                            print("Hesabinizdaki para {}'dir".format(baslangic))
                            cekilecekMiktar = int(input("Kac tl cekmek istiyorsunuz ? : "))
                            if cekilecekMiktar > baslangic:
                                print("Hesabinizda yeterli miktarda bakiye bulunmamaktadir")
                                break
                            else:
                                baslangic = baslangic - cekilecekMiktar
                                print("Hesabinizdaki son miktar {} tl'dir".format(baslangic))
                                break
                        elif giristeSecilenIslem == 3:
                            print("Hesabinizdaki para {}'dir".format(baslangic))
                            break
                        elif giristeSecilenIslem == 4:
                            ibanNumarasi = int(input("Ibaninizi giriniz : "));
                            if i['iban'] == ibanNumarasi:
                                transferMiktari = int(input("Transfer edeceginiz miktari giriniz : "))
                                baslangic = baslangic - transferMiktari
                                print("Hesabinizdaki para : {}".format(baslangic))
                                break
                            else:
                                print("Iban numaraniz hatali!")
                                break
                        else:
                            print("Yanlis secim yaptiniz ")
                            break
                else:
                    print("Kaydiniz bulunamadi")
                    break

    elif yapilanIslem == "2": #kayit
        kayitIsimSoyisim = input("Isim ve soyisminizi giriniz : ")
        tckn = input("TCKN'yi giriniz : ")
        if len(tckn) <= 6:
            kayitTckn = tckn
        else:
            print("TCKN 6 haneden fazla olamaz!")
            tckn = input("TCKN'yi giriniz : ")
            kayitTckn = tckn

        kayitParola = input("Parolanizi giriniz : ")
        kayitMail = input("Mail adresinizi giriniz : ")
        kayitIban = random.randint(10000,99999)
        print("Size atanan iban numaraniz : {}".format(kayitIban))
        yeniKayit = kayitYap(kayitIsimSoyisim, kayitTckn, kayitParola, kayitMail, kayitIban)
        print("Merhaba {},Kaydiniz tamamlanmistir.".format(yeniKayit['isim']))
        girisYapildiMi = True

    elif yapilanIslem == "q":
        print("Programdan cikis yapiliyor")
        break

    else:
        print("Yanlis secim yaptiniz.")
        break









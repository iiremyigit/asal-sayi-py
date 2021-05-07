#ASAL QUİZ1-2

sayi = '1'
asal_mi = False
giris_hakki = 5

def asal_bul(sayi):
    if (sayi == 1):
        return False
    elif (sayi == 2):
        return True
    else:
        for i in range(2, sayi+1):
            if (sayi % i ==0):
                return False
            else:
                return True

while True:
    sayi = input("Lutfen sayi giriniz: ")
    sayi = int(sayi)
    asal_mi = asal_bul(sayi)

    if (asal_mi == True):
        print("Sayi asaldir!")
        giris_hakki -= 1
    else:
        print("Sayi asal degildir!")
        giris_hakki -= 1

    if giris_hakki == 0:
        print("Giris hakkiniz bitti!")

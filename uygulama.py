import random
#enes ömer kara uygulaması

def myfunc():
    x=int(input("Enter a number: "))
    print("The number you entered is:", x)
    print(("hello world ")*x)

myfunc()

#sadık turan uygulaması

def myfunc2(text,adet):
    return text * adet
print(myfunc2("hello world ", 3))


#enes ömer kara uygulaması

def hesapla(kısa,uzun):
    alan=kısa*uzun
    cevre=2*(kısa+uzun)
    return alan,cevre

alan,cevre=hesapla(5,10)
print("Alan:", alan)
print("Çevre:", cevre)

#sadık turan uygulaması

def hesapla(kısa,uzun):
    alan=kısa*uzun
    cevre=2*(kısa+uzun)
    return f"alan: {alan}, çevre: {cevre}"

sonuc=hesapla(3,5)
print(sonuc)

def yazi_tura():
    sayi = random.randint(0, 1)
    if sayi == 0:
        return "Yazi"
    else:
        return "Tura"

yazi_tura_sonuc = yazi_tura()
print("Yazı mı Tura mı?", yazi_tura_sonuc)

def asal_sayi(sayi1,sayi2):
    for i in range(sayi1, sayi2 + 1):
        if i > 1:
            for j in range(2, int(i ** 0.5) + 1):
                if (i % j) == 0:
                    break
            else:
                print(i)

asal_sayi(10, 50)

def full_name(first_name, last_name):
    return first_name + " " + last_name

print(full_name("Enes Ömer", "Kara"))



def user(*args):
    for i in args:
        print(i)

user("Enes", "Ömer", "Kara")

file={
    "name": "Enes Ömer Kara",
    "age": 25,
    "city": "Kocaeli",
    "bakiye": 0,

}
def menu():
    print("1. Bakiye Görüntüle")
    print("2. Para Yatır")
    print("3. Para Çek")
    print("4. Çıkış")

menu()

if __name__ == "__main__":
    while True:
        menu()
        choice = input("Seçiminizi yapın (1-4): ")
        if choice == "1":
            print("Bakiye:", file["bakiye"])
        elif choice == "2":
            amount = int(input("Yatırmak istediğiniz miktarı girin: "))
            file["bakiye"] += amount
            print("Yeni Bakiye:", file["bakiye"])
        elif choice == "3":
            amount = int(input("Çekmek istediğiniz miktarı girin: "))
            if amount <= file["bakiye"]:
                file["bakiye"] -= amount
                print("Yeni Bakiye:", file["bakiye"])
            else:
                print("Yetersiz bakiye!")
        elif choice == "4":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim! Lütfen tekrar deneyin.")

dosya=open("bilgiler.txt", "w",encoding="utf-8")
dosya.write("Ad: Enes Ömer Kara\n")
dosya.write("Yaş: 25\n")
dosya.write("Şehir: Kocaeli\n")
dosya.write("Bakiye: 0\n")
dosya.close()

dosya=open("bilgiler.txt", "r",encoding="utf-8")
print(dosya.read())
dosya.close()
with open("bilgiler.txt", "a",encoding="utf-8") as dosya:
    dosya.write("Yeni Bakiye: 100\n")
    dosya.tell()

    dosya=open("bilgiler.txt", "a",encoding="utf-8")
    print(dosya.write("Yeni Bakiye: 200\n"))

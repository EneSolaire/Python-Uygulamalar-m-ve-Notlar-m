x = int(input("sayı: "))
y = int(input("ikinci sayı: "))

print("çarpım: ", x * y)
print("toplam: ", x + y)
print("çıkarma: ", x - y)
print("bölme ", x / y)

print("bölümden kalan: ", x % y)

a = int(input("""Birini seç:
1- Toplama
2- Çıkarma
3- Çarpma
4- Bölme
5- Mod
0- Çıkış """))

if a == 1:
    print("toplam: ", x + y)

if a == 2:
    print("çıkarma: ", x - y)

if a == 3:
    print("çarpım: ", x * y)

if a == 4:
    print("bölme ", x / y)

if a == 5:
    print("bölümden kalan: ", x % y)

if a == 0:
    print("Çıktın")

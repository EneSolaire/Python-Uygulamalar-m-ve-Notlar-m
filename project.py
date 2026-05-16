#input

r = int(input("yarıçap girin:"))
print( "Alan", int((r**2)), "pi" )

#variables

pi= 3.14
print(str(pi))

#arrays

my_string= "10987654321"
print(my_string[3:6])
print(my_string[1::5])

# string işlemleri
string_2= "Enes Ömer Kara "
print(string_2.lower())
print(string_2.upper())
print(string_2.split())

#string çoğaltma

print(string_2*3)

#listeler

first_list= ["enes","ömer", "19" ,"18"]
first_list[1] = "Ege"
first_list.append("ali")
print(first_list)

#summation and multiplication at lists

list1= ["Enes Ömer"]
list2= ["Terzioğlu "]
print(list1+list2)
print(list2*3)
print(list1[0][1])

#dictionaries

dict={"Enes":19, 34:"Erdem"}
print(dict.values())
print(dict.keys())

#sets

list_3= set(["İstanbul","İzmir", "Ankara","Ankara", "Ankara", "İzmir"])
list_4= list_3.add("Kastamonu")
print(list_3)

#boolean

is_dead= True
print(type(is_dead))
print(3<2)

#atıl samancıoğlı python exam-1

my_string = "James Hetfield"
# 1) Aşağıdaki String'in 5. harfini my_letter isimli bir değişkene atayınız.

#Cevap: 
my_letter="s"

# Aşağıdaki String'in 5. ve 8. karakteri arasındaki tüm harflerini yazdırınız (5 ve 8 dahil)
my_new_string = "QuentinTarantino"

#Cevap2
print(my_new_string[4:8])

# 1) Aşağıdaki işlemin sonucu hangi veri tipinde olacaktır?
a=3 + 10.2 + 50
print(type(a))

# 2) Aşağıdaki işlemin sonucu kaçtır?
x= 5 + 8 * 12 
print(x)

#if-elif-else-1

araba_markasi="Volvo"

if araba_markasi != "Volvo":
    print("Araba Volvo değildir.")
elif araba_markasi=="Volvo":
    print("Araba Volvo'dur.")
    
#if-elif-else-2

isim="Aydın Ege"
if isim!= "Mert Ali":
    print("İsim Mert Ali değildir.")
else:
    print("İsim Mert Ali'dir.")
    
# for döngüsü
liste_1=["19"]
liste_2=["18"]

for yas1 in liste_1:
    print("Enes", yas1)
for yas2 in liste_2:
    print("Aydın", yas2)
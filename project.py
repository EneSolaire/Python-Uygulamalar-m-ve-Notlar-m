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

# for loops-2

sayilar=[1,3,5,7,9,12,19,21]

#first implementation

for numbers in sayilar:
    if numbers%3==0:
        print(numbers)
        
# second implementation

for numbers in sayilar:
    if numbers%2==1:
        print(numbers**2)

#third for loop implementation

string_3= "enes"

# last example


for letters in string_3:
    print(letters.upper())
list_4=[(1,2),(6,7)]

for (x,y) in list_4:
    print(y)
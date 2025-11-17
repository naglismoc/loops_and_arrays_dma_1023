import random

txt = "Jonas"
result = txt.replace("o","a")
print(result)
print(txt)

#          0  1  2   3   4   5  6  7  8  9  10 # indexai
numbers = [1, 5, 10, 14, 20, 3, 8, 7, 5, 8, 12] #masyvas (list)
print(numbers)
print(numbers[0])
print(numbers[1])
print(len(numbers))

numbers.append(60)
print(numbers)

numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers.remove(14) # pasalins 3cia elementa, nes jo reiksme 14. salins tik viena.

numbers.insert(2,15)
print(numbers)

#             0              1            2          3
vardai = ['Žygimantas', "Gabrielius", "Jokūbas", "Vilius"]

print(vardai)
print(vardai[1])

arr = [
    "hi",
    1,
    True
]
print(arr)

arr2d = [
    [20,14,3], # 0
    [17,18,9], # 1
    [20,25,22, "Žygimantas"] # 2
]

print(arr2d)
print(arr2d[2])
print(arr2d[2][2])
print(arr2d[0][1])

#             0  1  2  3  4  5  6  7  8  9 indexai
my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
####################### PIRMAS PARAMETRAS INCLUSSIVE, JĮ IMA, ANTRAS EXCLUSIVE, JO NEIMA, IMA IKI JO #################
####################### Multidimensiniose masyvuose galioja tos pacios taiykles ######################################
# my_numbers[pradzia:galas:zingsnis]
print(my_numbers) #atspausdins viską
print(my_numbers[6]) #atspausdins viena elementa
print(my_numbers[0:4]) #nuo iki
print(my_numbers[4:8])
print(my_numbers[7:]) # nuo, iki galo
print(my_numbers[:4]) #nuo pradzios iki nurodytos pozicijos
print(my_numbers[-2]) #antra pozicija nuo galo
print(my_numbers[-5:]) #nuo 5tos pozicijos nuo galo iki galo
print(my_numbers[:-5]) # nuo pradzios iki penktos nuo galo
print(my_numbers[2:-5]) #nuo 2os pozicijos iki 5tos nuo galo
print(my_numbers[-6:-2]) #nuo 6tos nuo galo iki 2os nuo galo
print(my_numbers[-8:4]) #teoriskai veikia, bet neapsikraukit :D
print(my_numbers[:]) #nuo pradzios iki galo
new_arr = my_numbers[:] # padaro kopija
print(my_numbers[0:10:2]) #nuo pradzios iki galo, kas antras elementas
print(my_numbers[::2]) #nuo pradzios iki galo, kas antras elementas
print(my_numbers[::3]) #kas trecias elementas
print(my_numbers[1::2]) #nuo pirmo elemento iki galo kas antras
print(my_numbers[3:7:2]) #nuo 3cio iki 7to kas antras
print(my_numbers[2:-2:2])#nuo 2o iki 2o nuo galo, kas antras
print(my_numbers[-2:2:2]) #nuo antro nuo galo iki antro nuo pradzios kas antras (nereiks tokiu, teoriskai imanoma)
print(my_numbers[::-1]) # visi elementai nuo galo, reverse
print(my_numbers[::-2]) #visi elementai nuo galo kas antras
print(my_numbers[5::-2]) #nuo 5 iki galo(tiksliau pradzios, nes einam atbulai ;) )
print(my_numbers[8:2:-2]) # nuo 8tos iki 2os, kas antras. 2a pozicija exclusive
print(my_numbers[-2:2:-2]) # nuo antros nuo galo iki antros pozicijos, kas antras atbulai

#             0              1            2          3        4
vardai = ['Žygimantas', "Gabrielius", "Jokūbas", "Vilius", "Jonas"]

for vyriskis in vardai: # vyriskis yra vardai[x] kopija, originalas nesikeicia redaguojant vyriski
    vyriskis = vyriskis.upper()
    print(vyriskis)
print(vardai)

for i in range(0, 4):
    print(i)

for i in range(4):
    print( f'i = {i}, vardai[{i}] = {vardai[i]}')

for i in range(len(vardai)):
    vardai[i] = vardai[i].upper()

print(vardai)

for i, val in enumerate(vardai):
    print(i, val)

for i, vyriskio_vardas in enumerate(vardai):
    print(f'{i+1}. {vyriskio_vardas};')


names = [
    "Alexander", "Benjamin", "Charlotte", "Daniel", "Elizabeth",
    "Frederick", "Gabriella", "Henry", "Isabella", "Jacob",
    "Katherine", "Liam", "Madeline", "Nathaniel", "Olivia",
    "Patrick", "Quinn", "Rebecca", "Samuel", "Theresa",
    "Ulysses", "Victoria", "William", "Xavier", "Yvonne",
    "Zachary", "Abigail", "Brandon", "Cassandra", "Derek",
    "Emily", "Francis", "Grace", "Hannah", "Ian",
    "Julia", "Kevin", "Laura", "Michael", "Natalie",
    "Oscar", "Penelope", "Quincy", "Rachel", "Stephen",
    "Tracy", "Uma", "Vincent", "Wendy", "Yosef"
]

for name in names: #du identacijos lygiai
    if len(name) <= 4:
        print(name)

# select name from names where length(name) <= 4;
print("=======================")
for i, name in enumerate(names):
    if i % 5 == 0:  # 7 % 5 = 2   2! = 0;    20 % 5 = 0; 0 == 0;
        print(i, name)


print("-----------------------------------")
arr2d = [
    [1, 4, 10], # 0
    [3, 5, 8], # 1
    [1, 2, 3], # 2
    [5, 10, 5], # 3
]

print(arr2d)
for row in arr2d:
    print(row)

print("-----------------------------------")
suma = 0
count = 0
for row in arr2d:
    for data in row:
        suma = suma + data
        count += 1
print(f'suma {suma}, kiekis {count}, vidurkis {suma /count}.')

# matematika lietuviu fizika
# 1           4       10
# 3           5       8
suma = 0
for row in arr2d[1:3]:
    for cell in row[1:]:
        suma += cell
        print(cell)
print(suma)

print("-----------------------")
for i in range(10):
    print("Dienos skaicius yra:")
    if i % 2 == 0:
        continue
    print(i)

print("==========================")
for i in range(1, 10):
    print("Dienos skaicius yra:")
    if i % 4 == 0:
        break
    print(i)

counter = 0
while True:
    counter +=1
    if counter >= 4:
        break
    print("hahaha", counter)


print("==========================")
counter = 0
should_continue = True
while should_continue:
    counter +=1
    if counter >= 4:
        should_continue = False
    print("hahaha", counter)


# rnd_num = random.randint(1,6)
# while rnd_num != 6:
#     print(rnd_num)

while True:
    dice = random.randint(1,6)
    print(dice)
    if dice == 6:
        break
print("==========================")

should_roll_dice = True
while should_roll_dice:
    dice = random.randint(1,6)
    print(dice)
    if dice == 6:
        should_roll_dice = False

# magic words +
# x*y +
# sort +
# while +

for y in range(1,11):
    for x in range(1,11):
        print(f'{x * y: >3}', end=" ")
    print()

print("==========================")

for y in range(1, 11):
    row = ""
    for x in range(1, 11):
        row = row + str(x * y) + " "
    print(row)
print("==========================")

#       0 1 2  3 4 5
arr = [ 1,4,12,3,2,8]
print(arr)

for a in range(len(arr)):
    for i in range(len(arr) -1):
        if arr[i] > arr[i + 1]:
            temp = arr[i] # temp = 1
            arr[i] = arr[i + 1] # arr[i] = 4
            arr [i + 1] = temp # arr[i+1] = 1
print(arr)



# Basic:
## 1. Crear una lista que contenga las letras de una palabra, cada una en mayúscula
word = str(input("Word:"))
wordUp = word.upper()
wordList = list(wordUp)

print(wordList)

## 1.1
word = str(input("Word:"))
listWord = [x.upper() for x in word]

print(listWord)

## 2. Crear un diccionario que contenga el cuadrado de cada número del 1 al 5
numSquare = {}
for num in range(1, 6):
    numSquare[num] = num**2

print(numSquare)

## 2.1
numSquare = {num: num**2 for num in range(1, 6)}

print(numSquare)
## 3. Crear un diccionario que contenga los nombres y edades de varias personas
listNames = {}
while True:
    name = str(input("Input the name:"))
    if name == "Done":
        break
    age = int(input("Input the age:"))
    listNames[name] = age

for name, age in listNames.items():
    print(f"{name} is {age}")

print(listNames)

# Advanced:
## 1. Crear una lista que contenga los números del 1 al 20, pero reemplazando los múltiplos de 3 por `"EOI"`, los múltiplos de 5 por `"Cloud"` y los múltiplos de ambos por `"EOICloud"`
listofNumb = []

for i in range(1, 21):  
    if i % 3 == 0 and i % 5 == 0:
        listofNumb.append("EOICloud")
    elif i % 3 == 0:
        listofNumb.append("EOI")
    elif i % 5 == 0:
        listofNumb.append("Cloud")
    else:
        listofNumb.append(i)

print(listofNumb)

## 1.1
listofNumb = ["EOICloud" if i % 3 == 0 and i % 5 == 0 else "EOI" if i % 3 == 0 else "Cloud" if i % 5 == 0 else i for i in range(1, 21)]

print(listofNumb)


## 2. Crear un diccionario que contenga las palabras en una lista y la cantidad de veces que aparecen en ella
list = ["apple", "banana", "cherry", "banana", "apple", "cherry"]
wordCounts = {}

for word in list:
    if word in wordCounts:
        wordCounts[word] += 1
    else:
        wordCounts[word] = 1

print(wordCounts)

## 3. Dado un texto con una lista de ciudades con su emblema mas importante, pedir las ciudades para que las entre el usuario por teclado y crear un diccionario con su ciudad y su emblema. **Nota** el diccionario deberá ordenarse por su clave
cityEmblem = {
    'New York': 'The Statue of Liberty',
    'Tokyo': 'The cherry blossom',
    'Paris': 'The Eiffel Tower',
    'London': 'Big Ben',
    'Sydney': 'The Sydney Opera House',
    'Buenos Aires': 'The Obelisk',
    'Johannesburg': 'The Lion',
    'Moscow': 'The Kremlin',
    'Amsterdam': 'The windmills',
    'Dubai': 'The Burj Khalifa'
}
cities = input("Enter the cities separated by commas: ").split(',')

result = {}
for city in cities:
    city = city.strip()
    if city in cityEmblem:
        result[city] = cityEmblem[city]

# result = {city.strip(): cityEmblem[city.strip()] for city in cities if city.strip() in cityEmblem}

result = dict(sorted(result.items()))

print(result)
#listas
lista = [0,1,2,3,4,4]
print(lista)
lista.append(5)
print(lista)
lista.pop()
print(lista)

#tuplas - Listas imutáveis
tuplas = (0,1,2,3)
print(tuplas)
print(tuplas[0])

#set - Não permitem a inserção do mesmo valor, porém não possuem índices e não podem ser ordenadas
sets = {6,5,4,3,2}
print(sets)
sets.add(8)
print(sets)
sets.add(6)
print(sets)

#Conversões de variáveis
tuplas = tuple(lista)
print(tuplas)
lista = list(tuplas)
print(lista)
sets = set(lista)
print(sets)

#List comprehension
palavra_secreta = "banana".upper()
letras_acertadas = ["_" for letra in palavra_secreta]
print(letras_acertadas)

inteiros = [1,3,4,5,7,8,9]
print(inteiros)
pares = [x for x in inteiros if x % 2 == 0]
print(pares)
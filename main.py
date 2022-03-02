#Escribe una función palindromo la cual recibe como parametro una cadena/string
#La función debe regresar True si la palabra es un palíndromo
#Ejemplo de Palíndromos: oso, salas, seres, radar
def palindromo(palabra):
    inicio = 0
    final = len(palabra)-1

    while inicio < len(palabra) / 2: #Llegamos a la mitad #for i in range(0, len(palabra) / 2)
        if palabra[inicio] != palabra[final]:
            return False
        inicio += 1
        final -= 1
    return True

# print(palindromo("oso"))
# print(palindromo("radar"))
# print(palindromo("muñeca"))
# print(palindromo("compu"))
# print(palindromo("salas"))


#Escribe una función reverseString, la cual recibe como parámetro una cadena/string
#Y regresa el string al revés
#Ejemplo: Buenos días => saíd soneuB
#cadena = "Buenos"
#newString = ""
#FOR -> i = 6-1; i = 5. i MAX 0, i recorre -1
#i = 5
#newString += cadena[5] -> s; newString = s

#i = 4; 
#newString += cadena[4] -> o; newString = so

#i = 3;
#newString += cadena[3] -> n; newString = son

#i = 2
#newString += cadena[2] -> e; newString = sone

#i = 1
#newString += cadena[1] -> u; newString = soneu

#i = 0
#newString += cadena[0] -> B; newString = soneuB

#i = -1
#STOP

def reverseString(cadena): #Cadena= OSO -> 3. Ultima posicion 2
    newString = ""
    for i in range(len(cadena)-1, -1, -1): #Rango 2-0, recorriendo de -1 en -1 #2 -> 1 -> 0
        newString += cadena[i]
    return newString


# cadena = input('Escribe una palabra que quieras al revés ')
# print(reverseString(cadena))

pal = input('Escribe una palabra que creas que es palíndromo: ')
print(palindromo(pal))

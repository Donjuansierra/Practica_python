"""
Codelab: Variables Python
"""

entero = 1
decimal = 3.1416
cadena = 'Mi nombre es Juan Sebastian Sierra Chaparro'
booleano = True

# i
concatenacion = str(entero)+', ' + str(decimal) + ', '+ cadena +', '+ str(booleano)

k = '%s, %s, %s, %s' % (entero, decimal, cadena, booleano)

# ii

"""
Los numeros enteros (int) y decimales (float) en python no tienen limite de tamaño
Lo anterior debido a que python por debajo se encarga de asignar más o menos memoria al número, y podemos representar prácticamente cualquier número
"""

# iii

n = int(input ('ingresa la cantidad de primeros numeros pares a sumar: '))

suma_pares = n*(n+1)


# iv

print (entero, decimal, cadena, booleano, concatenacion, k, suma_pares, sep = '\n') 



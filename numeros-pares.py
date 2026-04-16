#CONDICIONAL
"""if condicion:
    print("")
    elif condicion:
    print("")
    else: 
    print("")
    
    """

#ESTRUCTURA DE REPETICION
""" for i in range(11) --va a loopear 10 veces--
    nota = input ("ingrese nota:")
        if nota == "salir"
    break
"""
"""while True: --se va a loopear indefinido hasta que usuario escriba salir--
    nota = input ("ingrese nota:")
        if nota == "salir"
    break
"""


# Script para mostrar los primeros 10 números pares
contador_pares = 0
numero = 1

print("Los primeros 10 números pares son:")

# Usamos un bucle while para encontrar exactamente 10 números
while contador_pares < 10:
    # El condicional valida si el número es par (divisible por 2)
    if numero % 2 == 0:
        print(numero)
        contador_pares += 1  # Aumentamos el contador solo cuando encontramos un par
    
    numero += 1  # Pasamos al siguiente número en cada vuelta


""" print(#range 11) imprime del 1 al 10, lo que comprende los parentesis
print(#range (0,21,5)) va a imprimir del 0 al 20, de 5 en 5...


# Otra forma usando un bucle for en un rango amplio
for n in range(1, 21):
    if n % 2 == 0:
        print(f"Número par encontrado: {n}")
        """
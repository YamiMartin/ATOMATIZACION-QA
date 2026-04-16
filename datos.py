nombre = (input("Por favor ingrese su nombre: " ))
edad = int(input("Por favor Ingrese du edad: "))
profesion = (input ("Por favor ingrese su profesion: "))

print(f"Hola {nombre}, tu edad es {edad} años y sos {profesion}")

""" LISTAS son modificables y tiene indice desde "0"
frutas = ["Banana", "frutilla", "Tomate"]
print(frutas)
print(frutas[0]) imprime la fruta con ese indice
frutas.append("Sandia")// para sumar algo a la lista
frutas.remove("Tomate")
frutas.sort() ordena alfabeticamente
frutas.sort(key=len) es por longitud de palabra
    """

"""
TUPLA guarda distintos tipos de datos
para desempaquetar hay que respetar la cantidad de valores que tiene esa tupla

"""

"""DICCIONARIOS
datos no ordenado, clave y valor
persona = {
"Nombre": "Luis",
"Apellido": "Barraza",
"edad": 34
}

print(persona["edad"])
print(persona.keys()) me devuelve las claves de diccionario
print(persona.value()) me devuelve los valores de dicc
print(persona.items()) devuelve listado del par

for i in persona:
print(i) claves
print(persona[i]) accedo al indice y me imprime valores

"""

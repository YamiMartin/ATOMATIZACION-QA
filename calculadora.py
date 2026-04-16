from calculadora.opciones import pedir_numero, pedir_opcion
from calculadora.operaciones import sumar, restar , multiplicar, dividir

while True:
    opcion = pedir_opcion()

    if opcion in ["1", "2", "3", "4"]:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))

    match opcion:
        case "1":
            print("Resultado ", sumar(a,b) )
        case "2":
            print("Resultado ", restar(a,b))
        case "3":
            print("Resultado ", multiplicar(a,b) )
        case "4":
            print("Resultado ", dividir(a,b))
        case _:
            print("Opcion invalida, elgí entre 1 y 4")

    otra = input("¿Querés hacer otra operacion ( s/n )")

    if otra != "s":
        print("Hasta la proxima!!!!!")
        break
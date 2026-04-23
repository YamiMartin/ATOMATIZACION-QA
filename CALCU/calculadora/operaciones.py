def sumar( a , b ):
    return a + b 

def restar( a , b ):
    return a - b 

def multiplicar(a, b):
    return a * b

def dividir( a , b ):
    if b == 0:
        # En lugar de print("No se puede..."), usamos raise:
        raise ValueError("No se puede dividir por cero")
    return a / b
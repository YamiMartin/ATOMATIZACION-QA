def sumar( a , b ):
    return a + b 

def restar( a , b ):
    return a - b 

def multiplicar( a , b ):
     if a == 0 or b == 0:
        return 0
        return a * b 

def dividir( a , b ):
    try:
         return a / b 
    except ZeroDivisionError:
        print("No se puede dividir por cero")
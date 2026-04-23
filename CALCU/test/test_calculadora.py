import pytest
from calculadora.opciones import pedir_numero, pedir_opcion
from calculadora.operaciones import sumar, restar , multiplicar, dividir

#CASOS DE PRUEBA
@pytest.mark.suma
def test_sumar_positivos(numeros): #INVOCO LOS NUMEROS DE CONFTEST
    assert sumar(*numeros) == 12 #los estoy desempaquetando del conftest fixture
     #a,b
    
def test_sumar_negativos ():
    assert sumar(-3,-1) == -4


def test_multiplicar(numeros):
    a,b = numeros #los estoy desempaquetando del conftest fixture
    assert multiplicar(a,b) == 20

@pytest.mark.parametrize("a,b, resultado",[
    (3,3,6),
    (5,15,20),
    (6,6,12)
],
ids=["caso1", "caso2", "caso3"]
) #recibe string y un obj diccionario

def test_sumar_casos_parametrize(a, b, resultado):
    assert sumar(a,b) == resultado
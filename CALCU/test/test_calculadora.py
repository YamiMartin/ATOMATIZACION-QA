import pytest
from calculadora.opciones import pedir_numero, pedir_opcion
from calculadora.operaciones import sumar, restar , multiplicar, dividir

#CASOS DE PRUEBA

# 1. FIXTURE DE FLOTANTES (Punto 2 de la consigna)
@pytest.fixture
def numeros_flotantes():
    return (0.1, 0.2)

@pytest.mark.suma
def test_sumar_positivos(numeros): #INVOCO LOS NUMEROS DE CONFTEST
    assert sumar(*numeros) == 12 #los estoy desempaquetando del conftest fixture
     #a,b
    
def test_sumar_negativos ():
    assert sumar(-3,-1) == -4


def test_multiplicar(numeros):
    a,b = numeros #los estoy desempaquetando del conftest fixture
    assert multiplicar(a,b) == 20

def test_multiplicar_por_cero():
    assert multiplicar(5, 0) == 0

# 2. TESTS DE SUMA (Parametrizados y marcados como Smoke)
@pytest.mark.smoke
@pytest.mark.parametrize("a,b, resultado",[
    (3,3,6),
    (5,15,20),
    (6,6,12)
],
ids=["caso1", "caso2", "caso3"]
) #recibe string y un obj diccionario

def test_sumar_casos_parametrize(a, b, resultado):
    assert sumar(a,b) == resultado

@pytest.mark.smoke
def test_sumar_flotantes(numeros_flotantes):
    # Usamos pytest.approx para evitar errores de precisión decimal en Python
    assert sumar(*numeros_flotantes) == pytest.approx(0.3)

# 5. TESTS DE DIVIDIR (Marcados como Exception)
def test_dividir_exito():
    assert dividir(10, 2) == 5

@pytest.mark.exception
def test_dividir_error_cero():
    with pytest.raises(ValueError):
        dividir(10, 0)
# 3. TESTS DE RESTA (Parametrizados)
@pytest.mark.parametrize("a, b, resultado", [
    (10, 5, 5),
    (20, 30, -10),
    (0, 0, 0)
], ids=["resta_1", "resta_2", "resta_3"])
def test_restar_parametrize(a, b, resultado):
    assert restar(a, b) == resultado
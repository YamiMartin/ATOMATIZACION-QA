import pytest
from app.carrito_funciones import agregar_producto


def test_agregar_producto(carrito_vacio, producto_teclado):  
    resultado = agregar_producto(carrito_vacio, producto_teclado)

    assert len(resultado) == 1 #verifico que carrito no este en 0
    #assert resultado[0]["Nombre"] == "Teclado" #veo si se agrego
    
def test_validar_nombre_carrito(carrito_vacio, producto_teclado):
    resultado = agregar_producto(carrito_vacio, producto_teclado)

    assert resultado[0]["Precio"] == 3000

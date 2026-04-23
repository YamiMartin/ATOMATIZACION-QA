import pytest

@pytest.fixture
def producto_teclado():
    return {"Nombre": "Teclado", "Precio": 3000}

@pytest.fixture
def carrito_vacio():
    return []

@pytest.fixture
def listado_productos():
    return [
        {"Nombre": "Teclado", "Precio": 3000},
        {"Nombre": "Mouse", "Precio": 2000},
        {"Nombre": "Laptop", "Precio": 250000},
        {"Nombre": "Memoria", "Precio": 83000},
        {"Nombre": "USB", "Precio": 25000},
        ]
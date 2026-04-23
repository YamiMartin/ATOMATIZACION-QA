import pytest
from app.auth_funciones import register, login, logout, usuarios #Importo lista de usuarios

#Limpio listado antes de empezar (Fixture)
@pytest.fixture(autouse=True)
def clean_data():
    usuarios.clear() # Vacía la lista antes de test, reinicia sesion activa
    import app.auth_funciones
    app.auth_funciones.sesion_activa = None
    yield            # Se ejecuta el test

#Test para evitar duplicados
def test_registro_duplicado():
    register("Juan", "123456")
    # Intentamos registrar al mismo usuario
    resultado = register("Juan", "999888") 
    assert resultado == "El usuario ya existe."
    assert len(usuarios) == 1 # Verificamos que no se agregó a la lista

# --- Tests para Logout ---
def test_logout_exitoso():
    register("Juan", "123456")
    login("Juan", "123456") # Iniciamos sesión primero
    assert logout() == "Sesión cerrada con éxito."

def test_logout_sin_sesion():
    # Intentamos cerrar sesión sin haber hecho login
    assert logout() == "No hay sesión activa."

@pytest.mark.register
@pytest.mark.parametrize("username, password, resultado",[
    ("Juan","123456","Registro Exitoso"), #exito
    ("","123456","Campos obligatorios vacíos."), #campo vacio
    ("Juan","123","No cumple con el minimo de longitud.")
])

def test_register(username, password, resultado):
    assert register(username, password) == resultado

@pytest.mark.parametrize("username, password, resultado",[
    ("Juan", "123456", "Login Exitoso"),
    ("Yami", "12345", "Credencial invalida")
    ])

def test_login (username, password, resultado): #Por Fixture, lisado vacio
    register("Juan","123456")
    assert login("Juan","123456") == "Login Exitoso"

def test_login_fallido():
    # Aquí la lista vuelve a estar vacía automáticamente
    assert login("Inexistente", "999") == "Credencial invalida"
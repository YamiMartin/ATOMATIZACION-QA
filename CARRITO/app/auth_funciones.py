usuarios = []
sesion_activa = None  # Variable para rastrear quién está logueado

def register (username, password):
    #usuario no me ingrese campos vacios
    if not username or not password:
        return "Campos obligatorios vacíos."
    
    # contraseña corta
    if len(password) < 4:
        return "No cumple con el minimo de longitud."

    #Evita duplicados
    for user in usuarios:
        if user["username"] == username:
            return "El usuario ya existe." 
        
    # agregar al restro
    usuarios.append({
        "username": username,
        "password": password
    })

    return "Registro Exitoso"

# register({"Username": "Yami", "Password": "1234"})

def login(username, password):
    global sesion_activa
    for user in usuarios:
        if user["username"] == username and user ["password"] == password:
            sesion_activa = username # Guardamos el usuario en la sesión
            return "Login Exitoso"
    
    return "Credencial invalida"

def logout():
    global sesion_activa
    if sesion_activa is None:
        return "No hay sesión activa."
    
    sesion_activa = None
    return "Sesión cerrada con éxito."
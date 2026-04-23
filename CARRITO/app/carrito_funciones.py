def agregar_producto(carrito, producto):
    carrito.append(producto)
    return carrito

if __name__ == "__main__":
    carrito = [] #vacio para luego agregar
    carrito = agregar_producto(carrito, {"Nombre": "Teclado", "Precio": 2000})
    print(carrito)
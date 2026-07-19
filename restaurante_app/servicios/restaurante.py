# Clase Restaurante
class Restaurante:

    # Constructor
    def __init__(self):
        self.productos = []
        self.clientes = []

    # Registrar producto
    def registrar_producto(self, producto):
        self.productos.append(producto)

    # Listar productos
    def listar_productos(self):
        if not self.productos:
            print("\nNo existen productos registrados.")
        else:
            print("\n===== LISTA DE PRODUCTOS =====")
            for producto in self.productos:
                print(producto.mostrar_informacion())
                print("-----------------------------")

    # Buscar producto
    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                return producto
        return None

    # Registrar cliente
    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)

    # Listar clientes
    def listar_clientes(self):
        if not self.clientes:
            print("\nNo existen clientes registrados.")
        else:
            print("\n===== LISTA DE CLIENTES =====")
            for cliente in self.clientes:
                print(cliente.mostrar_informacion())
                print("-----------------------------")

    # Buscar cliente
    def buscar_cliente(self, id_cliente):
        for cliente in self.clientes:
            if cliente.id_cliente == id_cliente:
                return cliente
        return None
    
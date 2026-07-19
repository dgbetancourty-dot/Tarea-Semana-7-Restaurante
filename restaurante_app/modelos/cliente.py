from dataclasses import dataclass

# Clase Cliente utilizando @dataclass
@dataclass
class Cliente:
    id_cliente: int
    nombre: str
    correo: str

    # Método para mostrar la información del cliente
    def mostrar_informacion(self):
        return (
            f"ID: {self.id_cliente}\n"
            f"Nombre: {self.nombre}\n"
            f"Correo: {self.correo}"
        )
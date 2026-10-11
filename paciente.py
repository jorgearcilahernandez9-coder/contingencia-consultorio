# datos de un paciente


class Paciente:

    def __init__(self, cedula, nombre, telefono, tipo_cliente, tipo_atencion, cantidad, prioridad, fecha, valor_atencion, valor_pagar):
        self.cedula = cedula
        self.nombre = nombre
        self.telefono = telefono
        self.tipo_cliente = tipo_cliente
        self.tipo_atencion = tipo_atencion
        self.cantidad = cantidad
        self.prioridad = prioridad
        self.fecha = fecha
        self.valor_atencion = valor_atencion
        self.valor_pagar = valor_pagar

    def mostrar_datos(self):
        print("")
        print("Cedula: " + self.cedula)
        print("Nombre: " + self.nombre)
        print("Telefono: " + self.telefono)
        print("Tipo cliente: " + self.tipo_cliente)
        print("Tipo atencion: " + self.tipo_atencion)
        print("Cantidad: " + str(self.cantidad))
        print("Prioridad: " + self.prioridad)
        print("Fecha cita: " + self.fecha)
        print("Valor atencion: $" + str(self.valor_atencion))
        print("Valor a pagar: $" + str(self.valor_pagar))

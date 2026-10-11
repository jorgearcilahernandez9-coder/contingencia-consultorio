# logica del consultorio odontologico

from paciente import Paciente
from pila import Pila
from cola import Cola
from datetime import datetime


class Consultorio:

    def __init__(self):
        self.lista_pacientes = []
        self.pila_urgencias = Pila()

    def cedula_existe(self, cedula_buscar):
        existe = False
        i = 0
        while i < len(self.lista_pacientes):
            if self.lista_pacientes[i].cedula == cedula_buscar:
                existe = True
            i = i + 1
        return existe

    def es_numero_entero(self, texto):
        if texto == "":
            return False
        es_numero = True
        pos = 0
        while pos < len(texto):
            if texto[pos] < "0" or texto[pos] > "9":
                es_numero = False
            pos = pos + 1
        return es_numero

    def obtener_valores(self, tipo_cliente, tipo_atencion, cantidad):
        # valores de la tabla del ejercicio
        valor_cita = 0
        valor_atencion = 0

        if tipo_cliente == "Particular":
            valor_cita = 80000
            if tipo_atencion == "Limpieza":
                valor_atencion = 60000
            elif tipo_atencion == "Calzas":
                valor_atencion = 80000
            elif tipo_atencion == "Extraccion":
                valor_atencion = 100000
            elif tipo_atencion == "Diagnostico":
                valor_atencion = 50000

        elif tipo_cliente == "EPS":
            valor_cita = 5000
            if tipo_atencion == "Limpieza":
                valor_atencion = 0
            elif tipo_atencion == "Calzas":
                valor_atencion = 40000
            elif tipo_atencion == "Extraccion":
                valor_atencion = 40000
            elif tipo_atencion == "Diagnostico":
                valor_atencion = 0

        elif tipo_cliente == "Prepagada":
            valor_cita = 30000
            if tipo_atencion == "Limpieza":
                valor_atencion = 0
            elif tipo_atencion == "Calzas":
                valor_atencion = 10000
            elif tipo_atencion == "Extraccion":
                valor_atencion = 10000
            elif tipo_atencion == "Diagnostico":
                valor_atencion = 0

        valor_pagar = valor_cita + (valor_atencion * cantidad)
        return valor_atencion, valor_pagar

    def registrar_paciente(self):
        print("")
        print("--- REGISTRO DE CLIENTE ---")

        cedula_ingresada = input("Digite la cedula del cliente: ")
        if cedula_ingresada == "":
            print("Error: la cedula no puede estar vacia.")
            return

        if self.cedula_existe(cedula_ingresada) == True:
            print("Error: ya existe un cliente con esa cedula.")
            return

        nombre_paciente = input("Digite el nombre del cliente: ")
        if nombre_paciente == "":
            print("Error: el nombre no puede estar vacio.")
            return

        telefono_paciente = input("Digite el telefono del cliente: ")
        if telefono_paciente == "":
            print("Error: el telefono no puede estar vacio.")
            return

        print("")
        print("Tipo de cliente:")
        print("1. Particular")
        print("2. EPS")
        print("3. Prepagada")
        opcion_cliente = input("Seleccione el tipo de cliente (1-3): ")

        tipo_cliente_guardado = ""
        if opcion_cliente == "1":
            tipo_cliente_guardado = "Particular"
        elif opcion_cliente == "2":
            tipo_cliente_guardado = "EPS"
        elif opcion_cliente == "3":
            tipo_cliente_guardado = "Prepagada"
        else:
            print("Error: tipo de cliente no valido.")
            return

        print("")
        print("Tipo de atencion:")
        print("1. Limpieza")
        print("2. Calzas")
        print("3. Extraccion")
        print("4. Diagnostico")
        opcion_atencion = input("Seleccione el tipo de atencion (1-4): ")

        tipo_atencion_guardado = ""
        if opcion_atencion == "1":
            tipo_atencion_guardado = "Limpieza"
        elif opcion_atencion == "2":
            tipo_atencion_guardado = "Calzas"
        elif opcion_atencion == "3":
            tipo_atencion_guardado = "Extraccion"
        elif opcion_atencion == "4":
            tipo_atencion_guardado = "Diagnostico"
        else:
            print("Error: tipo de atencion no valido.")
            return

        cantidad_ingresada = 1

        if tipo_atencion_guardado == "Limpieza":
            print("Para Limpieza la cantidad es siempre 1.")
        elif tipo_atencion_guardado == "Diagnostico":
            print("Para Diagnostico la cantidad es siempre 1.")
        else:
            texto_cantidad = input("Digite la cantidad: ")
            if self.es_numero_entero(texto_cantidad) == False:
                print("Error: la cantidad debe ser un numero mayor que cero.")
                return
            cantidad_ingresada = int(texto_cantidad)
            if cantidad_ingresada <= 0:
                print("Error: la cantidad debe ser mayor que cero.")
                return

        print("")
        print("Prioridad de atencion:")
        print("1. Normal")
        print("2. Urgente")
        opcion_prioridad = input("Seleccione la prioridad (1-2): ")

        prioridad_guardada = ""
        if opcion_prioridad == "1":
            prioridad_guardada = "Normal"
        elif opcion_prioridad == "2":
            prioridad_guardada = "Urgente"
        else:
            print("Error: prioridad no valida.")
            return

        fecha_cita = input("Digite la fecha de la cita (dd/mm/aaaa): ")
        try:
            fecha_cita = datetime.strptime(fecha_cita, "%d/%m/%Y").strftime("%d/%m/%Y")
        except ValueError:
            print("Error: la fecha debe existir y tener el formato dd/mm/aaaa.")
            return

        valor_atencion, valor_pagar = self.obtener_valores(tipo_cliente_guardado, tipo_atencion_guardado, cantidad_ingresada)

        paciente_nuevo = Paciente(
            cedula_ingresada,
            nombre_paciente,
            telefono_paciente,
            tipo_cliente_guardado,
            tipo_atencion_guardado,
            cantidad_ingresada,
            prioridad_guardada,
            fecha_cita,
            valor_atencion,
            valor_pagar
        )

        self.lista_pacientes.append(paciente_nuevo)

        print("")
        print("Cliente registrado correctamente.")
        print("Valor a pagar: $" + str(valor_pagar))

    def mostrar_pacientes(self):
        print("")
        print("--- LISTA DE CLIENTES ---")
        if len(self.lista_pacientes) == 0:
            print("No hay clientes registrados.")
        else:
            indice = 0
            while indice < len(self.lista_pacientes):
                print("")
                print("Cliente numero " + str(indice + 1))
                self.lista_pacientes[indice].mostrar_datos()
                indice = indice + 1

    def ordenar_burbuja(self):
        # ordenamos por el valor de la atencion de mayor a menor
        print("")
        print("--- ORDENAMIENTO POR BURBUJA ---")
        if len(self.lista_pacientes) == 0:
            print("No hay clientes para ordenar.")
            return

        n = len(self.lista_pacientes)
        for i in range(n):
            for j in range(0, n - i - 1):
                valor_actual = self.lista_pacientes[j].valor_atencion
                valor_siguiente = self.lista_pacientes[j + 1].valor_atencion
                if valor_actual < valor_siguiente:
                    temp = self.lista_pacientes[j]
                    self.lista_pacientes[j] = self.lista_pacientes[j + 1]
                    self.lista_pacientes[j + 1] = temp

        print("Lista ordenada de mayor a menor por valor de atencion.")
        print("")
        k = 0
        while k < len(self.lista_pacientes):
            paciente = self.lista_pacientes[k]
            print(paciente.nombre + " | Cedula: " + paciente.cedula + " | Valor atencion: $" + str(paciente.valor_atencion))
            k = k + 1

    def buscar_por_cedula(self):
        print("")
        print("--- BUSCAR CLIENTE POR CEDULA ---")
        if len(self.lista_pacientes) == 0:
            print("No hay clientes registrados.")
            return

        cedula_buscar = input("Digite la cedula a buscar: ")
        if cedula_buscar == "":
            print("Error: debe digitar una cedula.")
            return

        paciente_encontrado = False
        pos = 0
        while pos < len(self.lista_pacientes):
            if self.lista_pacientes[pos].cedula == cedula_buscar:
                paciente_encontrado = True
                print("")
                print("Cliente encontrado en la posicion " + str(pos + 1))
                self.lista_pacientes[pos].mostrar_datos()
                break
            pos = pos + 1

        if paciente_encontrado == False:
            print("No se encontro ningun cliente con esa cedula.")

    def generar_pila_urgencias(self):
        print("")
        print("--- PILA DE EXTRACCIONES URGENTES ---")

        clientes_urgentes = []
        indice = 0
        while indice < len(self.lista_pacientes):
            paciente = self.lista_pacientes[indice]
            if paciente.tipo_atencion == "Extraccion" and paciente.prioridad == "Urgente":
                clientes_urgentes.append(paciente)
            indice = indice + 1

        if len(clientes_urgentes) == 0:
            print("No hay clientes con extraccion urgente.")
            return

        # Se ordena de la fecha mas lejana a la mas cercana.
        # Al apilar en ese orden, la fecha mas cercana queda arriba.
        n = len(clientes_urgentes)
        for i in range(n):
            for j in range(0, n - i - 1):
                fecha_actual = datetime.strptime(clientes_urgentes[j].fecha, "%d/%m/%Y")
                fecha_siguiente = datetime.strptime(clientes_urgentes[j + 1].fecha, "%d/%m/%Y")
                if fecha_actual < fecha_siguiente:
                    temporal = clientes_urgentes[j]
                    clientes_urgentes[j] = clientes_urgentes[j + 1]
                    clientes_urgentes[j + 1] = temporal

        # Se guarda la pila en el consultorio para conservarla despues del informe.
        self.pila_urgencias = Pila()
        indice = 0
        while indice < len(clientes_urgentes):
            self.pila_urgencias.apilar(clientes_urgentes[indice])
            indice = indice + 1

        print("Informe de clientes para llamar, desde la fecha mas cercana:")
        print("Cantidad de clientes urgentes: " + str(self.pila_urgencias.cantidad()))

        # Se usa una pila auxiliar para mostrar el informe sin perder los pacientes.
        pila_auxiliar = Pila()
        posicion = 1
        while self.pila_urgencias.esta_vacia() == False:
            paciente = self.pila_urgencias.desapilar()
            print("")
            print("Prioridad numero " + str(posicion))
            print("Nombre: " + paciente.nombre)
            print("Cedula: " + paciente.cedula)
            print("Telefono: " + paciente.telefono)
            print("Tipo de atencion: " + paciente.tipo_atencion)
            print("Prioridad: " + paciente.prioridad)
            print("Fecha de cita: " + paciente.fecha)
            pila_auxiliar.apilar(paciente)
            posicion = posicion + 1

        # Se devuelven los pacientes a la pila original en el mismo orden.
        while pila_auxiliar.esta_vacia() == False:
            self.pila_urgencias.apilar(pila_auxiliar.desapilar())

        print("")
        print("La pila conserva los clientes urgentes para futuras consultas.")

    def generar_cola_atencion(self):
        print("")
        print("--- COLA DE ATENCION DIARIA ---")
        if len(self.lista_pacientes) == 0:
            print("No hay clientes registrados.")
            return

        fecha_buscar = input("Digite la fecha de la agenda (dd/mm/aaaa): ")
        try:
            fecha_buscar = datetime.strptime(fecha_buscar, "%d/%m/%Y").strftime("%d/%m/%Y")
        except ValueError:
            print("Error: la fecha debe existir y tener el formato dd/mm/aaaa.")
            return

        clientes_agenda = []
        indice = 0
        while indice < len(self.lista_pacientes):
            paciente = self.lista_pacientes[indice]
            if paciente.fecha == fecha_buscar:
                clientes_agenda.append(paciente)
            indice = indice + 1

        if len(clientes_agenda) == 0:
            print("No hay clientes agendados para esa fecha.")
            return

        # La agenda conserva el orden en que se registraron los clientes
        # para esa fecha. La cola atiende primero al que ingreso primero.
        cola_atencion = Cola()
        indice = 0
        while indice < len(clientes_agenda):
            cola_atencion.encolar(clientes_agenda[indice])
            indice = indice + 1

        print("")
        print("Agenda del " + fecha_buscar)
        print("Cantidad de clientes: " + str(cola_atencion.cantidad()))

        numero = 1
        while cola_atencion.esta_vacia() == False:
            paciente = cola_atencion.desencolar()
            print("")
            print("Atendiendo cliente numero " + str(numero))
            print("Nombre: " + paciente.nombre)
            print("Cedula: " + paciente.cedula)
            print("Tipo de atencion: " + paciente.tipo_atencion)
            print("Prioridad: " + paciente.prioridad)
            print("Fecha de cita: " + paciente.fecha)
            numero = numero + 1

        print("")
        print("La cola de atencion quedo vacia.")

    def mostrar_estadisticas(self):
        print("")
        print("--- ESTADISTICAS ---")
        if len(self.lista_pacientes) == 0:
            print("No hay datos para mostrar.")
            return

        total_clientes = len(self.lista_pacientes)

        ingresos_totales = 0
        indice = 0
        while indice < len(self.lista_pacientes):
            ingresos_totales = ingresos_totales + self.lista_pacientes[indice].valor_pagar
            indice = indice + 1

        clientes_extraccion = 0
        indice = 0
        while indice < len(self.lista_pacientes):
            if self.lista_pacientes[indice].tipo_atencion == "Extraccion":
                clientes_extraccion = clientes_extraccion + 1
            indice = indice + 1

        print("Total clientes: " + str(total_clientes))
        print("Ingresos totales recibidos: $" + str(ingresos_totales))
        print("Numero de clientes con extraccion: " + str(clientes_extraccion))

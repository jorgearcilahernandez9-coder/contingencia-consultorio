# Consultorio odontologico
# Programacion II

from consultorio import Consultorio


consultorio = Consultorio()

bandera_menu = True

print("==============================================")
print("       CONSULTORIO ODONTOLOGICO")
print("==============================================")

while bandera_menu == True:
    print("")
    print("---------- MENU PRINCIPAL ----------")
    print("1. Registrar cliente")
    print("2. Ver lista de clientes")
    print("3. Ordenar clientes por valor de atencion")
    print("4. Buscar cliente por cedula")
    print("5. Ver estadisticas")
    print("6. Generar pila de extracciones urgentes")
    print("7. Generar cola de atencion diaria")
    print("8. Salir")
    print("------------------------------------")

    opcion_seleccionada = input("Digite la opcion que desea: ")

    if opcion_seleccionada == "1":
        consultorio.registrar_paciente()

    elif opcion_seleccionada == "2":
        consultorio.mostrar_pacientes()

    elif opcion_seleccionada == "3":
        consultorio.ordenar_burbuja()

    elif opcion_seleccionada == "4":
        consultorio.buscar_por_cedula()

    elif opcion_seleccionada == "5":
        consultorio.mostrar_estadisticas()

    elif opcion_seleccionada == "6":
        consultorio.generar_pila_urgencias()

    elif opcion_seleccionada == "7":
        consultorio.generar_cola_atencion()

    elif opcion_seleccionada == "8":
        print("")
        print("Gracias por usar el sistema del consultorio odontologico.")
        bandera_menu = False

    else:
        print("Opcion no valida. Intente de nuevo.")

print("")
print("Programa finalizado.")

from modelos.usuario import Usuario
from modelos.vehiculo import Vehiculo
from servicios.sistema_transito import SistemaTransitoInteligente


def mostrar_menu():
    print("\n=== MENÚ DEL SISTEMA ===")
    print("1. Registrar usuario")
    print("2. Buscar usuario")
    print("3. Registrar vehículo a un usuario")
    print("4. Ver usuarios")
    print("5. Salir")


def registrar_usuario_desde_input(sistema):
    print("\n=== REGISTRO DE USUARIO ===")
    id_usuario = int(input("Ingrese el id del usuario: "))

    usuario_existente = sistema.buscar_usuario_por_id(id_usuario)
    if usuario_existente:
        print("Ya existe un usuario con ese id.")
        return

    nombre = input("Ingrese el nombre: ")
    correo = input("Ingrese el correo: ")

    usuario = Usuario(id_usuario, nombre, correo)
    sistema.registrar_usuario(usuario)
    print("Usuario registrado correctamente.")


def buscar_usuario_desde_input(sistema):
    print("\n=== BÚSQUEDA DE USUARIO ===")
    id_usuario = int(input("Ingrese el id del usuario a buscar: "))

    usuario = sistema.buscar_usuario_por_id(id_usuario)

    if usuario:
        print("\nUsuario encontrado:")
        print(usuario)
        print("Vehículos registrados:")
        print(usuario.mostrar_vehiculos())
    else:
        print("El usuario no está registrado.")
        opcion = input("Escriba s para SI o n para NO: ").lower()

        if opcion == "s":
            nombre = input("Ingrese el nombre: ")
            correo = input("Ingrese el correo: ")

            nuevo_usuario = Usuario(id_usuario, nombre, correo)
            sistema.registrar_usuario(nuevo_usuario)
            print("Usuario registrado correctamente.")
        else:
            print("No se registró el usuario.")


def registrar_vehiculo_desde_input(sistema):
    print("\n=== REGISTRO DE VEHÍCULO ===")
    id_usuario = int(input("Ingrese el id del usuario: "))

    usuario = sistema.buscar_usuario_por_id(id_usuario)

    if usuario:
        print(f"Usuario encontrado: {usuario.nombre}")

        placa = input("Ingrese la placa del vehículo: ")
        tipo = input("Ingrese el tipo de vehículo: ")
        marca = input("Ingrese la marca: ")
        modelo = input("Ingrese el modelo: ")
        color = input("Ingrese el color: ")

        vehiculo = Vehiculo(placa, tipo, marca, modelo, color)
        sistema.registrar_vehiculo_a_usuario(id_usuario, vehiculo)

        print("Vehículo registrado correctamente al usuario.")
    else:
        print("El usuario no está registrado.")
        opcion = input("¿Desea registrar primero al usuario? (s/n): ").lower()

        if opcion == "s":
            nombre = input("Ingrese el nombre del usuario: ")
            correo = input("Ingrese el correo del usuario: ")

            nuevo_usuario = Usuario(id_usuario, nombre, correo)
            sistema.registrar_usuario(nuevo_usuario)
            print("Usuario registrado correctamente.")

            print("\nAhora registre el vehículo:")
            placa = input("Ingrese la placa del vehículo: ")
            tipo = input("Ingrese el tipo de vehículo: ")
            marca = input("Ingrese la marca: ")
            modelo = input("Ingrese el modelo: ")
            color = input("Ingrese el color: ")

            vehiculo = Vehiculo(placa, tipo, marca, modelo, color)
            sistema.registrar_vehiculo_a_usuario(id_usuario, vehiculo)

            print("Vehículo registrado correctamente al usuario.")
        else:
            print("No se registró el vehículo.")


def main():
    sistema = SistemaTransitoInteligente()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario_desde_input(sistema)

        elif opcion == "2":
            buscar_usuario_desde_input(sistema)

        elif opcion == "3":
            registrar_vehiculo_desde_input(sistema)

        elif opcion == "4":
            print("\n=== USUARIOS Y VEHÍCULOS REGISTRADOS ===")
            print(sistema.mostrar_usuarios())

        elif opcion == "5":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


if _name_ == "_main_":
    main()
    
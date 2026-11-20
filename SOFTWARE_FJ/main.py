from sistema import Sistema
from cliente import Cliente
from excepciones import (ReservaYaCanceladaError, ServicioNoRegistradoError, ReservaNoEncontradaError, ClienteDuplicadoError, ClienteNoEncontradoError, ClienteNoRegistradoError)
from servicio import ServicioSala, ServicioEquipo, ServicioAsesoria
from excepciones import ServicioDuplicadoError, ServicioNoEncontradoError
from reserva import Reserva

sistema = Sistema()
def gestionar_clientes():
    while True:
        print("\n===== GESTIONAR CLIENTES =====")
        print("1. Registrar cliente")
        print("2. Buscar cliente")
        print("3. Listar clientes")
        print("4. Volver al menú principal")

        opcion = input("Seleccione una opcion: ").strip()
        
        if opcion == "1":
            identificacion = input("Identificacion: ")
            nombre = input("Nombre: ")
            telefono = input("Telefono: ")
            correo = input("Correo: ")
            
            try:
                cliente = Cliente(identificacion, nombre, telefono, correo)
                resultado = sistema.registrar_cliente(cliente)
            except (ValueError, TypeError, ClienteDuplicadoError) as error:
                print("Error:", error)
            else:
                print(resultado)
                print("Cliente registrado sin errores.")
            finally:
                print("Proceso de registro finalizado.")
        elif opcion =="2":
            identificacion = input("Identificacion del cliente: ")
            try:
                cliente = sistema.buscar_cliente(identificacion)
                print("Cliente encontrado:", cliente.nombre)
                print("Telefono:", cliente.telefono)
                print("Correo:", cliente.correo)
            except ClienteNoEncontradoError as error:
                print("Error:", error)
        elif opcion =="3":
            clientes = sistema.listar_clientes()

            if clientes:
                for cliente in clientes:
                    print("----------------------")
                    print("Identificacion:", cliente.identificacion)
                    print("Nombre:", cliente.nombre)
                    print("Telefono:", cliente.telefono)
                    print("Correo:", cliente.correo)
            else:
                print("No hay clientes registrados.")
        elif opcion == "4":
            break
        else:
            print("Opcion no válida.")



def gestionar_servicios():
    while True:
        print("\n===== GESTIONAR SERVICIOS =====")
        print("1. Registrar servicio")
        print("2. Buscar servicio")
        print("3. Listar servicio")
        print("4. Vovler al menú principal")

        opcion = input("Seleccione una opcion: ").strip()
        if opcion == "1":
             print("\n=== TIPO DE SERVICIO ===")
             print("1. Sala de reuniones")
             print("2. Alquiler de equipos")
             print("3. Asesoría especializada")

             tipo = input("Seleccione el tipo: ").strip()
             nombre = input("Nombre del servicio: ")
             precio = input("Precio base: ")
             try:
                 precio = float(precio)

                 if tipo == "1":
                     servicio = ServicioSala(nombre, precio)
                 elif tipo == "2":
                     servicio = ServicioEquipo(nombre, precio)
                 elif tipo == "3":
                     servicio = ServicioAsesoria(nombre, precio)
                 else:
                     raise ValueError("Tipo de servicio no válido.")
                 resultado = sistema.registrar_servicio(servicio)
             except (ValueError, TypeError, ServicioDuplicadoError) as error:
                 print("Error:", error)
             else:
                 print(resultado)
                 print("Servicio registrado sin errores.")
             finally:
                 print("Proceso de registro finalizado.")
        elif opcion == "2":
            nombre = input("Nombre del servicio que desea buscar: ")

            try:
                servicio = sistema.buscar_servicio(nombre)
                print(servicio.describir_servicio())
            except (ServicioNoEncontradoError, ValueError, TypeError) as error:
                print("Error:", error)

        elif opcion == "3":
            servicios = sistema.listar_servicios()
            if servicios:
                for servicio in servicios:
                    print("----------------")
                    print("Nombre:", servicio.nombre)
                    print("Precio Base:", servicio.precio_base)
            else:
                print("No hay servicios registrados.")
        elif opcion =="4":
            break

        else:
            print("Opcion no válida.")

def gestionar_reservas():
    while True:
        print("\n======== GESTIONAR RESERVAS =======")
        print("1. Registrar reserva")
        print("2. Buscar reserva")
        print("3. Listar reserva")
        print("4. Confirmar reserva")
        print("5. Cancelar reserva")
        print("6. Vovler al menú principal")
        opcion = input("Seleccione una opcion: ")

        #Registrar Reserva
        if opcion == "1":
            try:
                identificacion = input("Identificacion del cliente: ")
                cliente = sistema.buscar_cliente(identificacion)

                nombre_servicio = input("Nombre del servicio: ")
                servicio = sistema.buscar_servicio(nombre_servicio)

                unidades = float(input("Ingrese las horas o días: "))

                reserva = Reserva(cliente, servicio, unidades)
                resultado = sistema.registrar_reserva(reserva)

            except (
                ValueError, TypeError, ClienteNoRegistradoError, 
                ServicioNoRegistradoError, ClienteNoEncontradoError,
                ServicioNoEncontradoError) as error:
                print(f"Error al registrar la reserva: {error}")
            except Exception as error:
                print(f"Ha ocurrido un error inesperado: {error}")

            else:
                print(resultado)
                print(f"Codigo de reserva: {reserva.codigo}")
                print(f"Costo total: ${reserva.costo_total}")
                print("Reserva registrada sin errores.")

            finally:
                print("Proceso de registro finalizado.")
        elif opcion == "2":
            try:
                codigo = int(input("Codigo de la reserva: "))
                reserva = sistema.buscar_reserva(codigo)

                print("\n==== INFORMACION DE LA RESERVA ====")
                print(f"Código: {reserva.codigo}")
                print(f"Cliente: {reserva.cliente.nombre}")
                print(f"Servicio: {reserva.servicio.nombre}")
                print(f"Unidades: {reserva.unidades}")
                print(f"Costo total: ${reserva.costo_total}")
                print(f"Estado: {reserva.estado}")
            except (ValueError, TypeError, ReservaNoEncontradaError) as error:
                print(f"Error al buscar la reserva: {error}")
        
        elif opcion == "3":
            reservas = sistema.listar_reservas()
            if not reservas:
                print("No hay reservas registradas.")
            else:
                print("\n==== RESERVAS REGISTRADAS ====")
                for reserva in reservas:
                    print(f"Código: {reserva.codigo}")
                    print(f"Cliente: {reserva.cliente.nombre}")
                    print(f"Servicio: {reserva.servicio.nombre}")
                    print(f"Unidades {reserva.unidades}")
                    print(f"Costo: ${reserva.costo_total}")
                    print(f"Estado: {reserva.estado}")
        #Confirmar reserva
        elif opcion == "4":
            try:
                codigo = int(input("Código de la reserva: "))
                reserva = sistema.buscar_reserva(codigo)
                print(reserva.confirmar())
            except ReservaYaCanceladaError as error:
                print(f"Error: {error}")
            except (ValueError, TypeError, ReservaNoEncontradaError) as error:
                print(f"Error al confirmar la reserva: {error}")

        #Cancelar reserva
        elif opcion == "5":
            try: 
                codigo = int(input("Código de la reserva: "))
                reserva = sistema.buscar_reserva(codigo)
                print(reserva.cancelar())
            except (ValueError, TypeError, ReservaNoEncontradaError, ReservaYaCanceladaError) as error:
                print(f"Error al cancelar la reserva: {error}")
        elif opcion == "6":
            break
        else:
            print("Opcion no válida.")
        

                                    

    

def mostrar_menu():
    print("\n======== SOFTWARE FJ =======")
    print("1. Gestionar clientes")
    print("2. Gestionar servicios")
    print("3. Gestionar reservas")
    print("4. Salir")
    print("==========================")


while True:
    mostrar_menu()
    opcion = input("Seleccione una opcion: ").strip()
    if opcion =="1":
        gestionar_clientes()
    elif opcion == "2":
        gestionar_servicios()
    elif opcion == "3":
        gestionar_reservas()
    elif opcion =="4":
        print("Gracias por utilizar Software FJ.")
        break
    else:
        print("Opción no válida, Intente nuevamente.")

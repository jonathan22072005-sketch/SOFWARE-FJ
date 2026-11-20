from cliente import Cliente
from sistema import Sistema
from servicio import ServicioSala, ServicioEquipo, ServicioAsesoria
from reserva import Reserva
from excepciones import (ReservaNoEncontradaError, ClienteNoEncontradoError, ServicioNoEncontradoError, ReservaYaCanceladaError, ClienteDuplicadoError, ServicioDuplicadoError, ClienteNoRegistradoError, ServicioNoRegistradoError)



sistema = Sistema()

cliente1=Cliente("123456", "Carlos", "30012345", "carlos@gmail.com")
cliente2=Cliente("123456", "Andres", "3227230696", "andres@gmail.com")


#registrar clientes
print("=== REGISTRO DE CLIENTES ===")

try:
    print(sistema.registrar_cliente(cliente1))
    print(sistema.registrar_cliente(cliente2))
except ClienteDuplicadoError as error:
    print("Error:", error)
else:
   print("Los clientes se registraron correctamente")
finally:
   print("Finalizó el proceso de registro de clientes")

    

#CONSULTAR TOTAL DE CLIENTES
print("\n=== TOTAL DE CLIENTES ===")
print("Clientes registrados:", len(sistema.clientes))


#buscar clientes
print("\n==BUSQUEDA DE CLIENTES ===")
try:
   resultado = sistema.buscar_cliente("123456")
   print("Cliente encontrado:", resultado.nombre)
except ClienteNoEncontradoError as error:
   print("Error;", error)


#BUSCAR CLIENTE INEXISTENTE
print("\n=== PRUEBA DE CLIENTE INEXISTENTE ===")
try:
   resultado = sistema.buscar_cliente("999999")
   print("Resultado:", resultado)
except ClienteNoEncontradoError as error:
   print("Error:", error)


#LISTAR TODOS LOS CLIENTES
print("\n=== LISTA DE CLIENTES ===")
clientes = sistema.listar_clientes()
if clientes:
   for cliente in clientes:
      print("------------------------")
      print("Identificacion:", cliente.identificacion)
      print("Nombre:", cliente.nombre)
      print("Telefono:", cliente.telefono)
      print("Correo:", cliente.correo)
else:
   print("No hay clientes registrados")


#REGISTRO DE SERVICIOS
print("\n=== REGISTRO DE SERVICIOS ===")

sala = ServicioSala("Sala de reuniones", 50000)
equipo = ServicioEquipo("Alquiler de computador", 40000)
asesoria = ServicioAsesoria("Asesoria informatica", 60000)

try:
    print(sistema.registrar_servicio(sala))
    print(sistema.registrar_servicio(equipo))
    print(sistema.registrar_servicio(asesoria))

except (ValueError, TypeError) as error:
   print("Error:", error)


#PRUEBA DE SERVICIO DIPLICADO
print("\n=== PRUEBA DE SERVICIO DUPLICADO ===")
servicio_repetido = ServicioSala("Sala de reuniones", 50000)
try:
   sistema.registrar_servicio(servicio_repetido)
except ServicioDuplicadoError as error:
   print("Error:", error)



#PRUEBA DE SERVICIO INEXISTENTE
print("\n=== PRUEBA DE SERVICIO INEXISTENTE ===")
try:
   sistema.buscar_servicio("Servicio inexistente")
except ServicioNoEncontradoError as error:
   print("Error:", error)


#BUSCAR SERVICIO
print("\n=== BUSCAR SERVICIO ===")

try:
   resultado = sistema.buscar_servicio("sala de reuniones")
   print("Servicio encontrado:", resultado.nombre)
   print("Precio base:", resultado.precio_base)
except ServicioNoEncontradoError as error:
   print("Error:", error)




#LISTAR SERVICIOS
print("\n === LISTAR DE SERVICIOS ===")

for servicio in sistema.listar_servicios():
   
   print("_________________________")
   print("Nombre:", servicio.nombre)
   print("Precio base:", servicio.precio_base)


#CREAR RESERVA
print("\n=== CREAR RESERVA ===")
reserva1 = Reserva(cliente1, sala, 3)

print("Cliente:", reserva1.cliente.nombre)
print("Servicio:", reserva1.servicio.nombre)
print("Unidades:", reserva1.unidades)
print("Costo total:", reserva1.costo_total)
print("Estado:", reserva1.estado)

#REGISTRAR RESERVA
print("\n=== REGISTRAR RESERVA ===")
try:
   print(sistema.registrar_reserva(reserva1))
except (ValueError, TypeError) as error:
   print("Error:", error)


#CONFIRMAR RESERVA
print("\n=== CONFIRMAR RESERVA ===")
try:
   print(reserva1.confirmar())
   print("Estado actual:", reserva1.estado)
except (ValueError, ReservaYaCanceladaError) as error:
   print("Error:", error)

try:
   reserva1.cliente = cliente2
except ValueError as error:
   print(error)

try:
   reserva1.unidades = 5
except ValueError as error:
   print(error)

try:
   reserva1.servicio = equipo
except ValueError as error:
   print(error)


#PRUEBA DE CONFIRMACION DUPLICADA
print("\n=== PRUEBA DE CONFIRMACION DUPLICADA ===")
try:
   reserva1.confirmar()
except ValueError as error:
   print("Error:", error)

#PRUEBA DE RESERVA DUPLICADA
print("\n=== PRUEBA DE RESERVA DUPLICADA ===")
try:
   sistema.registrar_reserva(reserva1)
except ValueError as error:
   print("Error:", error)

print("\n=== PRUEBA DE CLIENTE NO REGISTRADO ===")

cliente_externo = Cliente("987654", "PEdro", "3001234567", "pedro@gmail.com")
reserva_invalida = Reserva(cliente_externo, sala, 2)
try:
   sistema.registrar_reserva(reserva_invalida)
except ClienteNoRegistradoError as error:
   print("Error:", error)



#PRUEBA DE SERVICIO NO REGISTRADO
print("\n=== PRUEBA DE SERVICIO NO REGISTRADO ===")
servicio_externo = ServicioSala("Sala externa", 70000)
reserva_invalida2 = Reserva(cliente1, servicio_externo, 2)
try:
   sistema.registrar_reserva(reserva_invalida2)
except ServicioNoRegistradoError as error:
   print("Error:", error)



#PRUEBA DE CLIENTE INEXISTENTE
print("\n=== PRUEBA DE CLIENTE INEXISTENTE ===")
try:
   cliente_encontrado = sistema.buscar_cliente("999999")
   print("Resultado:", cliente_encontrado)
except ClienteNoEncontradoError as error:
   print("Error:", error)



#CANCELAR RESERVA
print("\n=== CANCELAR RESERVA ===")
print(reserva1.cancelar())
print("Estado actual:", reserva1.estado)

#SEGUNDA CANCELACION
print("\n=== SEGUNDA CANCELACION")

try:
   print(reserva1.cancelar())
except ReservaYaCanceladaError as error:
   print("Error:", error)

#CONFIRMAR RESERVA CANCELADA
print("\n=== CONFIRMAR RESERVA CANCELADA ===")
try:
   reserva1.confirmar()
except ReservaYaCanceladaError as error:
   print("Error:", error)

try:
   reserva1.unidades = 5
except ValueError as error:
   print(error)



#BUSCAR RESERVA
print("\n=== BUSCAR RESERVA ===")

try:
   reserva_encontrada = sistema.buscar_reserva(reserva1.codigo)
   print("Reserva encontrada")
   print("Codigo:", reserva_encontrada.codigo)
   print("Cliente:", reserva_encontrada.cliente.nombre)
   print("Servicio:", reserva_encontrada.servicio.nombre)
except ReservaNoEncontradaError as error:
   print("Error:", error)


#PRUEBA DE RESERVA INEXISTENTE
print("\n=== PRUEBA DE RESERVA INEXISTENTE ===")
try:
   sistema.buscar_reserva(999)
except ReservaNoEncontradaError as error:
   print("Error:", error)


#LISTAR RESERVAS
print("\n=== LISTAR DE RESERVAS ===")
for reserva in sistema.listar_reservas():
   print("----------------------")
   print("Codigo:", reserva.codigo)
   print("Cliente:", reserva.cliente.nombre)
   print("Servicio:", reserva.servicio.nombre)
   print("Unidades:", reserva.unidades)
   print("Costo:", reserva.costo_total)
   print("Estado:", reserva.estado)
   
print("\n=== PRUEBA DE ENCADENAMIENTO DE EXCEPCIONES ===")
try:
   try:
      precio = int("Hola")
   except ValueError as error:
      raise RuntimeError("No se pudo procesar el precio") from error
except RuntimeError as error:
   print("Error:", error)
   print("Causa original:", error.__cause__)

from servicio import ServicioSala, ServicioEquipo, ServicioAsesoria
sala = ServicioSala("Sala de reuniones", 50000)
equipo = ServicioEquipo("Computador", 30000)
Asesoria = ServicioAsesoria("Asesoria tecnica", 80000)

print("Sala:", sala.calcular_costo(3, 10, 19))
print("Equipo:", equipo.calcular_costo(2, 5, 19))
print("Asesoria:", asesoria.calcular_costo(2))


print(ServicioSala.__mro__)
print(hasattr(sala, "validar_parametros"))


#PRUEBA DE VALIDAR PARAMETROS
print("\n=== PRUEBA DE VALIDAR PARAMETROS ===")
print(sala.validar_parametros(3))
try:
   sala.validar_parametros("hola")
except TypeError as error:
   print("Error:",error)
try:
   sala.validar_parametros(0)
except ValueError as error:
   print("Error:", error)

print("\n === DESCRIPCION DEL SERVICIO ===")
print(sala.describir_servicio())

try:
   sala.validar_porcentajes("10", 19)
except TypeError as error:
   print("Error:", error)

try:
   sala.validar_porcentajes(10, 150)
except ValueError as error:
   print("Error:", error)

try:
   sala.validar_porcentajes(True, 19)
except TypeError as error:
   print("Error:", error)


#PRUEBA DE UNIDADES EN RESERVA
print("\n=== PRUEBA DE UNIDADES EN RESERVA ===")
try:
   Reserva(cliente1, sala, "tres")
except TypeError as error:
   print("Error:", error)

try:
   Reserva(cliente1, sala, 0)
except ValueError as error:
   print("Error:", error)

try:
   Reserva(cliente1, sala, True)
except TypeError as error:
   print("Error:", error)
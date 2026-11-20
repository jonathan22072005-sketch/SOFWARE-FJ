from cliente import Cliente
from servicio import Servicio
from reserva import Reserva
from excepciones import (
   ClienteDuplicadoError, 
   ServicioDuplicadoError, 
   ClienteNoRegistradoError, 
   ServicioNoRegistradoError, 
   ClienteNoEncontradoError, 
   ServicioNoEncontradoError, 
   ReservaNoEncontradaError,
   ReservaDuplicadaError)
from registro import logger  



class Sistema:
    def __init__(self):
        self.clientes = []
        self.servicios = []
        self.reservas = []

#registrar clientes
    def registrar_cliente(self, cliente):
        if not isinstance(cliente, Cliente):
           logger.warning("Intento de registrar un objeto que no es un cliente")
           raise TypeError("El objeto debe ser un cliente")
        
        for cliente_registrado in self.clientes:
           if cliente_registrado.identificacion == cliente.identificacion:
            logger.warning(f"Intento de registrar cliente duplicado: {cliente.identificacion}")
            raise ClienteDuplicadoError("ya existe un cliente con esa identificacion")
           
        self.clientes.append(cliente)
        logger.info(f"Cliente registrado: {cliente.identificacion}")
        return "cliente registrado correctamente"

#BUSCAR CLIENTES
    def buscar_cliente(self, identificacion):
     for cliente in self.clientes:
        if cliente.identificacion == identificacion:
            return cliente
     logger.warning(f"Intento de busqueda de cliente inexistente: {identificacion}")
     raise ClienteNoEncontradoError("No se encontró un cliente con esa identificacion")


#listar clientes
    def listar_clientes(self):
       return self.clientes.copy()

    
#registrar servicio
    def registrar_servicio(self, servicio):
       if not isinstance(servicio, Servicio):
          logger.warning("Intento de registrar un objeto que no es un servicio")
          raise TypeError("El objeto debe ser un servicio")

       for servicio_registrado in self.servicios:
          if servicio_registrado.nombre.lower() == servicio.nombre.lower():
             logger.warning(f"Intento de registrar servicio duplicado: {servicio.nombre}")
             raise ServicioDuplicadoError("Ya existe un servicio con ese nombre")

       self.servicios.append(servicio)
       logger.info(f"Servicio registrado: {servicio.nombre}")
       return "Servicio registrado correctamente"


#BUSCAR SERVICIO
    def buscar_servicio(self, nombre):
       if not isinstance(nombre, str):
          logger.warning(f"Intento de busqueda con nombre de servicio invalido: {nombre}")
          raise TypeError("El nombre del servicio debe ser texto")
       if not nombre.strip():
          logger.warning("Intento de busqueda con nombre de servicio")
          raise ValueError("El nombre del servicio no puede estar vacio")
       for servicio in self.servicios:
          if servicio.nombre.lower() == nombre.strip().lower():
             return servicio
       logger.warning(f"Intento de busqueda de servicio inexistente: {nombre}")
       raise ServicioNoEncontradoError("No se encontró un servicio con ese nombre")


#listar servicios
    def listar_servicios(self):
       return self.servicios.copy()
    
#registrar reservas
    def registrar_reserva(self, reserva):
       if not isinstance(reserva, Reserva):
         logger.warning("Intento de registrar un objeto que no es una reserva")
         raise TypeError("El objeto debe ser una reserva")

       #Verificar estado de la reserva
       if reserva.estado != "Pendiente":
          logger.warning(f"Intento de registrar una reserva que no está pendiente: {reserva.codigo}")
          raise ValueError ("Solo se pueden registrar reservas pendientes")

       #verificar reservas duplicadas
       for reserva_registrada in self.reservas:
          if reserva_registrada.codigo == reserva.codigo:
              logger.warning(f"Intento de registrar una reserva con codigo repetido: {reserva.codigo}")
              raise ReservaDuplicadaError("La reserva ya está registrada")
          if (reserva_registrada.cliente.identificacion == reserva.cliente.identificacion
              and reserva_registrada.servicio.nombre ==
              reserva.servicio.nombre
              and reserva_registrada.unidades == reserva.unidades
              and reserva_registrada.estado != "Cancelada"):
              logger.warning("Intento de registrar una reserva duplicada")
              raise ReservaDuplicadaError("El cliente ya tiene una reserva activa para este servicio y cantidad")
       
         
      #Verificar cliente
       if reserva.cliente not in self.clientes:
          logger.warning(f"Intento de reserva con cliente no registrado: "
                         f"{reserva.cliente.identificacion}")
          raise ClienteNoRegistradoError("El cliente no esta registrado en el sistema")

      #Verificar servicio
       if reserva.servicio not in self.servicios:
         logger.warning(f"Intento de reserva con servicio no registrado: "
                        f"{reserva.servicio.nombre}")
         raise ServicioNoRegistradoError("El servicio no esta registrado en el sistema")

      #Registrar reserva
       self.reservas.append(reserva)
       logger.info(f"Reserva registrada: codigo {reserva.codigo}, "
                   f"cliente {reserva.cliente.identificacion}, "
                   f"servicio {reserva.servicio.nombre}")
       return "Reserva registrada correctamente"
    

#listar reserva
    def listar_reservas(self):
       return self.reservas.copy()

#Buscar reserva
    def buscar_reserva(self, codigo):
       if isinstance(codigo, bool) or not isinstance(codigo, int):
          logger.warning(f"Intento de busqueda con codigo de reserva inválido: {codigo}")
          raise TypeError("El codigo debe ser un numero entero")

       if codigo <= 0:
          logger.warning(f"Intento de busqueda con codigo no valido: {codigo}")
          raise ValueError("El codigo debe ser mayor que cero")

       for reserva in self.reservas:
          if reserva.codigo == codigo:
             return reserva
       logger.warning(f"Intento de busqueda de reserva inexistente: {codigo}")
       raise ReservaNoEncontradaError("No se encontró una reserva con ese codigo")
      
       
       

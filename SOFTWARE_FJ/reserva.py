from cliente import Cliente
from servicio import Servicio
from excepciones import ReservaYaCanceladaError
from registro import logger


class Reserva:
    contador = 1
    def __init__(self, cliente, servicio, unidades):
        self.__estado = "Pendiente"
        self.cliente = cliente
        self.servicio = servicio
        self.unidades = unidades

        self.__codigo = Reserva.contador
        Reserva.contador += 1

#CODIGO DE RESERVA
    @property
    def codigo(self):
        return self.__codigo


#CLIENTE
    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, nuevo_cliente):
        if self.__estado != "Pendiente":
            raise ValueError("No se puede modificar una reserva que ya no está pendiente")
        if not isinstance(nuevo_cliente, Cliente):
            raise TypeError("La reserva debe tener un cliente válido")
        self.__cliente = nuevo_cliente


#SERVICIO
    @property
    def servicio(self):
        return self.__servicio

    @servicio.setter
    def servicio(self, nuevo_servicio):
        if self.__estado != "Pendiente":
            raise ValueError("No se puede modificar una reserva que ya no esta pendiente")
        if not isinstance(nuevo_servicio, Servicio):
            raise TypeError("La reserva debe tener un servicio válido")
        self.__servicio = nuevo_servicio



#UNIDADES
    @property
    def unidades(self):
        return self.__unidades

    @unidades.setter
    def unidades(self, nuevas_unidades):
        if self.__estado != "Pendiente":
            raise ValueError("No se puede modificar una reserva que ya no esta pendiente")
        if isinstance(nuevas_unidades, bool) or not isinstance(nuevas_unidades, (int, float)):
            raise TypeError("Las unidades deben ser un número")

        if nuevas_unidades <= 0:
            raise ValueError("Las unidades deben ser mayores que cero")

        self.__unidades = nuevas_unidades



#COSTO TOTAL
    @property
    def costo_total(self):
        return self.servicio.calcular_costo(self.unidades)


#ESTADO
    @property
    def estado(self):
        return self.__estado

#CONFIRMAR RESERVA
    def confirmar(self):
        if self.__estado == "Cancelada":
            logger.warning(f"Intento de confirmar una reserva cancelada: {self.__codigo}")
            raise ReservaYaCanceladaError("No se puede confirmar una reserva cancelada")
        if self.__estado == "Confirmada":
            raise ValueError("La reserva ya esta confirmada")
        self.__estado = "Confirmada"
        logger.info(f"Reserva confirmada: codigo {self.__codigo}")
        return "Reserva confirmada correctamente"


#CANCELAR RESERVA
    def cancelar(self):
        if self.__estado == "Cancelada":
            logger.warning(f"Intento de cancelar una reserva ya cancelada: {self.__codigo}")            
            raise ReservaYaCanceladaError("La reserva ya está cancelada")
        
        self.__estado = "Cancelada"
        logger.info(f"Reserva cancelada: codigo {self.__codigo}")
        return "Reserva cancelada correctamente"

    



from abc import ABC, abstractmethod

class Servicio(ABC):
    def __init__(self, nombre, precio_base):
        self.nombre = nombre
        self.precio_base = precio_base

    #PROPIEDAD NOMBRE
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if not isinstance(nuevo_nombre, str):
            raise TypeError("El nombre del servicio debe ser texto")
        if not nuevo_nombre.strip():
            raise ValueError("El nombre del servicio no puede estar vacio")
        self.__nombre = nuevo_nombre.strip()


    #PROPIEDAD PRECIO BASE
    @property
    def precio_base(self):
        return self.__precio_base  
    @precio_base.setter
    def precio_base(self, nuevo_precio):
        if isinstance(nuevo_precio, bool) or not isinstance (nuevo_precio, (int, float)):
            raise TypeError("El precio base debe ser un numero")
        if nuevo_precio <= 0:
            raise ValueError("El precio debe ser mayor que cero") 
        self.__precio_base = nuevo_precio


    #METODO ABSTRACTO
    @abstractmethod
    def calcular_costo(self, unidades, descuento=0, impuesto=0):
        pass

    def describir_servicio(self):
        return (f"Servicio: {self.nombre}\n"
                f"Precio base: ${self.precio_base}")
        
    def validar_parametros(self, unidades):
            if isinstance(unidades, bool) or not isinstance(unidades, (int, float)):
               raise TypeError("Las unidades deben ser un numero")
            if unidades <= 0:
               raise ValueError("Las unidades deben ser mayores que cero")
            return True 
    def validar_porcentajes(self, descuento, impuesto):
        if isinstance(descuento, bool) or not isinstance(descuento, (int, float)):
            raise TypeError("El descuento debe ser un numero")
        if isinstance(impuesto, bool) or not isinstance(impuesto, (int, float)):
            raise TypeError("El impuesto debe ser un numero")
        if not 0 <= descuento <= 100:
            raise ValueError("El descuento debe estar entre 0 y 100")
        if not 0 <= impuesto <= 100:
            raise ValueError("El impuesto debe estar entre 0 y 100")
        return True




class ServicioSala(Servicio):

    def __init__(self, nombre, precio_base):
        super().__init__(nombre, precio_base)

    def calcular_costo(self, horas, descuento=0, impuesto=0):
        self.validar_parametros(horas)
        self.validar_porcentajes(descuento, impuesto)

        subtotal = self.precio_base * horas
        total_descuento = subtotal * (descuento / 100)
        subtotal_con_descuento = subtotal - total_descuento
        total_impuesto = subtotal_con_descuento * (impuesto / 100)

        return subtotal_con_descuento + total_impuesto

class ServicioEquipo(Servicio):

    def __init__(self, nombre, precio_base):
        super().__init__(nombre, precio_base)
        
    def calcular_costo(self, dias, descuento=0, impuesto=0):
        self.validar_parametros(dias)
        self.validar_porcentajes(descuento, impuesto)

        subtotal = self.precio_base * dias
        total_descuento = subtotal * (descuento / 100)
        subtotal_con_descuento = subtotal - total_descuento
        total_impuesto = subtotal_con_descuento * (impuesto / 100)
        return subtotal_con_descuento + total_impuesto

        


class ServicioAsesoria(Servicio):
    def __init__(self, nombre, precio_base):
        super().__init__(nombre, precio_base)

    def calcular_costo(self, horas, descuento=0, impuesto=0):
        self.validar_parametros(horas)
        self.validar_porcentajes(descuento, impuesto)

        subtotal = self.precio_base * horas
        total_descuento = subtotal * (descuento / 100)
        subtotal_con_descuento = subtotal - total_descuento
        total_impuesto = subtotal_con_descuento * (impuesto / 100)
        return subtotal_con_descuento + total_impuesto
    
    


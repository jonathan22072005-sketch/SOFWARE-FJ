class Cliente:
    def __init__(self, identificacion, nombre, telefono, correo):
        self.identificacion = identificacion
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo


    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if not isinstance(nuevo_nombre, str):
            raise TypeError("El nombre debe ser texto")
        nuevo_nombre = nuevo_nombre.strip()
        if not nuevo_nombre:
            raise ValueError("El nombre no puede estar vacio")
        self.__nombre = nuevo_nombre

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, nuevo_telefono):
        if not isinstance(nuevo_telefono, str):
            raise TypeError("El telefono debe ser texto")
        nuevo_telefono = nuevo_telefono.strip()
        if not nuevo_telefono:
            raise ValueError("El telefono no puede estar vacio")
        if not nuevo_telefono.isdigit():
            raise ValueError("El telefono solo debe contener numeros")
        if len(nuevo_telefono) < 7 or len (nuevo_telefono) > 15:
            raise ValueError("El telefono debe tener entre 7 y 15 digitos")
        self.__telefono = nuevo_telefono
    
    @property
    def identificacion(self):
        return self.__identificacion

    @identificacion.setter
    def identificacion(self, nueva_identificacion):
        if not isinstance(nueva_identificacion,str):
            raise TypeError("La identificacion debe ser texto")

        nueva_identificacion=nueva_identificacion.strip()

        if not nueva_identificacion.isdigit():
            raise ValueError("la identificacion solo debe contener numeros")

        if len (nueva_identificacion) < 5 or len (nueva_identificacion) > 15:
            raise ValueError("la identificacion debe tener entre 5 y 15 digitos")
        self.__identificacion = nueva_identificacion

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, nuevo_correo):
        if not isinstance(nuevo_correo, str):
            raise TypeError("El correo debe ser texto")
        
        nuevo_correo=nuevo_correo.strip()

        if not nuevo_correo:
            raise ValueError("El correo no puede estar vacio")
        if "@" not in nuevo_correo or "." not in nuevo_correo:
            raise ValueError("El correo no tiene un formato valido")
        if " " in nuevo_correo:
            raise ValueError("El correo no debe contener espacios")
        
        self.__correo = nuevo_correo

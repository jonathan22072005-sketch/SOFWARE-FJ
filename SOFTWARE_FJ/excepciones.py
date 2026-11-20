class ClienteDuplicadoError(ValueError):
  pass

class ClienteNoEncontradoError(LookupError):
  pass


class ServicioDuplicadoError(ValueError):
  pass

class ServicioNoEncontradoError(LookupError):
  pass


class ReservaNoEncontradaError(LookupError):
  pass

class ReservaYaCanceladaError(ValueError):
  pass

class ClienteNoRegistradoError(ValueError):
  pass

class ServicioNoRegistradoError(ValueError):
  pass

class ReservaDuplicadaError(ValueError):
  pass
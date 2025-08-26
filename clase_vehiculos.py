class Vehiculo:
    """Clase de vehiculos"""
    def __init__(self,dominio,tipo):
        self.dominio=dominio
        self.tipo=tipo
        # print(f"Vehiculo creado: {tipo.upper()} - {dominio}")
        pass

    def get_dominio(self):
        return self.dominio
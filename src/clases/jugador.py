class Jugador: 
    
    def __init__(self, carnet, nombre, apellido, nivel):
        
        self.carnet = carnet
        self.nombre = nombre
        self.apellido = apellido
        self.nivel = nivel
        self.intentos = []
        
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"
    
    def agregar_intento(self, intento):
        self.intentos.append(intento)
        
        
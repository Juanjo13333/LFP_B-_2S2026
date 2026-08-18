import os
from clases.tablero import Tablero
from clases.jugador import Jugador
from clases.intento import Intento



class GestorTorneo:
    
    def __init__(self):
        
        self.tableros = {}
        self.jugadores = {}
        self.intentos = []
        
        
    def cargar_sudokus(self, ruta_archivo):
        if not os.path.exists(ruta_archivo):
            raise FileNotFoundError(f"El archivo {ruta_archivo} no fue encontrado")
        
        
        registros_cargados = 0
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                
                if not linea:
                    continue
                
                partes = linea.split(",")
                if len(partes) == 3:
                    
                    
                    try:
                        
                        id_sudoku = int(partes[0].strip())
                        dificultad = partes [1].strip()
                        tablero_str = partes[2].strip()
                        
                        tablero = Tablero(id_sudoku, dificultad, tablero_str)
                        self.tableros[id_sudoku] = tablero
                        registros_cargados +=1
                    
                    
                    except ValueError as e:
                        print(f"formato invalido {linea} -> {e}")
        
        return registros_cargados
    
    
    def cargar_jugadores(self, ruta_archivo):
        
        
        if not os.path.exists(ruta_archivo):
            raise FileNotFoundError(f"el archivo {ruta_archivo} no fue encontrado")
        
        
        registros_cargados = 0 
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if not linea:
                    continue
                
                partes = linea.split(",")
                if len(partes) == 4:
                    
                    
                    try:
                        
                        
                        carnet = int(partes[0].strip())
                        nombre = partes[1].strip()
                        apellido = partes[2].strip()
                        nivel = partes[3].strip()
                        
                        
                        jugador = Jugador(carnet, nombre, apellido, nivel)
                        self.jugadores[carnet] = jugador
                        registros_cargados += 1
                    
                    except ValueError:
                        
                        print(f"jugador invalido {linea}")
                        
        return registros_cargados
    
    
    
    def cargar_intentos(self, ruta_archivo):
        
        if not os.path.exists(ruta_archivo):
            raise FileNotFoundError(f"El archivo {ruta_archivo} no fue encontrado")
        
        
        registros_cargados = 0
        
        with open(ruta_archivo, "r", encoding = "utf-8") as arcihvo:
            for linea in arcihvo:
                linea = linea.strip()
                if not linea:
                    continue
                
                partes = linea.split(",")
                if len(partes) == 5:
                    
                    
                    try:
                        carnet = int(partes[0].strip())
                        id_sudoku = int(partes[1].strip())
                        solucion_str = partes[2].strip()
                        tiempo_segundos = int(partes[3].strip())
                        fecha = partes[4].strip()
                        
                        intento = Intento(carnet,id_sudoku,solucion_str,tiempo_segundos,fecha)
                        self.intentos.append(intento)
                        
                        if carnet in self.jugadores:
                            self.jugadores[carnet].agregar_intento(intento)
                        
                        registros_cargados += 1
                        
                    except ValueError as e:
                        print(f"formato invalido {linea} = {e}")
                        
        return registros_cargados       
    
    
    
    def calificar_todos_los_intentos(self):
        if not self.intentos:
            print("Aún no hay ningun intento")
            return 0
        
        intentos_calificados = 0
        for intento in self.intentos:
            if intento.id_sudoku in self.tableros:
                tablero_original = self.tableros[intento.id_sudoku]
                intento.calificar(tablero_original)
                intentos_calificados += 1
            
            else: 
                print(f"No se encontro el tablero con ID {intento.id_sudoku} "
                    f"para el intento del jugador con carnet {intento.carnet}")
                
        
        return intentos_calificados
                    
                        
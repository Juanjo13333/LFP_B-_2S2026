class Tablero:
    
    def __init__(self, id_sudoku, dificultad, tablero_str):
        # 1. Validar que la cadena tenga exactamente 81 caracteres
        if len(tablero_str) != 81:
            raise ValueError(
                f"El tablero debe tener exactamente 81 caracteres (se recibieron {len(tablero_str)})."
            )
            
        self.id_sudoku = id_sudoku
        self.dificultad = dificultad
        self.tablero_str = tablero_str
        
        # 2. Generar matriz y extraer pistas
        self.matriz = self._string_a_matriz(tablero_str)
        self.pistas = self._extraer_pistas()
        
    def _string_a_matriz(self, cadena):
        matriz = []
        for i in range(9):
            fila = []
            for j in range(9):
                caracter = cadena[i * 9 + j]
                val = int(caracter) if caracter.isdigit() else 0
                fila.append(val)
            matriz.append(fila)
        return matriz
    
    def _extraer_pistas(self):
        pistas = {}
        for i in range(9):
            for j in range(9):
                if self.matriz[i][j] != 0:
                    pistas[(i, j)] = self.matriz[i][j]
        return pistas
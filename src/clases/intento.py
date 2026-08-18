class Intento:

    def __init__(
        self, carnet, id_sudoku, solucion_str, tiempo_segundos, fecha
    ):
        self.carnet = carnet
        self.id_sudoku = id_sudoku
        self.solucion_str = solucion_str
        self.tiempo_segundos = tiempo_segundos
        self.fecha = fecha

        # Convierte la cadena recibida en la matriz 9x9 del intento
        self.matriz_solucion = self._string_a_matriz(solucion_str)
        self.porcentaje_validez = 0.0
        self.pistas_respetadas = False

    def _string_a_matriz(self, cadena):
        """Convierte una cadena de 81 caracteres en una matriz 9x9."""
        matriz = []
        for i in range(9):
            fila = []
            for j in range(9):
                caracter = cadena[i * 9 + j]
                val = int(caracter) if caracter.isdigit() else 0
                fila.append(val)
            matriz.append(fila)
        return matriz

    def calificar(self, tablero_original):
        """Califica el intento comparándolo con el tablero inicial y las reglas de Sudoku."""
        # 1. Verificar si respetó las pistas originales del tablero
        self.pistas_respetadas = self._verificar_pistas(tablero_original)

        # Si no respetó las pistas fijas, la validez es 0%
        if not self.pistas_respetadas:
            self.porcentaje_validez = 0.0
            return 0.0

        # 2. Contar estructuras válidas (filas, columnas, cajas de 3x3)
        filas_validas = self._validar_filas()
        cols_validas = self._validar_columnas()
        cajas_validas = self._validar_cajas()

        total_validos = filas_validas + cols_validas + cajas_validas

        # 3. Calcular porcentaje sobre las 27 estructuras (9 filas + 9 columnas + 9 cajas)
        self.porcentaje_validez = (total_validos / 27.0) * 100.0
        return self.porcentaje_validez

    def _verificar_pistas(self, tablero_original):
        # tablero_original.pistas es un diccionario {(fila, columna): valor}
        for (i, j), valor_original in tablero_original.pistas.items():
            if self.matriz_solucion[i][j] != valor_original:
                return False
        return True

    def _validar_filas(self):
        validas = 0
        for i in range(9):
            if set(self.matriz_solucion[i]) == set(range(1, 10)):
                validas += 1
        return validas

    def _validar_columnas(self):
        validas = 0
        for j in range(9):
            columna = [self.matriz_solucion[i][j] for i in range(9)]
            if set(columna) == set(range(1, 10)):
                validas += 1
        return validas

    def _validar_cajas(self):
        validas = 0
        for f in range(0, 9, 3):
            for c in range(0, 9, 3):
                caja = []
                for i in range(3):
                    for j in range(3):
                        caja.append(self.matriz_solucion[f + i][c + j])
                if set(caja) == set(range(1, 10)):
                    validas += 1
        return validas

    def resuelto_correctamente(self):   
        return self.porcentaje_validez == 100.0 and self.pistas_respetadas
            
        
          
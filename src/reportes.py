import os

class GeneradorReportes:
    
    
    def __init__(self, ruta_destino ="../reportes_html"):
        
        self.ruta_destino = ruta_destino
        
        if not os.path.exists(self.ruta_destino):
            os.makedirs(self.ruta_destino)
            
    def generar_reporte_ranking(self, jugadores):
        ruta_archivo = os.path.join(self.ruta_destino, "ranking.html")
        
        listas_jugadores = list(jugadores.values())
        
        def criterio_orden(j):
            if not j.intentos:
                return (-1, float("inf"))
            mejor_porcentaje = max(i.porcentaje_validez for i in j.intentos)
            menor_tiempo = min(
                i.tiempo_segundos
                for i in j.intentos
                if i.porcentaje_validez == mejor_porcentaje
            )
            return (mejor_porcentaje, -menor_tiempo)
        
        listas_jugadores.sort(key=criterio_orden, reverse=True)
        
        html = """<!DOCTYPE html>
<html lang = "es">        
<head>
    <meta charset ="UTF-8">
    <title>RANKING DE JUGADORES </title>
    <style>
        body { font-family: Arial, sans-serif; margin: 30px; background-color: #f4f4f9; }
        h1 { color: #333; text-align: center; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; background: #fff; }
        th, td { border: 1px solid #ddd; padding: 12px; text-align: center; }
        th { background-color: #2c3e50; color: white; }
        tr:nth-child(even) { background-color: #f2f2f2; }
    </style>
</head>
<body>
    <h1>Ranking General del Torneo lfp</h1>
    <table>
        <thead>
            <tr>
                <th>Posicion</th>
                <th>Carnet</th>
                <th>Nombre Completo</th>
                <th>Nivel</th>
                <th>Intentos totales</th>
                <th>Mejor validez %</th>
            </tr>
        </thead>
        <tbody>
""" 

        posicion = 1
        for j in listas_jugadores:
            if j.intentos:
                mejor_validez = max(i.porcentaje_validez for i in j.intentos)
                html += f""""           <tr>
                <td>{posicion}</td>
                <td>{j.carnet}</td>
                <td>{j.nombre_completo()}</td>
                <td>{len(j.intentos)}</td>
                <td>{mejor_validez:.2f}%</td>
            </tr>\n """
                posicion += 1
                
        html += """        </tbody>
    </table>
</body>
</html>
"""
        with open(ruta_archivo, "w", encoding="utf-8") as f:
            f.write(html)
            
        return ruta_archivo
    
    def generar_reporte_intentos(self, intentos, jugadores):
        ruta_archivo = os.path.join(self.ruta_destino, "historial_intentos.html")
        
        html = """"<!DOCTYPE html> 
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>HISTORIAL DE INTENTOS</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 30px; background-color: #f4f4f9; }
        h1 { color: #333; text-align: center; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; background: #fff; }
        th, td { border: 1px solid #ddd; padding: 10px; text-align: center; }
        th { background-color: #34495e; color: white; }
        tr:nth-child(even) { background-color: #f9f9f9; }
        .exito { color: green; font-weight: bold; }
        .fallo { color: red; font-weight: bold; }
    </style>
</head>
<body>
    <h1>Historial completo de intentos</h1>
    <table>
        <thead>
            <tr>
                <th>Fecha</th>
                <th>Carnet</th>
                <th>Jugador</th>
                <th>ID Sudoku</th>
                <th>Tiempo</th>
                <th>Validez</th>
                <th>Pistas Respetadas</th>
                <th>Estado</th>
            </tr>
        </thead>
        <tbody> 
"""
        for intento in intentos:
            nombre_jugador = (
                jugadores[intento.carnet].nombre_completo()
                if intento.carnet in jugadores 
                else "Desconocido"
            )         
            estado_clase =(
                "exito" if intento.resuelto_correctamente() else "fallo"
            )
            
            estado_texto = (
                "Resuelto"
                if intento.resuelto_correctamente()
                else "incorrecto"
            )
            
            
            html += f"""                <tr>
                <td>{intento.fecha}</td>
                <td>{intento.carnet}</td>
                <td>{nombre_jugador}</td>
                <td>{intento.id_sudoku}</td>
                <td>{intento.tiempo_segundos}</td>
                <td>{intento.porcentaje_validez:.2f}%</td>
                <td>{"SI" if intento.pistas_respetadas else "NO"}</td>
                <td class="{estado_clase}">{estado_texto}</td>
            </tr>\n"""
        
        html += """                  </tbody>
    </table>
</body>
</html>
"""

        with open(ruta_archivo, "w", encoding="utf-8") as f:
            f.write(html)
            
        
        return ruta_archivo
        
        
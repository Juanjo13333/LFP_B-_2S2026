import os 
from gestor import GestorTorneo
from reportes import GeneradorReportes


def mostrar_menu():
    print("\n----------------------------------")
    print("          SUDOKU USAC LFP           ")
    print("------------------------------------")
    print("1. Cargar Arcihvos .lfp")
    print("2. Calificar todos los intentos")
    print("3. Generar reportes HTML")
    print("4. salir")
    print("------------------------------------")
    
def main():
    
    gestor = GestorTorneo()
    generador_reportes = GeneradorReportes(ruta_destino="../reportes")
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()
        
        if opcion == "1":
            print("Carga de archivos .lfp")
            r_sudokus = (
                input("Ruta de sudokus.lfp").strip()
                or "../datos/sudokus.lfp"
            )
            
            r_jugadores =  (
                input("Ruta de jugadores.lfp").strip()
                or"../datos/jugadores.lfp"
            )
            
            r_intentos = (
                input("Ruta de intentos.lfp").strip()
                or"../datos/intentos.lfp"
            )
            
            try:
                c_sudokus = gestor.cargar_sudokus(r_sudokus)
                c_jugadores = gestor.cargar_jugadores(r_jugadores)
                c_intentos = gestor.cargar_intentos(r_intentos)
                
                print("Carga completa")
                print(f"    -sudokus cargados: {c_sudokus}")
                print(f"    -Jugadores Cargados: {c_jugadores}")
                print(f"    -Intentos cargados: {c_intentos}")
            except Exception as e:
                print(f"\n No es posible cargar: {e}")
                
        elif opcion == "2":
            print("\n------- Califiacion de intentos -------")
            if not gestor.intentos:
                print("Por favor primero ingrese los archivos (opcion 1)")
                continue
            total = gestor.calificar_todos_los_intentos()
            print(f"Se han calificado {total} intentos correctamente")
            
        elif opcion == "3":
            print("\n------- Generar Reportes HTML -------")
            if not gestor.intentos:
                print("Debe cargar y calificar algún dato para poder generar el archivo")
                continue
            
            try:
                
                r_ranking = generador_reportes.generar_reporte_ranking(gestor.jugadores)
                r_intentos = generador_reportes.generar_reporte_intentos(gestor.intentos, gestor.jugadores)
                
                print("Reportes generados exitosamente!")
                print(f"-{r_ranking}")
                print(f"-{r_intentos}")
            
            except Exception as e:
                print(f"Ocurrio un inconveniente al generar el HTML: {e}")
                
        
        elif opcion == "4":
            print("Gracias por usar el sudoku Usac LFP")
            break
        else: 
            print("Por favor digite una opcion válida")
            
if __name__ == "__main__":
    main()
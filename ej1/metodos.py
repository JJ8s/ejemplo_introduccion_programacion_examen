class agencia:
    def __init__(self):
    
        self.turistas = {
                "001": ["John Doe", "Estados Unidos", "12-01-2024"],
                "002": ["Emily Smith", "Estados Unidos", "23-03-2024"],
                "012": ["Julian Martinez", "Argentina", "19-09-2023"],
                "014": ["Agustin Morales", "Argentina", "28-03-2024"],
                "005": ["Carlos Garcia", "Mexico", "10-05-2024"],
                "006": ["Maria Lopez", "Mexico", "08-12-2023"],
                "007": ["Joao Silva", "Brasil", "20-06-2024"],
                "003": ["Michael Brown", "Estados Unidos", "05-07-2023"],
                "004": ["Jessica Davis", "Estados Unidos", "15-11-2024"],
                "008": ["Ana Santos", "Brasil", "03-10-2023"],
                "010": ["Martin Fernandez", "Argentina", "13-02-2023"],
                "011": ["Sofia Gomez", "Argentina", "07-04-2024"],
            }
        
    def turistas_por_pais(self, pais):
            encontrados = False
            print(f"Turistas de {pais}:")
            for datos in self.turistas.values():
                nombre = datos[0]
                pais_turista = datos[1]
                if pais_turista.lower() == pais.lower():
                    print(f" - {nombre}")
                    encontrados = True
            if not encontrados:
                print("No se encontraron turistas de ese país.")
    
    def turista_mes(self, mes):
        if mes.isdigit() and len(mes)==1:
            mes ="0"+mes
            total =len(self.turistas)
            if total==0:
                return 0.0
            conteo_mes=0
            for datos in self.turistas.values():
                fecha=datos[2]
                mes_turista=fecha.split("-")[1]
                if mes_turista==mes:
                    conteo_mes+=1
            porcentaje=(conteo_mes/total)*100
            return round(porcentaje, 1)
    def eliminar(self):
        while True:
            try:
                nombre_buscado = input("Ingrese nombre de la persona: ").strip().lower()
                id_encontrado = None

                for id_turista, datos in self.turistas.items():
                    nombre_actual = datos[0].strip().lower()
                    if nombre_actual == nombre_buscado:
                        id_encontrado = id_turista
                        break

                if id_encontrado:
                    del self.turistas[id_encontrado]
                    print(f"La persona '{nombre_buscado}' fue eliminada.")
                    break  # Salir del while después de eliminar
                else:
                    print("Persona no encontrada.")
                    # Si quieres pedir el nombre otra vez, puedes continuar el ciclo,
                    # si no, pones break para salir
                    break

            except BaseException as error:
                print(error)

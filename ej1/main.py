from metodos import*
agencia=agencia()
ciclo=True
while ciclo:
    print('''
    *** MENU PRINCIPAL ***
    1.- Turistas por país.
    2.- Turista por mes.
    3.- Eliminar turista.
    4.- Salir
    ''')

    try:
        op=input("Ingrese su opcion: ").strip()
        if not op.isdigit():
            print("porfavor ingrese un numero valido. ")
            continue
        op=int(op)
        match op:
            case 1:
                paises=set([datos[1] for datos in agencia.turistas.values()])
                print(f"paises disponibles: {', '.join(paises)}")
                pais = input("Ingrese el país a buscar: ").strip()
                agencia.turistas_por_pais(pais)  # <- nombre correcto del método
            case 2:
                print("meses disponible: 1-12")
                mes=input("ingese el numero del mes ").strip()
                porcentaje=agencia.turista_mes(mes)
                print(f"el porcentaje de turistas que llegaron en el mes {mes} y fue de: {porcentaje}%")
                pass
            case 3:
                agencia.eliminar()
                pass
            case 4:
                ciclo= False
                print("adiooos")    
            case _:
                print("dato mal ingresado")            
    except BaseException as error:
        print(error)
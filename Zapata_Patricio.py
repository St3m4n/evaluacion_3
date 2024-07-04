from os import system
from random import randint
system("cls")
pedidos = []
rutas = ["Concepción", "Chiguayante", "Talcahuano", "Hualpén", "San Pedro"]
def registrar_pedido():
    while True:
        nombre_apellido = input("Ingrese un nombre y un apellido: ")
        if " " in nombre_apellido:
            revisar = nombre_apellido.split(" ")
            if (len(revisar) == 2) and (len(revisar[0]) >= 3) and (revisar[0].isalpha()) and (revisar[1].isalpha()):
                break
            else:
                    print("Por favor, respete el formato, ejemplo: Wacoldo Luna")
        else:
            print("Por favor, respete el formato, ejemplo: Wacoldo Luna")
    direccion = input("Ingrese su direccion: ")
    while True:
        print(f"Rutas disponibles: {rutas[0]}, {rutas[1]}, {rutas[2]}, {rutas[3]}, {rutas[4]}")
        sector = input("Ingrese su Sector: ")
        if sector in rutas:
            break
        else:
            print("Ruta no disponible, intente nuevamente...")
    solicitando = True
    disp_seis = 0
    disp_dies = 0
    disp_veinte = 0
    while solicitando:
        print('''
    1.- Dispensador de 6L
    2.- Dispensador de 10L
    3.- Dispensador de 20L
    ''')
        selec = input("Ingrese que producto desea: ")
        match selec:
            case "1":
                ingresando = True
                while ingresando:
                    try:
                        cantidad = int(input("Ingrese la cantidad a solicitar: "))
                        if cantidad < 0:
                            print("No puede ingresar valores negativos, intente nuevamente...")
                        else:
                            disp_seis += cantidad   
                            ingresando = False
                    except ValueError:
                        print("Cantidad ingresada no valida, intente nuevamente...")
            case "2":
                ingresando = True
                while ingresando:
                    try:
                        cantidad = int(input("Ingrese la cantidad a solicitar: "))
                        if cantidad < 0:
                            print("No puede ingresar valores negativos, intente nuevamente...")
                        else:
                            disp_dies += cantidad   
                            ingresando = False
                    except ValueError:
                        print("Cantidad ingresada no valida, intente nuevamente...")                    
            case "3":
                ingresando = True
                while ingresando:
                    try:
                        cantidad = int(input("Ingrese la cantidad a solicitar: "))
                        if cantidad < 0:
                            print("No puede ingresar valores negativos, intente nuevamente...")
                        else:
                            disp_veinte += cantidad   
                            ingresando = False
                    except ValueError:
                        print("Cantidad ingresada no valida, intente nuevamente...")                    
            case other:
                print("opción ingresada no valida...")
        while True:
            continuar = input("Desea agregar otro tipo de producto? s/n: ")
            if continuar.lower() in ["s", "n"] and continuar.isalpha():
                break
            else:
                print("Por favor, ingrese 's' para continuar ingresando o 'n' para finalizar el pedido...")
        if continuar.lower() == "s":
                solicitando = True
        else:
            if (disp_dies + disp_seis + disp_veinte) >0:
                id = randint(100000, 999999)
                pedido = [id, nombre_apellido, direccion, sector, disp_seis, disp_dies, disp_veinte]
                pedidos.append(pedido)
                system("cls")
                print(f"Se a registrado el pedido, el ID del registro es {id}")
                solicitando = False
            else:
                system("cls")
                print("No se a ingresado ninguna solicitud, ya que no solicito productos....")
                solicitando = False
    return

def listar_pedidos():
    if len(pedidos) >0:
        print('''
    ID      Cliente         Dirección           Sector         Disp. 6lts      Disp. 10lts      Disp. 20lts
''')
        for pedido in pedidos:
            print(f'''
    {pedido[0]}  {pedido[1]}    {pedido[2]}        {pedido[3]}      {pedido[4]}                {pedido[5]}              {pedido[6]}
''')
    else:
        print("No se registran pedidos...")
    return

def imprimir_ruta():
    if len(pedidos)>0:
        print("Rutas disponibles: ")
        contador = 0
        for ruta in rutas:
            contador +=1
            print(f"{contador}.- {ruta}")
        ruta_seleccionada = int(input("Ingrese la ruta que desea imprimir: "))
        existen = 0
        for pedido in pedidos:
            if pedido[3] == rutas[ruta_seleccionada-1]:
                existen +=1
        if existen > 0:
            archivo = open(f"Sector_de_{rutas[ruta_seleccionada-1]}", "w")
            archivo.write("ID;Cliente;Direccion;Sector;Disp. 6lts; Disp. 10lts; Disp. 20lts\n")
            for pedido in pedidos:
                if pedido[3] == rutas[ruta_seleccionada-1]:
                    archivo.write(";".join(map(str,pedido))+"\n")
            archivo.close()
            print("Se a ganerado archivo con los pedidos")
        else:
            print("No se registran pedidos para la ruta seleccionada, no se genera archivo...")
    else:
        print("No se registran pedidos para generar un archivo de ruta...")
    return
def buscar_pedido():
    if len(pedidos) >0:
        buscar = int(input("Ingrese el ID del pedido a buscar: "))
        for pedido in pedidos:
            if buscar == pedido[0]:
                print('''
        ID      Cliente         Dirección           Sector         Disp. 6lts      Disp. 10lts      Disp. 20lts
''')
                print(f'''
        {pedido[0]}  {pedido[1]}    {pedido[2]}        {pedido[3]}      {pedido[4]}                {pedido[5]}              {pedido[6]}
    ''')
            else:
                print("No se registran pedidos con ese ID...")
    else:
        print("Actualmente no se registran pedidos...")
    return

while True:
    print('''
1. Registrar pedido
2. Listar los todos los pedidos
3. Imprimir hoja de ruta
4. Buscar un pedido por ID
5. Salir del programa
''')
    op = input("Ingrese la opción: ")

    match op:
        case "1":
            registrar_pedido()
        case "2":
            system("cls")
            listar_pedidos()
        case "3":
            system("cls")
            imprimir_ruta()
        case "4":
            system("cls")
            buscar_pedido()
        case "5":
            break
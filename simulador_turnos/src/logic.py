def agregar_turnos(turnos):
    nombre= input("¿Cuál es su nombre?")
    activo=True
    while activo==True:
        edad= int(input("¿Cuál es su edad?"))
        if edad<100 and edad>0:
            activo=False
        else:
            print("Pruebe de nuevo")
            activo=True
    especialidad=0
    while especialidad==0:
        print('¿Qué especialidad quiere?\nA. Dermatología\nB. Cardiología\nC. Clínica')
        esp= input('Responda con una letra\n')
        if esp=='A' or esp=='a':
            especialidad='Dermatología'
            break
        elif esp=='B' or esp=='b':
            especialidad='Cardiología'
            break
        elif esp=='C' or esp=='c':
            especialidad='Clínica'
            break
        else:
            especialidad=0
            print("Seleccione una letra entre la lista")
        print("Muchas gracias")
    turno={
        'nombre':nombre,
        'edad':edad,
        'especialidad':especialidad
        }
    turnos.append(turno)
    return turnos
       
def mostrar_turnos(turnos):
    print('Estos son los turnos que hay en el momento:')
    i=1
    for line in turnos:
        print(i, ".", line["nombre"], line["edad"], line["especialidad"])
        i=i+1
    return 

def filtrar_por_especialidad(turnos):
    activo=True
    while activo==True:
        print('¿Qué especialidad quiere?\nA. Dermatología\nB. Cardiología\nC. Clínica')
        esp= input('Responda con una letra\n')
        if esp=='A' or esp=='a':
            especialidad='Dermatología'
            activo=False
        elif esp=='B' or esp=='b':
            especialidad='Cardiología'
            activo=False
        elif esp=='C' or esp=='c':
            especialidad='Clínica'
            activo=False
        else:
            print("Seleccione una letra entre la lista")
            activo=True
        print("Muchas gracias")
    i=1
    for line in turnos:
        if line["especialidad"]== especialidad:
            print(i, ".", line["nombre"], line["edad"], line["especialidad"])
            i=i+1
        else:
            pass
    return

def filtrar_mayores(turnos):
    activo=True
    while activo==True:
        edad= int(input("¿Cuál es la edad que desea filtrar?\n"))
        if edad<100 and edad>0:
            activo=False
        else:
            print("Pruebe de nuevo")
            activo=True
    activo=True
    while activo==True:
        filtro=input("¿cómo desea filtrar?\n A. Mayores a esa edad \n B. Menores a esa edad\n")
        if filtro!="A" and filtro!="a" and filtro!="b" and filtro!="B":
            print("Pruebe con una de las opciones")
            activo=True
        else:
            activo= False
    if filtro=='a' or filtro=='A':
        i=1
        for line in turnos:
            if line["edad"]>=edad:
                print(i, ".", line["nombre"], line["edad"], line["especialidad"])
                i=i+1
            else:
                pass
    else:
        i=1
        for line in turnos:
            if line["edad"]<=edad:
                print(i, ".", line["nombre"], line["edad"], line["especialidad"])
                i=i+1
            else:
                pass
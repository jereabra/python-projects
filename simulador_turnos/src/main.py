from storage import cargar_turnos, guardar_turnos, exportar_csv, exportar_txt
from logic import agregar_turnos, mostrar_turnos, filtrar_mayores, filtrar_por_especialidad

turnos=cargar_turnos()
print("se cargaron los turnos")

def main():
    activo=True
    while activo==True:
        print("Bienvenid@, elija como desea comenzar:")
        opcion=int(input('1. Agregar turno.\n2. Mostrar todos los turnos.\n3. Filtrar por especialidad \n4. Filtrar por edad \n5. Exportar csv \n6. Exportar TXT \n7. Guardar y Salir.\n'))

        if opcion==1:
            agregar_turnos(turnos)
            mostrar_turnos(turnos)
        elif opcion==2:
            mostrar_turnos(turnos)
        elif opcion==3:
            filtrar_por_especialidad(turnos)
        elif opcion==4:
            filtrar_mayores(turnos)
        elif opcion==5:
            exportar_csv(turnos)
            print('Se han guardado correctamente los turnos')
        elif opcion==6:
            exportar_txt(turnos)
            print('Se han guardado correctamente los turnos')
        elif opcion==7:
            guardar_turnos(turnos)
            print('Se han guardado correctamente los turnos')
            print("Muchas gracias")
            activo=False
        else:
            print("Elija una opción correcta")


main()
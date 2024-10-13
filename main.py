def main():
    while True:
        opcion = menu_principal()

        if opcion == 1:
            ingresar_puntuacion_y_comentario()
        elif opcion == 2:
            mostrar_resultados()
        elif opcion == 3:
            print("Finalizando...")
            break
        else:
            print("Introduzca un número del 1 al 3.")


def menu_principal():
    """Despliega el menú principal y solicita la opción al usuario."""
    print("Seleccione el proceso que desea aplicar:")
    print("1: Ingresar puntuación y comentario")
    print("2: Comprobar los resultados obtenidos hasta ahora")
    print("3: Finalizar")
    opcion = input(">> ")

    if opcion.isdecimal():
        return int(opcion)
    else:
        print("Por favor, introduzca un número válido.")
        return 0


def ingresar_puntuacion_y_comentario():
    """Solicita una puntuación y comentario, y los guarda en un archivo."""
    while True:
        punto = input("Por favor, introduzca una puntuación en una escala del 1 al 5: ")
        if punto.isdecimal():
            punto = int(punto)
            if 1 <= punto <= 5:
                comentario = input("Por favor, introduzca un comentario: ")
                guardar_en_archivo(punto, comentario)
                break
            else:
                print("Introduzca un valor entre 1 y 5.")
        else:
            print("Introduzca una puntuación válida en números.")


def guardar_en_archivo(punto, comentario):
    """Guarda la puntuación y el comentario en un archivo."""
    with open("data.txt", "a") as archivo:
        archivo.write(f"Puntuación: {punto} | Comentario: {comentario}\n")


def mostrar_resultados():
    """Lee y muestra los resultados guardados hasta el momento."""
    try:
        with open("data.txt", "r") as archivo:
            contenido = archivo.read()
            print("Resultados hasta la fecha:")
            print(contenido if contenido else "No hay datos registrados.")
    except FileNotFoundError:
        print("No se encontraron resultados guardados.")


if __name__ == "__main__":
    main()

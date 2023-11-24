import json

from composite import ArchivoSAMUR, Documento, Carpeta


def cargar_json(ruta):
    try:
        with open(ruta, 'r') as archivo:
            data = json.load(archivo)
        return data
    except FileNotFoundError:
        print(f"El archivo en la ruta '{ruta}' no fue encontrado.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error al decodificar JSON en '{ruta}': {e}")
        return None


ruta_json = 'Emergencias/data/prueba.json'


def cargar_estructura_desde_json(ruta):
    datos_json = cargar_json(ruta)
    if datos_json:
        nombre = datos_json['nombre']
        tipo = datos_json['tipo']
        contenido = []
        for item in datos_json['contenido']:
            if item['tipo'] == 'documento':
                contenido.append(
                    Documento(item['nombre'], item['tipo'], item['tamaño']))
            # Puedes manejar otros tipos de archivos aquí si los tienes definidos

        carpeta = Carpeta(nombre)
        carpeta.contenido = contenido
        return carpeta
    return None


estructura = cargar_estructura_desde_json(ruta_json)


def guardar_json(nombre_archivo, estructura):
    estructura_serializable = estructura.to_dict()
    with open(nombre_archivo, 'w') as archivo_salida:
        json.dump(estructura_serializable, archivo_salida, indent=4)


def mostrar_contenido_json(ruta):
    datos_json = cargar_json(ruta)
    if datos_json:
        print(json.dumps(datos_json, indent=4, ensure_ascii=False))


def seleccionar_carpeta_por_ruta(carpeta_actual, ruta):
    carpetas = ruta.split('/')
    carpeta_temp = carpeta_actual

    # Verificar si la primera carpeta de la ruta coincide con la carpeta actual
    if carpetas[0] != carpeta_temp.obtener_nombre():
        print(f"No se encontró la carpeta '{
              carpetas[0]}' como carpeta actual.")
        return None

    for nombre in carpetas[1:]:
        encontrado = False
        for contenido in carpeta_temp.contenido:
            if isinstance(contenido, Carpeta) and contenido.obtener_nombre() == nombre:
                carpeta_temp = contenido
                encontrado = True
                break

        if not encontrado:
            print(f"No se encontró la carpeta '{
                  nombre}' en la ruta proporcionada.")
            return None

    return carpeta_temp


ruta_json = 'Emergencias/data/prueba.json'
estructura = Carpeta('Documentos')

# Aquí debes cargar tu estructura inicial desde el JSON


def mostrar_menu():
    print("1. Mostrar JSON")
    print("2. Agregar documento")
    print("3. Agregar carpeta")
    print("4. Eliminar documento")
    print("5. Salir")


def main():
    carpeta_actual = estructura

    while True:
        mostrar_menu()
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            mostrar_contenido_json(ruta_json)
        elif opcion == 2:
            ruta = input(
                "Ingrese la ruta de la carpeta (p.ej., 'Carpeta locura'): ")
            carpeta_para_documento = seleccionar_carpeta_por_ruta(
                carpeta_actual, ruta)
            if carpeta_para_documento:
                nombre = input("Ingrese el nombre del documento: ")
                tipo = input("Ingrese el tipo del documento: ")
                tamaño = input("Ingrese el tamaño del documento: ")
                documento = Documento(nombre, tipo, tamaño)
                carpeta_para_documento.agregar_documento(documento)
                guardar_json(ruta_json, estructura)
        elif opcion == 3:
            nombre = input("Ingrese el nombre de la carpeta a agregar: ")
            carpeta = Carpeta(nombre)
            carpeta_actual.agregar_carpeta(carpeta)
            guardar_json(ruta_json, estructura)
        elif opcion == 4:
            guardar_json(ruta_json, estructura)
        elif opcion == 5:
            break
        else:
            print("Opción inválida.")


if __name__ == '__main__':
    estructura = cargar_estructura_desde_json(ruta_json)
    main()
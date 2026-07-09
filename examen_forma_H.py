arreglos = {
    'FLO1': ['Ramo Primavera', 'ramo', 'rosado', 'M', True, 'primavera'],
    'FLO2': ['Caja Elegante', 'caja', 'blanco', 'L', True, 'todo año'],
    'FLO3': ['Ramo Solar', 'ramo', 'amarillo', 'S', False, 'verano'],
    'FLO4': ['Centro Mesa', 'centro', 'rojo', 'M', True, 'todo año'],
    'FLO5': ['Ramo Bosque', 'ramo', 'verde', 'L', False, 'otoño'],
    'FLO6': ['Caja Noche', 'caja', 'morado', 'M', True, 'invierno']
}
bodega = {
    'FLO1': [15990, 8],
    'FLO2': [29990, 3],
    'FLO3': [9990, 12],
    'FLO4': [24990, 5],
    'FLO5': [19990, 0],
    'FLO6': [22990, 6]
}
def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Debe seleccionar una opción válida")
        except ValueError:
            print("Debe seleccionar una opción válida")
        

def unidades_tipo(tipo, arreglos, bodega):
    total = 0
    for codigo, datos in arreglos.items():
        if datos[1].lower() == tipo.lower():
            total += bodega.get(codigo, [0, 0])[1]
            print(f"El total de unidades disponibles es: {total}")

def busqueda_precio(p_min, p_max, arreglos, bodega):
    resultados = []
    for codigo, (precio, unidades) in bodega.items():
        if p_min <= precio <= p_max and unidades != 0:
            nombre = arreglos[codigo][0]
            resultados.append(f"{nombre}--{codigo}")
        if resultados:
            print("Los arreglos encontrados son:", sorted(resultados))
        else:
            print("No hay arreglos en ese rango de precios.")
def buscar_codigo(codigo, diccionario):
    codigo = codigo.upper()
    return codigo in (key.upper() for key in diccionario.keys())

def actualizar_precio(codigo, nuevo_precio, bodega):
    codigo = codigo.upper()
    for key in bodega.keys():
        if key.upper() == codigo:
            bodega[key][0] = nuevo_precio
            return True
    return False

def validar_codigo(codigo, arreglos, bodega):
    if not codigo.strip():
        return False
        codigo = codigo.upper()
    if codigo in (key.upper() for key in arreglos.keys()) or codigo in (key.upper() for key in bodega.keys()):
        return False
    return True

def validar_nombre(nombre):
    return bool(nombre.strip())

def validar_tipo(tipo):
    return bool(tipo.strip())

def validar_color(color):
    return bool(color.strip())

def validar_tamano(tamano):
    return tamano in ['S', 'M', 'L']

def validar_tarjeta(tarjeta):
    return tarjeta.lower() in ['s', 'n']

def validar_temporada(temporada):
    return bool(temporada.strip())

def validar_precio(precio):
    return isinstance(precio, int) and precio > 0

def validar_unidades(unidades):
    return isinstance(unidades, int) and unidades >= 0

def agregar_arreglo(codigo, nombre, tipo, color, tamano, tarjeta, temporada, precio, unidades, arreglos, bodega):
    codigo = codigo.upper()
    if codigo in arreglos or codigo in bodega:
        return False
    arreglos[codigo] = [nombre, tipo, color, tamano, tarjeta, temporada]
    bodega[codigo] = [precio, unidades]
    return True

def eliminar_arreglo(codigo, arreglos, bodega):
    codigo = codigo.upper()
    if codigo in (key.upper() for key in arreglos.keys()):
        real_key = next(key for key in arreglos.keys() if key.upper() == codigo)
        arreglos.pop(real_key)
        bodega.pop(real_key)
        return True
    return False

def main():
    while True:
        print("========== MENÚ PRINCIPAL ==========")
        print("1. Unidades por tipo de arreglo")
        print("2. Búsqueda de arreglos por rango de precio")
        print("3. Actualizar precio de arreglo")
        print("4. Agregar arreglo")
        print("5. Eliminar arreglo")
        print("6. Salir")
        print("====================================")
        opcion = leer_opcion()
        if opcion == 1:
            tipo = input("Ingrese tipo de arreglo a consultar: ")
            unidades_tipo(tipo, arreglos, bodega)
        elif opcion == 2:
            while True:
                try:
                    p_min = int(input("Ingrese precio mínimo: "))
                    p_max = int(input("Ingrese precio máximo: "))
                    if p_min < 0 or p_max < 0 or p_min > p_max:
                        print("Debe ingresar valores enteros válidos")
                        continue
                    break
                except ValueError:
                    print("Debe ingresar valores enteros")
            busqueda_precio(p_min, p_max, arreglos, bodega)
        elif opcion == 3:
            while True:
                codigo = input("Ingrese código del arreglo: ")
                try:
                    nuevo_precio = int(input("Ingrese nuevo precio: "))
                    if nuevo_precio <= 0:
                        print("El precio debe ser mayor que cero")
                        continue
                except ValueError:
                    print("Debe ingresar un valor entero para el precio")
                    continue
                if actualizar_precio(codigo, nuevo_precio, bodega):
                    print("Precio actualizado")
                else:
                    print("El código no existe")
                otro = input("¿Desea actualizar otro precio (s/n)?: ")
                if otro.lower() != 's':
                    break
        elif opcion == 4:
            codigo = input("Ingrese código del arreglo: ")
            nombre = input("Ingrese nombre: ")
            tipo = input("Ingrese tipo: ")
            color = input("Ingrese color principal: ")
            tamano = input("Ingrese tamaño (S/M/L): ")
            tarjeta = input("¿Incluye tarjeta? (s/n): ")
            temporada = input("Ingrese temporada: ")
            try:
                precio = int(input("Ingrese precio: "))
                unidades = int(input("Ingrese unidades: "))
            except ValueError:
                print("Precio y unidades deben ser valores enteros")
                continue
            # Validaciones
            if not validar_codigo(codigo, arreglos, bodega):
                print("Código inválido o ya existe")
                continue
            if not validar_nombre(nombre):
                print("Nombre inválido")
                continue
            if not validar_tipo(tipo):
                print("Tipo inválido")
                continue
            if not validar_color(color):
                print("Color inválido")
                continue
            if not validar_tamano(tamano):
                print("Tamaño inválido")
                continue
            if not validar_tarjeta(tarjeta):
                print("Valor de tarjeta inválido")
                continue
            if not validar_temporada(temporada):
                print("Temporada inválida")
                continue
            if not validar_precio(precio):
                print("Precio inválido")
                continue
            if not validar_unidades(unidades):
                print("Unidades inválidas")
                continue
            incluye_tarjeta = True if tarjeta.lower() == 's' else False
            if agregar_arreglo(codigo, nombre, tipo, color, tamano, incluye_tarjeta, temporada, precio, unidades, arreglos, bodega):
                print("Arreglo agregado")
            else:
                print("El código ya existe")
        elif opcion == 5:
            codigo = input("Ingrese código del arreglo a eliminar: ")
            if eliminar_arreglo(codigo, arreglos, bodega):
                print("Arreglo eliminado")
            else:
                print("El código no existe")
        elif opcion == 6:
            print("Programa finalizado.")
            break

main()
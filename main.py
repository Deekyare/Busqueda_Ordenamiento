'''
Este será el archivo principal que importará las funciones de los otros archivos y manejará la interacción con el usuario,
el menú y la comparación de tiempos.'''

#Importaciones de modulos y librerias
import time
import random
from generador_listas import generar_lista_aleatoria, obtener_lista_usuario
from ordenamiento import ordenar_lista
from busqueda_lineal import busqueda_lineal
from busqueda_binaria import busqueda_binaria

# --- Función Principal de Comparación ---

def comparar_metodos_busqueda(tamaño_lista, cantidad_busquedas):
    """
    Compara la eficiencia de los métodos de búsqueda lineal y binaria
    en una lista de números.
    Args:
        tamaño_lista (int): El número de elementos que tendrá la lista para la comparación.
        cantidad_busquedas (int): El número de veces que se realizará una búsqueda.
    """
    print("\n--- Iniciando Comparación de Métodos de Búsqueda y Ordenamiento ---")

    # Generar una lista aleatoria grande para la comparación
    lista_original = generar_lista_aleatoria(tamaño_lista)

    # --- Medir tiempo de Ordenamiento ---
    print("\n--> PASO 1: Ordenando la lista para la búsqueda binaria.")
    tiempo_inicio = time.perf_counter()
    lista_ordenada = ordenar_lista(lista_original)
    tiempo_ordenamiento = time.perf_counter() - tiempo_inicio
    print(f"Tiempo total de ordenamiento: {tiempo_ordenamiento:.6f} segundos")

    # Generar números aleatorios para buscar en ambas listas
    elementos_a_buscar = [random.randint(0, 1000000) for _ in range(cantidad_busquedas)]
    print(f"\nSe realizarán {cantidad_busquedas} búsquedas aleatorias.")

    # --- Medir tiempo de Búsqueda Lineal ---
    print("\n--> PASO 2: Realizando búsquedas lineales.")
    tiempo_total_lineal = 0
    elementos_encontrados_lineal = 0
    for elemento in elementos_a_buscar:
        tiempo_inicio = time.perf_counter()
        posicion = busqueda_lineal(lista_ordenada, elemento) # Se busca en la lista ordenada para una comparación justa si se encontrara
        tiempo_total_lineal += time.perf_counter() - tiempo_inicio
        if posicion != -1:
            elementos_encontrados_lineal += 1
    print(f"Tiempo total para búsqueda lineal: {tiempo_total_lineal:.6f} segundos")
    print(f"Elementos encontrados (Lineal): {elementos_encontrados_lineal}")

    # --- Medir tiempo de Búsqueda Binaria ---
    print("\n--> PASO 3: Realizando búsquedas binarias.")
    tiempo_total_binaria = 0
    elementos_encontrados_binaria = 0
    for elemento in elementos_a_buscar:
        tiempo_inicio = time.perf_counter()
        posicion = busqueda_binaria(lista_ordenada, elemento)
        tiempo_total_binaria += time.perf_counter() - tiempo_inicio
        if posicion != -1:
            elementos_encontrados_binaria += 1
    print(f"Tiempo total para búsqueda binaria: {tiempo_total_binaria:.6f} segundos")
    print(f"Elementos encontrados (Binaria): {elementos_encontrados_binaria}")

    # --- Mostrar Resultados y Conclusiones ---
    print("\n--- Resultados de la Comparación ---")
    print(f"Tamaño de la lista utilizada: {tamaño_lista}")
    print(f"Cantidad de búsquedas realizadas: {cantidad_busquedas}")
    print(f"Tiempo de ordenamiento inicial de la lista: {tiempo_ordenamiento:.6f} segundos")
    print(f"Tiempo total para búsquedas lineales: {tiempo_total_lineal:.6f} segundos")
    print(f"Tiempo promedio por búsqueda lineal: {tiempo_total_lineal/cantidad_busquedas:.9f} segundos")
    print(f"Tiempo total para búsquedas binarias: {tiempo_total_binaria:.6f} segundos")
    print(f"Tiempo promedio por búsqueda binaria: {tiempo_total_binaria/cantidad_busquedas:.9f} segundos")
    print(f"Diferencia de tiempo (Lineal - Binaria): {tiempo_total_lineal - tiempo_total_binaria:.6f} segundos")

    print("\n--- Conclusión General ---")
    if tiempo_total_lineal > tiempo_total_binaria:
        print("La **búsqueda binaria** es significativamente más rápida para listas grandes.")
        print("**Razón**: La búsqueda binaria tiene una complejidad de tiempo de **O(log n)**,")
        print("mientras que la búsqueda lineal tiene **O(n)**. Esto significa que la búsqueda binaria")
        print("reduce el espacio de búsqueda a la mitad en cada paso, siendo mucho más eficiente")
        print(f"cuando la lista es grande (como en este caso con {tamaño_lista} elementos).")
        print("Sin embargo, es crucial recordar que la búsqueda binaria requiere que la lista esté **ordenada** previamente,")
        print(f"lo que agrega un costo inicial de ordenamiento (O(n log n), en nuestro caso {tiempo_ordenamiento:.6f} segundos).")
    else:
        print("En este caso (poco común para listas grandes), la búsqueda lineal fue más rápida o similar.")
        print("Esto podría ocurrir en listas muy pequeñas o si los elementos buscados están al principio de la lista.")
        print("Generalmente, para grandes volúmenes de datos, la búsqueda binaria es superior si la lista está ordenada.")
    print("\n--- Fin de la Comparación ---")

# --- Programa Principal (Interactivo) ---

if __name__ == "__main__":
    random.seed(42) # Para que los resultados aleatorios sean los mismos cada vez que se ejecuta

    print("¡Bienvenido al programa de Búsqueda y Ordenamiento!")
    print("Aquí podrás explorar cómo funcionan y qué tan eficientes son.")

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Realizar un ejemplo de ordenamiento y búsqueda con tu propia lista.")
        print("2. Comparar la eficiencia de la búsqueda lineal y binaria (con lista grande generada).")
        print("3. Salir.")

        opcion = input("Elige una opción (1, 2 o 3): ")

        if opcion == '1':
            print("\n--- EJEMPLO CON TU PROPIA LISTA ---")
            mi_lista = obtener_lista_usuario()

            if not mi_lista:
                print("La lista está vacía. Intenta de nuevo.")
                continue

            print(f"\nTu lista original: {mi_lista}")

            # Ordenar la lista del usuario
            lista_ordenada_usuario = ordenar_lista(mi_lista)
            print(f"Tu lista ordenada: {lista_ordenada_usuario}")

            # Realizar búsqueda en la lista del usuario
            while True:
                try:
                    elemento_a_buscar_usuario = int(input("\n¿Qué número deseas buscar en tu lista? (ingresa un número): "))
                    break
                except ValueError:
                    print("Por favor, ingresa un número válido.")

            # Búsqueda Lineal
            posicion_lineal = busqueda_lineal(lista_ordenada_usuario, elemento_a_buscar_usuario)
            if posicion_lineal != -1:
                print(f"Búsqueda Lineal: El número {elemento_a_buscar_usuario} fue encontrado en la posición (índice) {posicion_lineal}.")
            else:
                print(f"Búsqueda Lineal: El número {elemento_a_buscar_usuario} no fue encontrado en la lista.")

            # Búsqueda Binaria
            posicion_binaria = busqueda_binaria(lista_ordenada_usuario, elemento_a_buscar_usuario)
            if posicion_binaria != -1:
                print(f"Búsqueda Binaria: El número {elemento_a_buscar_usuario} fue encontrado en la posición (índice) {posicion_binaria}.")
            else:
                print(f"Búsqueda Binaria: El número {elemento_a_buscar_usuario} no fue encontrado en la lista.")

        elif opcion == '2':
            print("\n--- COMPARACIÓN DE EFICIENCIA (LISTA GRANDE) ---")
            try:
                tamano_lista = int(input("Ingresa el tamaño de la lista a generar (ej: 10000 para una lista grande): "))
                num_busquedas = int(input("Ingresa la cantidad de búsquedas a realizar (ej: 100): "))
                if tamano_lista <= 0 or num_busquedas <= 0:
                    print("El tamaño de la lista y la cantidad de búsquedas deben ser números positivos.")
                    continue
                comparar_metodos_busqueda(tamano_lista, num_busquedas)
            except ValueError:
                print("Entrada inválida. Por favor, ingresa números enteros para el tamaño y la cantidad de búsquedas.")

        elif opcion == '3':
            print("\n¡Gracias por usar el programa! ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige 1, 2 o 3.")
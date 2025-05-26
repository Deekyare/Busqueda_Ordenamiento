"""Esta función realiza una búsqueda binaria en una lista ordenada.
    Divide repetidamente la lista a la mitad hasta encontrar el elemento.
    Es mucho más eficiente que la búsqueda lineal para listas grandes y ordenadas.
    Argumentos que va a recibir:
        lista_ordenada_para_buscar (list): La lista (debe estar ordenada) en la que se buscará.
        elemento_a_buscar (int): El número que se busca dentro de la lista.
        Se retorna:
        int: La posición (índice) del elemento si se encuentra, de lo contrario, -1.
        Cuando se trabaja con funciones de búsqueda como busqueda_lineal o busqueda_binaria,
        es una convención común usar el valor -1 para indicar que un elemento no fue encontrado en la lista.
        Si la función devolviera, 0 para indicar que no se encontró, sería ambiguo, ya que 0 es un índice válido (el primer elemento)
    """

def busqueda_binaria(lista_ordenada_para_buscar, elemento_a_buscar):
   
    print(f"Realizando búsqueda binaria para encontrar el número '{elemento_a_buscar}'...")
    izquierda = 0 # Define el límite inferior de la búsqueda
    derecha = len(lista_ordenada_para_buscar) - 1 # Define el límite superior de la búsqueda

    while izquierda <= derecha:
        punto_medio = (izquierda + derecha) // 2 # Calcula el punto medio de la sección actual
        if lista_ordenada_para_buscar[punto_medio] == elemento_a_buscar:
            return punto_medio # Se encontró el elemento en el punto medio
        elif lista_ordenada_para_buscar[punto_medio] < elemento_a_buscar:
            izquierda = punto_medio + 1 # El elemento está en la mitad derecha, ajusta el límite inferior
        else:
            derecha = punto_medio - 1 # El elemento está en la mitad izquierda, ajusta el límite superior
    return -1 # El elemento no se encontró en la lista
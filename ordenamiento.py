""" Ordena una lista de números de forma ascendente.
    Argumentos que va a recibir:
        lista_a_ordenar (list): La lista de números que se desea ordenar.
    Se retorna:
        list: Una nueva lista con los números ordenados.
"""

def ordenar_lista(lista_a_ordenar):

    print("\nIniciando el proceso de ordenamiento de la lista...")
    lista_ordenada = lista_a_ordenar.copy()  # Creamos una copia para no modificar la lista original
    lista_ordenada.sort() # El método .sort() ordena la lista en su lugar
    print("¡Lista ordenada con éxito!")
    return lista_ordenada
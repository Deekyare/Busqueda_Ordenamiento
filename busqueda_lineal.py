"""Esta función realiza una búsqueda lineal (o secuencial) en una lista.
    Examina cada elemento de la lista uno por uno hasta encontrar el elemento deseado.
    Argumentos que va a recibir:
        lista_donde_buscar (list): La lista en la que se realizará la búsqueda.
        elemento_a_buscar (int): El número que se busca dentro de la lista.
    Se retorna:
        int: La posición (índice) del elemento si se encuentra, de lo contrario, -1."""
        
def busqueda_lineal(lista_donde_buscar, elemento_a_buscar):
   
    print(f"Realizando búsqueda lineal para encontrar el número '{elemento_a_buscar}'...")
    
    #enumerate: obtenemos indice y valor de cada elemento en la iteración
    for indice, elemento_actual in enumerate(lista_donde_buscar):
        if elemento_actual == elemento_a_buscar:
            return indice # Se encontró el elemento, se devuelve su posición
    return -1 # El elemento no se encontró en la lista
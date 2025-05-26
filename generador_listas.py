import random
""" Genera una lista de números enteros aleatorios.
     Argumentos a recibir por la función:
        cantidad_elementos (int): El número de elementos que tendrá la lista.
        valor_minimo (int): El valor mínimo posible para los números aleatorios.
        valor_maximo (int): El valor máximo posible para los números aleatorios.
    Retorno:
        list: Una lista de números enteros aleatorios."""

def generar_lista_aleatoria(cantidad_elementos, valor_minimo=0, valor_maximo=1000000):
  
    print(f"Generando una lista con {cantidad_elementos} números aleatorios entre {valor_minimo} y {valor_maximo}")
    return [random.randint(valor_minimo, valor_maximo) for _ in range(cantidad_elementos)]

def obtener_lista_usuario():
    """
    Permite al usuario ingresar una lista de números.
    Returns:
        list: Una lista de números ingresados por el usuario.
    """
    while True:
        entrada_usuario = input("Por favor, ingresa los números separados por comas (ej: 10,20,5,30): ")
        try:
            # Convertir la cadena de entrada en una lista de enteros
            lista_numeros = [int(numero.strip()) for numero in entrada_usuario.split(',')]
            return lista_numeros
        except ValueError:
            print("Entrada inválida. Asegúrate de ingresar solo números separados por comas.")
def suma_consecutivos(lista):
    if not isinstance(lista, list):
        raise TypeError("El parametro debe ser una lista.")
    
    if not all(isinstance(i, (int, float)) for i in lista):
        raise ValueError("Todos los elementos de la lista deben ser números.")
    
    if len(lista) < 2:
        raise ValueError("La lista debe contener al menos dos elementos.")

    mayor_suma = lista[0] + lista[1]  
    for i in range(1, len(lista) - 1):
        suma_actual = lista[i] + lista[i + 1]
        if suma_actual > mayor_suma:
            mayor_suma = suma_actual

    return mayor_suma

try:
    lista = [5, 1, 3, 7, 9, 17, 10]
    print(suma_consecutivos(lista))  
except (TypeError, ValueError) as e:
    print(f"Error: {e}")

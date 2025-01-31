def mismos_caracteres(lista):
    grupos = {}
    
    for palabra in lista:
        if not isinstance(palabra, str):
            raise ValueError(f"Todos los elementos de la lista deben ser cadenas. Se encontró: {type(palabra)}")
        
        clave = tuple(sorted(palabra))
        
        if clave in grupos:
            grupos[clave].append(palabra)
        else:
            grupos[clave] = [palabra]
    
    resultado = []
    for palabras in grupos.values():
        if len(palabras) > 1:
            resultado.extend(palabras)
    
    return resultado

try:
    lista = ["amor", "roma", "perro"]
    print(mismos_caracteres(lista))
except ValueError as e:
    print(f"Error: {e}")
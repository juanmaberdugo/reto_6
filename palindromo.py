def palindromo(palabra):
    try:
        palabra = str(palabra)
        palabra = palabra.lower()
        longitud = len(palabra)
        for i in range(longitud // 2):
            if palabra[i] != palabra[longitud - i - 1]:
                print("No es palíndromo")
                return False
        print("Es palíndromo")
        return True
    except Exception as e:
        print(f"Error inesperado: {str(e)}")
        return False

try:
    palabra = input("Escriba la palabra: ")
    print(palindromo(palabra))
except Exception as e:
    print(f"Error inesperado: {str(e)}")

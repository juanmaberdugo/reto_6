def primo(numero):
    for i in range(2, numero):
        if numero % i == 0:
            print("No es primo", i, "es divisor")
            return False
    print("Es primo")
    return True

try:
    numero = int(input("Ingrese el número: "))
    print(primo(numero))
except ValueError as e:
    print("Error:", e)
except Exception as e:
    print("Ocurrió un error inesperado:", e)
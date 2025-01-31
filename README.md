# reto_6
Para este reto se planteo el uso de excepciones en el codigo que se desarrollo en los anteriores retos.
## Primera parte
- Add the required exceptions in the Reto 1 code assigments

Para esta primera funcion se usaron excepciones en caso de que se intentara ingresar divisiones con denominador cero y que se le ingresaran valores incorrecttos.
```python
def operaciones_basicas(numero_1, numero_2, eleccion_operacion):
    try:
        operacion_matematica = eleccion_operacion.lower().replace(" ", "")
        match operacion_matematica:
            case "+":
                return numero_1 + numero_2
            case "-":
                return numero_1 - numero_2
            case "*":
                return numero_1 * numero_2
            case "/":
                if numero_2 == 0:
                    raise ZeroDivisionError("Error: No se puede dividir por cero.")
                return numero_1 / numero_2
            case _:
                raise ValueError("Operacion no existente. Por favor, escriba bien el nombre.")
    except ZeroDivisionError as e:
        return str(e)
    except ValueError as e:
        return str(e)
    except Exception as e:
        return f"Error inesperado: {str(e)}"

try:
    primer_numero = int(input("Digite el primer número a realizar operación: "))
    segundo_numero = int(input("Digite el segundo número a realizar operación: "))
    operacion = str(input("Escriba la operación a realizar (+, -, *, /): "))
    resultado = operaciones_basicas(primer_numero, segundo_numero, operacion)
    print("Resultado:", resultado)
except ValueError:
    print("Error: Entrada no válida. Asegúrese de ingresar números enteros.")
except Exception as e:
    print(f"Error inesperado: {str(e)}")
```

En esta se usaron en caso de que un error inesperado cualquiera ocurriera en el codigo
```python
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
```

Aca se usaron en caso de que se ingresara un valor invalido y que ocurriera un error inesperado
```python
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
```


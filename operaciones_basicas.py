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

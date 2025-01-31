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

En esta se usaron en caso de que un error inesperado cualquiera ocurriera en el codigo.
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

Aca se usaron en caso de que se ingresara un valor invalido y que ocurriera un error inesperado.
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

En esta funcion se usaron excepciones para validar que se pase como parametro una lista, ademas de que los valores sean correctos.
```python
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
```

Para esta funcion se valida con las excepciones que los valores que se le entregan esta sean correctos osea que sean cadenas.
```python
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
```

## Parte 2

- In the package Shape identify at least cases where exceptions are needed (maybe when validate input data, or math procedures) explain them clearly using comments and add them to the code.

En el paquete shape se añaden diferentes excepciones para que el codigo tenga un flujo correcto. Como se muestra en el siguiente codigo primero que todo se añade una excepcion para que los atributos x, y Point() sean numericos. En el metodo compute_distance() de la clase Point() se usa para que se calcule la distancia usando los atributos de instancia de Point().
En la clase Line se usan para validar que los puntos que usa sean instancias de Point() ademas hay otra excepcion que valida que los dos puntos sean diferentes. En la clase Triangle() se usan para validar que solo existen 3 vertices. Finalmente en cada de una de las subclases de Triangle se usan excepciones para validar que efectivamente son el tipo de triangulo que especifica la clase.
```python
class Point:
    def __init__(self, x: float = 0, y: float = 0):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Las coordenadas x e y deben ser números.")
        self.x = x
        self.y = y

    def compute_distance(self, point: "Point") -> float:
        if not isinstance(point, Point):
            raise TypeError("El argumento debe ser una instancia de Point.")
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5

class Line:
    def __init__(self, start_point: Point, end_point: Point):
        if not isinstance(start_point, Point) or not isinstance(end_point, Point):
            raise TypeError("Los puntos de inicio y fin deben ser instancias de Point.")
        if start_point.x == end_point.x and start_point.y == end_point.y:
            raise ValueError("Los puntos de inicio y fin no pueden ser iguales.")
        self.start_point = start_point
        self.end_point = end_point

    def compute_length(self) -> float:
        return self.start_point.compute_distance(self.end_point)

class Shape:
    def __init__(self, is_regular: bool = False):
        self.is_regular = is_regular
        self.vertices = []
        self.edges = []
        self.inner_angles = [] 

    def compute_area(self):
        ...

    def compute_perimeter(self):
        ...

class Rectangle(Shape):
    def __init__(self, **kwargs):
        if "center" in kwargs:
            center = kwargs["center"]
            width = kwargs["width"]
            height = kwargs["height"]
            x = center.x - width / 2
            y = center.y - height / 2
        elif "bottom_left" in kwargs and "upper_right" in kwargs:
            bottom_left = kwargs["bottom_left"]
            upper_right = kwargs["upper_right"]
            x = bottom_left.x
            y = bottom_left.y
            width = upper_right.x - bottom_left.x
            height = upper_right.y - bottom_left.y
        else:
            x = kwargs["x"]
            y = kwargs["y"]
            width = kwargs["width"]
            height = kwargs["height"]

        self.bottom_left = Point(x, y)
        self.upper_right = Point(x + width, y + height)
        self.width = width
        self.height = height

    def compute_perimeter(self):
        return 2 * (self.width + self.height)

    def compute_area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side_length: float, **kwargs):
        kwargs["width"] = side_length
        kwargs["height"] = side_length
        super().__init__(**kwargs)

class Triangle(Shape):
    def __init__(self, vertices: list[Point]):
        super().__init__(is_regular=False)
        if len(vertices) != 3:
            raise ValueError("Un triángulo debe tener exactamente 3 vértices.")
        self.vertices = vertices
        self.edges = []
        self._build_edges()

    def _build_edges(self):
        self.edges.append(Line(self.vertices[0], self.vertices[1]))
        self.edges.append(Line(self.vertices[1], self.vertices[2]))
        self.edges.append(Line(self.vertices[2], self.vertices[0]))

    def compute_perimeter(self) -> float:
        return sum(edge.compute_length() for edge in self.edges)

    def compute_area(self) -> float:
        a, b, c = [edge.compute_length() for edge in self.edges]
        s = self.compute_perimeter() / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return area

class Equilateral(Triangle):
    def __init__(self, vertices: list[Point]):
        super().__init__(vertices)
        first_length = self.edges[0].compute_length()
        if any(abs(edge.compute_length() - first_length) > 1e-9 for edge in self.edges):
            raise ValueError("Todos los lados de un triángulo equilátero deben ser iguales.")
        self.is_regular = True

class Isosceles(Triangle):
    def __init__(self, vertices: list[Point]):
        super().__init__(vertices)
        lengths = [edge.compute_length() for edge in self.edges]
        unique_lengths = set(lengths)
        if len(unique_lengths) > 2:
            raise ValueError("Un triángulo isósceles debe tener al menos dos lados iguales.")

class Scalene(Triangle):
    def __init__(self, vertices: list[Point]):
        super().__init__(vertices)
        lengths = [edge.compute_length() for edge in self.edges]
        unique_lengths = set(lengths)
        if len(unique_lengths) != 3:
            raise ValueError("Un triángulo escaleno debe tener todos los lados de diferente longitud.")

class TriRectangle(Triangle):
    def __init__(self, vertices: list[Point]):
        super().__init__(vertices)
        lengths = sorted([edge.compute_length() for edge in self.edges])
        a, b, c = lengths
        if abs(a**2 + b**2 - c**2) > 1e-9:
            raise ValueError("Un triángulo rectángulo debe cumplir el teorema de Pitágoras.")
```

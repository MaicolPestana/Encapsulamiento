# Encapsulamiento

Ejercicio 1.

Explicación:

Atributos privados:
__nombre: almacena el nombre del estudiante.
__codigo: almacena el código del estudiante.
__notas: lista para almacenar las notas.

Validaciones en @property y @setter:
nombre: no permite valores vacíos.
codigo: asegura que sea alfanumérico.

Método agregar_nota:
Permite agregar notas solo si están en el rango de 0.0 a 5.0.
Si no cumple, lanza un ValueError.

Método calcular_promedio:
Retorna el promedio de las notas almacenadas.
Si no hay notas, el promedio será 0.0.

Método es_aprobado:
Retorna True si el promedio es mayor o igual a 3.0, indicando que el estudiante está aprobado.

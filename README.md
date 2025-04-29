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


Ejercicio 2. 

Explicación del código:

Atributos privados:
__usuario: almacena el nombre del propietario de la cuenta.
__saldo_btc: almacena el saldo en BTC (inicialmente 0.0).

Métodos:
consultar_saldo: retorna el saldo actual en BTC.
comprar_btc: convierte una cantidad en USD a BTC usando el precio actual y suma el resultado al saldo.
Verifica que ambos valores sean positivos.
vender_btc: resta una cantidad de BTC del saldo y calcula el equivalente en USD.
Valida que el monto a vender no supere el saldo disponible.
Asegura que el precio y el monto sean positivos.

Validaciones:
Los métodos lanzan un ValueError si los valores proporcionados son inválidos (negativos, insuficiente saldo, etc.).


Ejercicio 3. 

Explicación del código:

Cifrado básico:
La clave se almacena cifrada en reversa (clave[::-1]) para añadir una capa de seguridad básica.
Métodos privados (__cifrar_clave y __descifrar_clave) se usan para cifrar y descifrar la clave.

Propiedades:
nombre: permite ver el nombre del empleado.
rol: permite ver el rol del empleado.
No se proporciona acceso directo para modificar la clave.

Método verificar_clave:
Compara la clave ingresada con la clave descifrada almacenada.
Método cambiar_clave:
Cambia la clave solo si la clave antigua ingresada coincide con la clave descifrada actual.


Ejercicio 4.

Explicación del código:
Clase Padre Persona:
Contiene atributos comunes (__nombre, __edad, __documento) con acceso controlado mediante @property y @setter.
Valida que la edad sea mayor a 0.

Clase Hija Paciente:
Hereda de Persona.
Añade atributos específicos (__diagnostico, __historial).
Métodos para gestionar el historial y mostrar el diagnóstico.

Clase Hija Doctor:
Hereda de Persona.
Añade un atributo para la especialidad (__especialidad).
Métodos para ver la especialidad y modificar el diagnóstico de un paciente, asegurando que solo se puede modificar si el objeto es una instancia de Paciente.



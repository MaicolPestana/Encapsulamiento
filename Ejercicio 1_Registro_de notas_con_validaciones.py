class Estudiante:
    def __init__(self, nombre, codigo):
        # Atributos privados
        self.__nombre = None
        self.__codigo = None
        self.__notas = []
        
        # Uso de setters para inicializar con validación
        self.nombre = nombre
        self.codigo = codigo

    # Propiedad para el nombre
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if valor.strip():  # Validar que no esté vacío
            self.__nombre = valor
        else:
            raise ValueError("El nombre no puede estar vacío.")

    # Propiedad para el código
    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, valor):
        if valor.isalnum():  # Validar que sea alfanumérico
            self.__codigo = valor
        else:
            raise ValueError("El código debe ser alfanumérico.")

    # Método para agregar una nota
    def agregar_nota(self, nota):
        if 0.0 <= nota <= 5.0:  # Validar que esté en el rango permitido
            self.__notas.append(nota)
        else:
            raise ValueError("La nota debe estar entre 0.0 y 5.0.")

    # Método para calcular el promedio
    def calcular_promedio(self):
        if self.__notas:  # Verificar que existan notas
            return sum(self.__notas) / len(self.__notas)
        return 0.0

    # Método para determinar si el estudiante está aprobado
    def es_aprobado(self):
        return self.calcular_promedio() >= 3.0


# Ejemplo de uso
try:
    estudiante = Estudiante("Juan Pérez", "A123")
    estudiante.agregar_nota(4.0)
    estudiante.agregar_nota(3.5)
    estudiante.agregar_nota(2.8)

    print(f"Nombre: {estudiante.nombre}")
    print(f"Código: {estudiante.codigo}")
    print(f"Promedio de notas: {estudiante.calcular_promedio():.2f}")
    print(f"¿Está aprobado? {'Sí' if estudiante.es_aprobado() else 'No'}")

except ValueError as e:
    print(f"Error: {e}")

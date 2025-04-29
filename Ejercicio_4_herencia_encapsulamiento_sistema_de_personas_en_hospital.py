class Persona:
    def __init__(self, nombre, edad, documento):
        # Atributos privados
        self.__nombre = nombre
        self.__edad = None
        self.__documento = documento

        # Validación de la edad
        self.edad = edad

    # Propiedad para el nombre
    @property
    def nombre(self):
        return self.__nombre

    # Propiedad para la edad
    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, valor):
        if valor > 0:
            self.__edad = valor
        else:
            raise ValueError("La edad debe ser mayor a 0.")

    # Propiedad para el documento
    @property
    def documento(self):
        return self.__documento


# Clase hija: Paciente
class Paciente(Persona):
    def __init__(self, nombre, edad, documento, diagnostico):
        super().__init__(nombre, edad, documento)
        # Atributos privados
        self.__diagnostico = diagnostico
        self.__historial = []

    # Método para agregar entrada al historial
    def agregar_historial(self, entrada):
        self.__historial.append(entrada)

    # Método para ver el historial completo
    def ver_historial(self):
        return self.__historial

    # Método para ver el diagnóstico
    def ver_diagnostico(self):
        return self.__diagnostico


# Clase hija: Doctor
class Doctor(Persona):
    def __init__(self, nombre, edad, documento, especialidad):
        super().__init__(nombre, edad, documento)
        # Atributo privado
        self.__especialidad = especialidad

    # Método para ver la especialidad
    def ver_especialidad(self):
        return self.__especialidad

    # Método para modificar el diagnóstico de un paciente
    def modificar_diagnostico(self, paciente, nuevo_diagnostico):
        if isinstance(paciente, Paciente):
            paciente._Paciente__diagnostico = nuevo_diagnostico
            print("Diagnóstico actualizado correctamente.")
        else:
            print("Error: Solo se puede modificar el diagnóstico de un paciente.")


# Ejemplo de uso
try:
    # Crear un paciente
    paciente1 = Paciente("Luis Gómez", 30, "12345678", "Gripe")
    paciente1.agregar_historial("Consulta inicial - 28/04/2025")
    paciente1.agregar_historial("Receta de medicamentos - 29/04/2025")

    # Crear un doctor
    doctor1 = Doctor("Dra. Ana Pérez", 45, "87654321", "Medicina General")

    # Ver datos del paciente
    print(f"Paciente: {paciente1.nombre}, Edad: {paciente1.edad}, Documento: {paciente1.documento}")
    print(f"Diagnóstico inicial: {paciente1.ver_diagnostico()}")
    print("Historial médico:", paciente1.ver_historial())

    # Modificar el diagnóstico del paciente
    doctor1.modificar_diagnostico(paciente1, "Bronquitis")
    print(f"Diagnóstico actualizado: {paciente1.ver_diagnostico()}")

    # Ver datos del doctor
    print(f"Doctor: {doctor1.nombre}, Especialidad: {doctor1.ver_especialidad()}")

except ValueError as e:
    print(f"Error: {e}")

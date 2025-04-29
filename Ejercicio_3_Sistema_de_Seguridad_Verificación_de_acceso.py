class Empleado:
    def __init__(self, nombre, rol, clave_acceso):
        # Atributos privados
        self.__nombre = nombre
        self.__rol = rol
        self.__clave_acceso = self.__cifrar_clave(clave_acceso)

    # Método para cifrar una clave (en reversa)
    def __cifrar_clave(self, clave):
        return clave[::-1]

    # Método para descifrar una clave
    def __descifrar_clave(self, clave_cifrada):
        return clave_cifrada[::-1]

    # Propiedad para ver el nombre
    @property
    def nombre(self):
        return self.__nombre

    # Propiedad para ver el rol
    @property
    def rol(self):
        return self.__rol

    # Método para verificar si la clave ingresada es correcta
    def verificar_clave(self, clave_ingresada):
        clave_descifrada = self.__descifrar_clave(self.__clave_acceso)
        return clave_ingresada == clave_descifrada

    # Método para cambiar la clave si la antigua es correcta
    def cambiar_clave(self, clave_antigua, nueva_clave):
        if self.verificar_clave(clave_antigua):
            self.__clave_acceso = self.__cifrar_clave(nueva_clave)
            print("Clave cambiada exitosamente.")
        else:
            print("La clave antigua no es correcta. No se realizó el cambio.")

# Ejemplo de uso
empleado = Empleado("Juan Pérez", "Administrador", "clave123")

# Ver propiedades del empleado
print(f"Nombre: {empleado.nombre}")
print(f"Rol: {empleado.rol}")

# Verificar clave
if empleado.verificar_clave("clave123"):
    print("La clave ingresada es correcta.")
else:
    print("La clave ingresada es incorrecta.")

# Intentar cambiar la clave
empleado.cambiar_clave("clave123", "nuevaClave456")

# Verificar con la nueva clave
if empleado.verificar_clave("nuevaClave456"):
    print("La nueva clave ingresada es correcta.")
else:
    print("La nueva clave ingresada es incorrecta.")

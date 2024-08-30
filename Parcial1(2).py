class Empleado:
    def __init__(self, nombre, anios_laborados):
        self.nombre = nombre
        self.anios_laborados = anios_laborados

    def calcular_pago(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases.")

    def calcular_bono(self):
        return 1000 if self.anios_laborados > 5 else 0


class EmpleadoPlazaFija(Empleado):
    def __init__(self, nombre, anios_laborados, salario_base, comisiones):
        super().__init__(nombre, anios_laborados)
        self.salario_base = salario_base
        self.comisiones = comisiones

    def calcular_pago(self):
        pago = self.salario_base + self.comisiones + self.calcular_bono()
        return pago


class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, anios_laborados, horas_trabajadas, tarifa_por_hora):
        super().__init__(nombre, anios_laborados)
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora

    def calcular_pago(self):
        pago = (self.horas_trabajadas * self.tarifa_por_hora) + self.calcular_bono()
        return pago


# Ejemplo de uso
def generar_planilla(empleados):
    for empleado in empleados:
        pago = empleado.calcular_pago()
        print(f"Empleado: {empleado.nombre} - Pago: ${pago:.2f}")

# Creación de instancias de empleados
empleado1 = EmpleadoPlazaFija("Carlos", 6, 1500, 300)
empleado2 = EmpleadoPorHoras("Ana", 3, 120, 15)
empleado3 = EmpleadoPlazaFija("Luis", 10, 1800, 500)
empleado4 = EmpleadoPorHoras("Marta", 7, 100, 20)

# Lista de empleados
empleados = [empleado1, empleado2, empleado3, empleado4]

# Generar planilla
generar_planilla(empleados)
                                                                                                                                                                                                                                                            
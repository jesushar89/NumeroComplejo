class NumeroComplejo:
    def __init__(self, real: float, imaginario: float):
        self.real = real
        self.imaginario = imaginario

    def __str__(self):
        return f"{self.real} + {self.imaginario}i"

    def sumar(self, otro):
        real = self.real + otro.real
        imaginario = self.imaginario + otro.imaginario
        return NumeroComplejo(real, imaginario)

    def restar(self, otro):
        real = self.real - otro.real
        imaginario = self.imaginario - otro.imaginario
        return NumeroComplejo(real, imaginario)

    def multiplicar(self, otro):
        real = self.real * otro.real - self.imaginario * otro.imaginario
        imaginario = self.real * otro.imaginario + self.imaginario * otro.real
        return NumeroComplejo(real, imaginario)

    def dividir(self, otro):
        denominador = otro.real**2 + otro.imaginario**2
        real = (self.real * otro.real + self.imaginario * otro.imaginario) / denominador
        imaginario = (self.imaginario * otro.real - self.real * otro.imaginario) / denominador
        return NumeroComplejo(real, imaginario)

# Ejemplo de uso:
complejo1 = NumeroComplejo(4, 5)
complejo2 = NumeroComplejo(2, 3)

suma = complejo1.sumar(complejo2)
resta = complejo1.restar(complejo2)
multiplicacion = complejo1.multiplicar(complejo2)
division = complejo1.dividir(complejo2)

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")

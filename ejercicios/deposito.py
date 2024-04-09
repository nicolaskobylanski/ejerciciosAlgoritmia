class CuentaDeposito:
    def __init__(self, saldo_inicial):
        # Inicializa el saldo de la cuenta con el valor inicial proporcionado
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        # Añade la cantidad depositada al saldo de la cuenta
        self.saldo += cantidad

    def retirar(self, cantidad):
        # Verifica si hay suficiente saldo antes de permitir la retirada
        if self.saldo - cantidad >= 0:
            self.saldo -= cantidad  # Resta la cantidad retirada del saldo
            return cantidad  # Devuelve la cantidad retirada
        else:
            print("No se puede retirar fondos. Saldo insuficiente.")
            return 0  # Devuelve 0 si no se puede retirar la cantidad deseada

# Subclase de CuentaDeposito que permite descubiertos
class CuentaDepositoConDescubierto(CuentaDeposito):
    def __init__(self, saldo_inicial, descubierto_autorizado):
        # Inicializa la cuenta con un saldo inicial y el descubierto autorizado
        super().__init__(saldo_inicial)
        self.descubierto_autorizado = descubierto_autorizado

    def retirar(self, cantidad):
        # Verifica si hay suficiente saldo (incluido el descubierto autorizado) antes de permitir la retirada
        if self.saldo - cantidad >= -self.descubierto_autorizado:
            self.saldo -= cantidad  # Resta la cantidad retirada del saldo
            return cantidad  # Devuelve la cantidad retirada
        else:
            print("No se puede retirar fondos. Saldo insuficiente.")
            return 0  # Devuelve 0 si no se puede retirar la cantidad deseada


def main():
    cuenta1 = CuentaDeposito(1000)
    print("Saldo inicial de cuenta1:", cuenta1.saldo)

    # Deposita 500 en la cuenta1
    cuenta1.depositar(500)
    print("Saldo después de depositar en cuenta1:", cuenta1.saldo)

    # Intenta retirar 700 de cuenta1
    cantidad_retirada = cuenta1.retirar(700)
    print("Cantidad retirada de cuenta1:", cantidad_retirada)
    print("Saldo después de retirar de cuenta1:", cuenta1.saldo)

    print("\nProbando cuenta con descubierto autorizado:")
    cuenta2 = CuentaDepositoConDescubierto(1000, 500)
    print("Saldo inicial de cuenta2:", cuenta2.saldo)

    # Deposita 300 en cuenta2
    cuenta2.depositar(300)
    print("Saldo después de depositar en cuenta2:", cuenta2.saldo)

    # Intenta retirar 2000 de cuenta2 con descubierto autorizado
    cantidad_retirada_con_descubierto = cuenta2.retirar(2000)
    print("Cantidad retirada de cuenta2 con descubierto autorizado:", cantidad_retirada_con_descubierto)
    print("Saldo después de retirar de cuenta2 con descubierto autorizado:", cuenta2.saldo)

if __name__ == "__main__":
    main()

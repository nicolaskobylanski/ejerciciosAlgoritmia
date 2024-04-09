# Definición de la función para calcular el precio con impuestos
def calcular_precio_con_impuestos(precio_sin_impuestos, porcentaje_iva):
    # Calcula los impuestos como el producto del precio sin impuestos y el porcentaje de IVA
    impuestos = precio_sin_impuestos * (porcentaje_iva / 100)
    # Suma los impuestos al precio sin impuestos para obtener el precio con impuestos
    precio_con_impuestos = precio_sin_impuestos + impuestos
    return precio_con_impuestos

# Definición de la función para calcular los intereses
def calcular_intereses(capital, tasa_interes, tiempo_meses):
    # Calcula los intereses como el producto del capital, la tasa de interés y el tiempo en meses
    intereses = capital * (tasa_interes / 100) * (tiempo_meses / 12)
    return intereses


def main():
    precio_sin_impuestos = 100
    porcentaje_iva = 21
    precio_con_impuestos = calcular_precio_con_impuestos(precio_sin_impuestos, porcentaje_iva)
    print("Precio con impuestos:", precio_con_impuestos)

    capital = 1000
    tasa_interes = 5
    tiempo_meses = 6
    intereses = calcular_intereses(capital, tasa_interes, tiempo_meses)
    print("Intereses generados:", intereses)

if __name__ == "__main__":
    main()

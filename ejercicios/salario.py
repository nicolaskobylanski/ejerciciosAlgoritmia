# Definición de la función para calcular el importe de las horas extra
def calcular_horas_extra(salario_bruto_mensual, horas_extra):
    # Calcula el salario bruto semanal
    salario_bruto_semanal = salario_bruto_mensual / 4  # Se asume que el mes tiene 4 semanas

    # Calcula el salario bruto por hora normal
    salario_bruto_hora_normal = salario_bruto_semanal / 35  # Se asume 35 horas trabajadas por semana

    # Inicializa el importe total de las horas extra
    importe_horas_extra = 0

    # Calcula el importe de las horas extra
    if horas_extra > 35:  # Si hay horas extra
        horas_extra_normales = min(horas_extra, 35)  # Se calculan como máximo 35 horas extra a la tarifa normal
        importe_horas_extra += horas_extra_normales * salario_bruto_hora_normal * 1.25  # Tarifa 125%

        if horas_extra > 43:  # Si hay más de 43 horas extra
            horas_extra_44_mas = horas_extra - 43  # Se calculan las horas restantes a la tarifa del 150%
            importe_horas_extra += horas_extra_44_mas * salario_bruto_hora_normal * 1.5

    return importe_horas_extra


def main():
    salario_bruto_mensual = 3000
    horas_extra_trabajadas = 50
    importe_horas_extra = calcular_horas_extra(salario_bruto_mensual, horas_extra_trabajadas)
    print("Importe de las horas extra:", importe_horas_extra)

if __name__ == "__main__":
    main()
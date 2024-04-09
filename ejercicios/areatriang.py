# Definición de la función para calcular el área de un triángulo dado un lado y la altura relativa a ese lado
def calcular_area_triangulo(base, altura): # SE PUEDE UTILIZAR PARA UN TRIÁNGULO RECTÁNGULO
    # Calcula el área del triángulo utilizando la fórmula: Área = (base * altura) / 2
    area = base * altura * 0.5
    return area

def main():
    base = 5
    altura = 8
    area_triangulo = calcular_area_triangulo(base, altura)
    print("Área del triángulo (base y altura):", area_triangulo)

if __name__ == "__main__":
    main()
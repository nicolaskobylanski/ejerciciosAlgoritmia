# Definición de la función para calcular la media aritmética de tres números
def calcular_media_aritmetica(num1, num2, num3):
    # Calcula la suma de los tres números y la divide entre 3 para obtener la media aritmética
    media_aritmetica = (num1 + num2 + num3) / 3
    return media_aritmetica

# Definición de la función para calcular la media ponderada
def calcular_media_ponderada(nums, ponderaciones):
    # Calcula la suma de los productos de cada número con su ponderación
    suma_productos = sum(num * ponderacion for num, ponderacion in zip(nums, ponderaciones))
    # Calcula la suma de las ponderaciones
    suma_ponderaciones = sum(ponderaciones)
    # Divide la suma de los productos entre la suma de las ponderaciones para obtener la media ponderada
    media_ponderada = suma_productos / suma_ponderaciones
    return media_ponderada

def main():
    num1 = 10
    num2 = 20
    num3 = 30
    media_aritmetica = calcular_media_aritmetica(num1, num2, num3)
    print("Media aritmética:", media_aritmetica)

    nums = [15, 25, 35]
    ponderaciones = [0.2, 0.3, 0.5]
    media_ponderada = calcular_media_ponderada(nums, ponderaciones)
    print("Media ponderada:", media_ponderada)

if __name__ == "__main__":
    main()

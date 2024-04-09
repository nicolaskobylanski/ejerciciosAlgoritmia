# Calculadora de Precios e Intereses

Este script en Python proporciona funciones para calcular el precio con impuestos y los intereses generados.

## Función `calcular_precio_con_impuestos`

Esta función calcula el precio con impuestos dados un precio sin impuestos y un porcentaje de IVA.

```python
def calcular_precio_con_impuestos(precio_sin_impuestos, porcentaje_iva):
    """
    Calcula el precio con impuestos.

    Args:
        precio_sin_impuestos (float): Precio sin impuestos.
        porcentaje_iva (float): Porcentaje de IVA.

    Returns:
        float: Precio con impuestos.
    """
    impuestos = precio_sin_impuestos * (porcentaje_iva / 100)
    precio_con_impuestos = precio_sin_impuestos + impuestos
    return precio_con_impuestos
```
# Media aritmética

Este script de Python contiene dos funciones para calcular diferentes tipos de medias: la media aritmética y la media ponderada. También incluye un ejemplo en la función `main()` para mostrar cómo usar estas funciones.

## Funciones

### `calcular_media_aritmetica(num1, num2, num3)`

Esta función toma tres números como entrada y calcula la media aritmética de esos números. La media aritmética se calcula sumando los tres números y dividiendo la suma por 3. Luego devuelve el resultado de la media aritmética.

### `calcular_media_ponderada(nums, ponderaciones)`

Esta función toma dos listas como entrada: una lista de números y una lista de ponderaciones asociadas a esos números. Calcula la media ponderada multiplicando cada número por su ponderación correspondiente, sumando los productos y dividiendo esta suma por la suma de las ponderaciones. Devuelve el resultado de la media ponderada.

## Ejemplo de Uso

El script incluye un ejemplo en la función `main()` que muestra cómo usar las funciones definidas anteriormente.

1. Se definen tres números (`num1`, `num2`, `num3`) y se llama a la función `calcular_media_aritmetica()` con estos números. Luego se imprime la media aritmética calculada.

2. Se definen dos listas: `nums`, que contiene los números `[15, 25, 35]`, y `ponderaciones`, que contiene las ponderaciones `[0.2, 0.3, 0.5]`. Se llama a la función `calcular_media_ponderada()` con estas listas y se imprime la media ponderada calculada.

# Área del triángulo

Este script de Python contiene una función para calcular el área de un triángulo dada la longitud de uno de sus lados (base) y la altura relativa a ese lado. También incluye un ejemplo en la función `main()` para mostrar cómo usar esta función.

## Función

### `calcular_area_triangulo(base, altura)`

Esta función toma dos parámetros: la longitud de la base del triángulo y la altura relativa a esa base. Utiliza la fórmula estándar del área de un triángulo, que es el producto de la base y la altura dividido por 2 (Área = base * altura / 2). Devuelve el área calculada del triángulo.

## Ejemplo de Uso

El script incluye un ejemplo en la función `main()` que muestra cómo usar la función `calcular_area_triangulo()`.

1. Se define la longitud de la base (`base`) y la altura (`altura`) del triángulo.

2. Se llama a la función `calcular_area_triangulo()` con estos parámetros y se asigna el resultado a la variable `area_triangulo`.

3. Se imprime el resultado del cálculo del área del triángulo.

# Calculadora de salarios

Este script de Python contiene una función para calcular el importe de las horas extra trabajadas, dadas ciertas condiciones de salario y horas de trabajo. También incluye un ejemplo en la función `main()` para mostrar cómo usar esta función.

## Función

### `calcular_horas_extra(salario_bruto_mensual, horas_extra)`

Esta función toma dos parámetros: el salario bruto mensual del trabajador y el número de horas extra trabajadas en un mes. Calcula el importe total de las horas extra utilizando una lógica específica:

1. Calcula el salario bruto semanal dividiendo el salario bruto mensual entre 4, asumiendo que el mes tiene 4 semanas laborales.
2. Calcula el salario bruto por hora normal dividiendo el salario bruto semanal entre 35, asumiendo que se trabajan 35 horas por semana.
3. Inicializa el importe total de las horas extra en 0.
4. Calcula el importe de las horas extra según las siguientes condiciones:
   - Si el número de horas extra es mayor que 35, se calculan como máximo 35 horas extra a la tarifa normal y se añaden al importe total.
   - Si hay más de 43 horas extra, se calculan las horas restantes a una tarifa del 150% y se añaden al importe total.
   
Finalmente, devuelve el importe total de las horas extra calculadas.

## Ejemplo de Uso

El script incluye un ejemplo en la función `main()` que muestra cómo usar la función `calcular_horas_extra()`.

1. Se define el salario bruto mensual (`salario_bruto_mensual`) y el número de horas extra trabajadas (`horas_extra_trabajadas`).
2. Se llama a la función `calcular_horas_extra()` con estos parámetros y se asigna el resultado a la variable `importe_horas_extra`.
3. Se imprime el importe total de las horas extra calculadas.

# Cuenta de Depósito

Este script de Python define una clase `CuentaDeposito` y una subclase `CuentaDepositoConDescubierto`. Estas clases modelan cuentas de depósito bancario con funciones para depositar y retirar fondos. La clase `CuentaDepositoConDescubierto` extiende la funcionalidad de `CuentaDeposito` al permitir descubiertos en la cuenta.

## Clases

### `CuentaDeposito`

Esta clase representa una cuenta de depósito bancario estándar. Contiene los siguientes métodos:

- `__init__(self, saldo_inicial)`: Inicializa el saldo de la cuenta con el valor proporcionado.
- `depositar(self, cantidad)`: Añade la cantidad depositada al saldo de la cuenta.
- `retirar(self, cantidad)`: Verifica si hay suficiente saldo antes de permitir la retirada. Si hay suficiente saldo, se resta la cantidad retirada del saldo y se devuelve la cantidad retirada. Si no hay suficiente saldo, se imprime un mensaje de saldo insuficiente y se devuelve 0.

### `CuentaDepositoConDescubierto`

Esta es una subclase de `CuentaDeposito` que permite descubiertos en la cuenta. Hereda todos los métodos de `CuentaDeposito` y redefine el método `retirar(self, cantidad)` para tener en cuenta el descubierto autorizado. Siempre y cuando la cantidad a retirar no exceda el saldo disponible más el descubierto autorizado, la operación de retiro se lleva a cabo con éxito. De lo contrario, se imprime un mensaje de saldo insuficiente y no se realiza la operación de retiro.

## Ejemplo de Uso

El script incluye un ejemplo en la función `main()` que muestra cómo usar estas clases.

1. Se crea una instancia de `CuentaDeposito` con un saldo inicial de 1000 y se realizan operaciones de depósito y retiro.
2. Se crea una instancia de `CuentaDepositoConDescubierto` con un saldo inicial de 1000 y un descubierto autorizado de 500. Se realizan operaciones de depósito y retiro, incluyendo una retirada que excede el saldo actual pero no el descubierto autorizado.








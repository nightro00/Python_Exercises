#Fibonacci
"""
/*
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 */
"""

def fibonacci(num):
    fibonacci_list = []

    if len(fibonacci_list) == 0:
        fibonacci_list.append(1)
    
    for i in range(num + 1):
        sumatoria_numeros = fibonacci_list[i - 1] + fibonacci_list[i]
        fibonacci_list.append(sumatoria_numeros)

    return fibonacci_list

print(fibonacci(10))
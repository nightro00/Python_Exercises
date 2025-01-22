#AREA POLIGONO
"""
/*
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 */
"""

def area_poligono(tipo_poligono, base = 0, altura = 0, lado = 0): 
    if tipo_poligono == "triangulo":
        return f"El area es {(base * altura) / 2}"
    elif tipo_poligono == "cuadrado":
        return f"El area es {(lado ** 2)}"
    elif tipo_poligono == "rectangulo":
        return f"El area es {(base * altura)}"
    else:
        return f"Este poligono no esta implementado"
    
print(area_poligono("cuadrado", 0, 0, 2))
### Challenges ###
#PRIMO
"""
/*
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */
"""
def numero_primos(num):
    count_num = 2
    no_primos_list = []

    while (count_num <= num):
        for n in range(2, num + 1):
            if count_num % n == 0 and n != count_num:
                print(f"{count_num} - no es primo")
                no_primos_list.append(count_num)
                break
        if not count_num in no_primos_list:   
            print(f"{count_num} - es primo")
        count_num += 1

            
#numero_primos(10)

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
    
#print(area_poligono("cuadrado", 0, 0, 2))

#ASPECT RATIO IMAGEN
"""
/*
 * Crea un programa que se encargue de calcular el aspect ratio de una
 * imagen a partir de una url.
 * - Url de ejemplo:
 *   https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png
 * - Por ratio hacemos referencia por ejemplo a los "16:9" de una
 *   imagen de 1920*1080px.
 */"""

#INVIRTIENDO CADENAS
"""
/*
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
 */"""

def invirtiendo_cadena(word):
    print(word[::-1])   

#invirtiendo_cadena("Hola mundo")

#CONTANDO PALABRAS

"""
/*
 * Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que
 *   lo resuelvan automáticamente.
 */
"""

def contando_palabras(paragraph):

    paragraph_list = paragraph.replace(".", "").replace(",", "").replace("\'", "").split(" ")

    for word in paragraph_list:
        count_word = 0
        for word2 in paragraph_list:
            if word == word2:
                count_word = count_word + 1
        print(f"{word} - {count_word}")

#print(contando_palabras("Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen. No sólo sobrevivió 500 años, sino que tambien ingresó como texto de relleno en documentos electrónicos, quedando esencialmente igual al original. Fue popularizado en los 60s con la creación de las hojas 'Letraset', las cuales contenian pasajes de Lorem Ipsum, y más recientemente con software de autoedición, como por ejemplo Aldus PageMaker, el cual incluye versiones de Lorem Ipsum."))

#DECIMAL A BINARIO
"""
/*
 * Crea un programa se encargue de transformar un número
 * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
 */
"""
def decimal_binario(num):
    new_num = num
    par_impar_list = []

    while(new_num > 1):
        if(new_num == num and new_num % 2 == 0):
            par_impar_list.append(0)
        elif(new_num == num and new_num % 2 != 0):
            par_impar_list.append(1)

        new_num = int(new_num / 2)
        if(new_num % 2 == 0):
            par_impar_list.append(0)
        elif(new_num % 2 != 0):
            par_impar_list.append(1)

    return par_impar_list
        

#print(decimal_binario(420)[::-1])

#CODIGO MORSE

"""
    /*
 * Crea un programa que sea capaz de transformar texto natural a código
 * morse y viceversa.
 * - Debe detectar automáticamente de qué tipo se trata y realizar
 *   la conversión.
 * - En morse se soporta raya "—", punto ".", un espacio " " entre letras
 *   o símbolos y dos espacios entre palabras "  ".
 * - El alfabeto morse soportado será el mostrado en
 *   https://es.wikipedia.org/wiki/Código_morse.
 */
"""
global dictionary_morse

dictionary_morse = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--." ,"H": "....", "I" : "..", "J": ".---", "K" : "-.-", "L" : ".-..", "M" : "--", "N" : "-.", "Ñ" : "--.--", "O": "---", "P": ".--.", "Q" : "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--","X" : "-..-", "Y": "-.-", "Z": "--.."}

def codigo_morse(words):
    morse_list = []
    for word in words:
        for morse in dictionary_morse.keys():
            if word.lower() == morse.lower():
                morse_list.append(dictionary_morse[morse])
                break

    return morse_list

#print(codigo_morse("El código Morse fue desarrollado para usar el telégrafo, un dispositivo ideado también por Samuel Morse en 1832"))

#EXPRESIONES EQUILIBRADAS

"""
/*
 * Crea un programa que comprueba si los paréntesis, llaves y corchetes
 * de una expresión están equilibrados.
 * - Equilibrado significa que estos delimitadores se abren y cieran
 *   en orden y de forma correcta.
 * - Paréntesis, llaves y corchetes son igual de prioritarios.
 *   No hay uno más importante que otro.
 * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
 * - Expresión no balanceada: { a * ( c + d ) ] - 5 }
 */
"""

#def equilibrado(expression):

#ELIMINANDO CARACTERES

""" 
/*
 * Crea una función que reciba dos cadenas como parámetro (str1, str2)
 * e imprima otras dos cadenas como salida (out1, out2).
 * - out1 contendrá todos los caracteres presentes en la str1 pero NO
 *   estén presentes en str2.
 * - out2 contendrá todos los caracteres presentes en la str2 pero NO
 *   estén presentes en str1.
 */ 
"""

def eliminando_caracteres(str1, str2):
    str1_list = []
    str2_list = []

    for s1 in str1:
        for s2 in str2:
            if not s1 in str2:
                str1_list.append(s1)
                break

    for s2 in str2:
        for s1 in str1:
            if not s2 in str1:
                str2_list.append(s2)
                break

    return f"{str1_list} {str2_list}"

#print(eliminando_caracteres("word1s", "word2x"))

#PALINDROMO

"""
/*
 * Escribe una función que reciba un texto y retorne verdadero o
 * falso (Boolean) según sean o no palíndromos.
 * Un Palíndromo es una palabra o expresión que es igual si se lee
  * de izquierda a derecha que de derecha a izquierda.
 * NO se tienen en cuenta los espacios, signos de puntuación y tildes.
 * Ejemplo: Ana lleva al oso la avellana.
 */
"""

def palindromo(word):

    if word.lower() != word[::-1].lower():
        return False

    return True

#print(palindromo("ana"))

#Factorial

"""
/*
 * Escribe una función que calcule y retorne el factorial de un número dado
 * de forma recursiva.
 */
"""

def factorial(num):
    total = 0

    for i in range(1, num):
        total += num * i
    return total

#print(factorial(4))

#Numero ARMSTRONG

"""
/*
 * Escribe una función que calcule si un número dado es un número de Armstrong
 * (o también llamado narcisista).
 * Si no conoces qué es un número de Armstrong, debes buscar información
 * al respecto.
 */
"""

def armstrong(num):
    total = 0
    for i in range(0, len(num)):
        total = total + (int(num[i]) ** 3)
    
    if total == int(num):
        return f"El numero {num} es un numero armstrong"
    else:
        return f"El numero {num} no es un numero armstrong"

#print(armstrong("153"))


#CUANTOS DIAS

"""
/*
 * Crea una función que calcule y retorne cuántos días hay entre dos cadenas
 * de texto que representen fechas.
 * - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
 * - La función recibirá dos String y retornará un Int.
 * - La diferencia en días será absoluta (no importa el orden de las fechas).
 * - Si una de las dos cadenas de texto no representa una fecha correcta se
 *   lanzará una excepción.
 */
"""

from datetime import datetime

global date_to_str

def cantidad_dias(date1, date2):
    date_format = "%Y/%m/%d"
    try:
        diferencia = datetime.strptime(date1, date_format) - datetime.strptime(date2, date_format)
        return f"la diferencia de dias es: {diferencia}"
    except ValueError as Error:
        print("A value error is raised because:", Error)

#print(cantidad_dias("2024/01/01", "2024/02/01"))

#EN MAYUSCULA

"""
/*
 * Crea una función que reciba un String de cualquier tipo y se encargue de
 * poner en mayúscula la primera letra de cada palabra.
 * - No se pueden utilizar operaciones del lenguaje que
 *   lo resuelvan directamente.
 */
"""

def primera_leta_mayuscula(pos_word):
    word_list = pos_word.split(" ")
    new_word_list = []
    
    delimiter = " "
    try:
        for pos_word in range(len(word_list)):
            temp_word_list = word_list[pos_word]

            for pos_letra in temp_word_list:
                new_word_list.append(temp_word_list[0].upper() + temp_word_list[1:])
                break
        
        string_list = [str(new_word) for new_word in new_word_list]
        result_string = delimiter.join(string_list)

        return result_string     
    except ValueError as Error:
        print("A value error is raised because:", Error)

#print(primera_leta_mayuscula("hola mi nombre es jose julio."))

#Cadena Ostaculos

"""
/*
 * Crea una función que evalúe si un/a atleta ha superado correctamente una
 * carrera de obstáculos.
 * - La función recibirá dos parámetros:
 *      - Un array que sólo puede contener String con las palabras
 *        "run" o "jump"
 *      - Un String que represente la pista y sólo puede contener "_" (suelo)
 *        o "|" (valla)
 * - La función imprimirá cómo ha finalizado la carrera:
 *      - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla)
 *        será correcto y no variará el símbolo de esa parte de la pista.
 *      - Si hace "jump" en "_" (suelo), se variará la pista por "x".
 *      - Si hace "run" en "|" (valla), se variará la pista por "/".
 * - La función retornará un Boolean que indique si ha superado la carrera.
 * Para ello tiene que realizar la opción correcta en cada tramo de la pista.
 */
"""

#TRES EN RAYA

"""
/*
 * Crea una función que analice una matriz 3x3 compuesta por "X" y "O"
 * y retorne lo siguiente:
 * - "X" si han ganado las "X"
 * - "O" si han ganado los "O"
 * - "Empate" si ha habido un empate
 * - "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta.
 *   O si han ganado los 2.
 * Nota: La matriz puede no estar totalmente cubierta.
 * Se podría representar con un vacío "", por ejemplo.
 */"""

def tres_en_raya_recursiva(array):
    for pos_row in range(len(array)):

        count_x = 0   
        count_o = 0
        for pos_col in range(len(array[0])):
            if array[pos_col][pos_row] == "X":
                count_x += 1
            elif array[pos_col][pos_row] == "O":
                count_o += 1
            
            if count_x == 3:
                return f" 'X' ha ganado en la columna"
            elif count_o == 3:
                return f" 'O' ha ganado en la columna"

def tres_en_raya_oblicuas(array):

    for pos_row in range(len(array)):

        count_x = 0   
        count_o = 0

        pos_x_oblicuo = 0
        pos_o_oblicuo = 0

        pos_x_neg_oblicuo = 2
        pos_O_neg_oblicuo = 2
        for pos_col in range(len(array[0])):
            if pos_row + pos_x_oblicuo != 3:
                if array[pos_col][pos_row + pos_x_oblicuo] == "X":
                    count_x += 1
                    pos_x_oblicuo += 1
            if pos_row + pos_o_oblicuo != 3:
                if array[pos_col][pos_row + pos_o_oblicuo] == "O":
                    count_o += 1
                    pos_o_oblicuo += 1

            if pos_row + pos_x_neg_oblicuo >= 0:
                if array[pos_col][pos_row + pos_x_neg_oblicuo] == "X":
                    count_x += 1
                pos_x_neg_oblicuo -= 1
            if pos_row + pos_O_neg_oblicuo >= 0:
                if array[pos_col][pos_row + pos_O_neg_oblicuo] == "O":
                    count_o += 1
                pos_O_neg_oblicuo -= 1

            if count_x == 3:
                return f" 'X' ha ganado oblicuo"
            elif count_o == 3:
                return f" 'O' ha ganado oblicuo"
            
def tres_en_raya(array):
    
    for pos_row in range(len(array)):
        if array[pos_row].count(" ") > 0:
            return f" Hay valores vacios, por favor juegue."

    for pos_row in range(len(array)):
        if array[pos_row].count("X") == 3:
            return f" 'X' ha ganado en la fila"
        elif array[pos_row].count("O") == 3:
            return f" 'O' ha ganado en la fila"
        
    result_columna = tres_en_raya_recursiva(array)   

    if result_columna == None:
        return tres_en_raya_oblicuas(array)
    return result_columna
        
    

#print(tres_en_raya([["O", "O", "X"], ["X", "X", "O"], ["X", "O", "O"]]))
#print(tres_en_raya([["X", "O", "X"], ["O", "X", "O"], ["O", "O", "X"]]))
#print(tres_en_raya([["O", "O", "O"], ["O", "X", "X"], ["O", "X", "X"]]))
#print(tres_en_raya([["X", "O", "X"], ["X", "X", "O"], ["X", "X", "X"]]))
#print(tres_en_raya([[" ", "O", "X"], ["X", "X", "O"], ["X", "X", "X"]]))

#CONVERSOR DE TIEMPO

"""
/*
 * Crea una función que reciba días, horas, minutos y segundos (como enteros)
 * y retorne su resultado en milisegundos.
 */
"""

def conversor_tiempo(dias, horas, minutos, segundos):
    try:    
        tiempo_total = 0

        tiempo_total = segundos * 1000
        tiempo_total = minutos * 60 * 1000
        tiempo_total = horas * 60 * 60 * 1000
        tiempo_total = dias * 24 * 60 * 60 * 1000
        
        return f"La cantidad de milisegundo es: ", tiempo_total
    except ValueError as Error:
        return f"{Error}"
    
#print(conversor_tiempo(1, 0, 0, 0))

#PARANDO EL TIEMPO

"""
/*
 * Crea una función que sume 2 números y retorne su resultado pasados
 * unos segundos.
 * - Recibirá por parámetros los 2 números a sumar y los segundos que
 *   debe tardar en finalizar su ejecución.
 * - Si el lenguaje lo soporta, deberá retornar el resultado de forma
 *   asíncrona, es decir, sin detener la ejecución del programa principal.
 *   Se podría ejecutar varias veces al mismo tiempo.
 */
"""

import asyncio
#from timer import Timer

async def async_sumar(num1, num2):
    t = Timer()
    t.start()
    suma = 0
    suma = num1 + num2
    await asyncio.sleep(0.5)
    
    print(f"Suma en {t.stop()} seconds")

    return suma

#print(async_sumar(115252525, 22525252))

#CALCULADORA

"""
/*
 * Lee el fichero "Challenge21.txt" incluido en el proyecto, calcula su
 * resultado e imprímelo.
 * - El .txt se corresponde con las entradas de una calculadora.
 * - Cada línea tendrá un número o una operación representada por un
 *   símbolo (alternando ambos).
 * - Soporta números enteros y decimales.
 * - Soporta las operaciones suma "+", resta "-", multiplicación "*"
 *   y división "/".
 * - El resultado se muestra al finalizar la lectura de la última
 *   línea (si el .txt es correcto).
 * - Si el formato del .txt no es correcto, se indicará que no se han
 *   podido resolver las operaciones.
 */
"""
global count_num, count_operator, num_listm, operator_list
count_num = 0
count_operator = 0
num_list = []
operator_list = []

def read_path(path):
    file = open(path, "r")

    content = file.read()
    file.close()

    return calculate(content)

def  calculate(content):
    delimiter = ""
    total = 0

    contains_num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9] 

    try:
        operatior_list = [str(line) for line in content.split("\n")]

        result_operation_list = delimiter.join(operatior_list)
        
        for pos_value in range(len(result_operation_list)):
            if type(result_operation_list[pos_value]) in contains_num_list and pos_value == 0:
                total = result_operation_list[pos_value]
            else:
                if result_operation_list[pos_value - 1] == "+":
                    total = total + int(result_operation_list[pos_value]) 
                elif result_operation_list[pos_value - 1] == "-":
                    total = total - int(result_operation_list[pos_value])
                elif result_operation_list[pos_value - 1] == "*":
                    total = total * int(result_operation_list[pos_value])
                elif result_operation_list[pos_value - 1] == "/":
                    total = total / int(result_operation_list[pos_value])
        return f"El resultado es: {total}"

    except ValueError as Error:
        print(f"The error raises was ", Error)

#print(read_path("Ejercicios Intermedio/Challenge21.txt"))

#CONJUNTOS

"""
/*
 * Crea una función que reciba dos array, un booleano y retorne un array.
 * - Si el booleano es verdadero buscará y retornará los elementos comunes
 *   de los dos array.
 * - Si el booleano es falso buscará y retornará los elementos no comunes
 *   de los dos array.
 * - No se pueden utilizar operaciones del lenguaje que
 *   lo resuelvan directamente.
 */
"""
def elemen_comunes(arr1, arr2):

    elemen_comunes_list = []

    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j]:
                elemen_comunes_list.append(arr1[i])
                break
    return elemen_comunes_list

def elemen_no_comunes(arr1, arr2):

    elemen_no_comunes_list = []
    count_elemen_bool = False

    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] != arr2[j]:
                count_elemen_bool = True
            else:
                count_elemen_bool = False
    if(count_elemen_bool):
        elemen_no_comunes_list.append(arr1[i])
    return elemen_no_comunes_list

def conjunto(arr1, arr2, boolean):
    
    if boolean:
        result = elemen_comunes(arr1, arr2)
    else:
        result = elemen_no_comunes(arr1, arr2)

    return result
    
#print(conjunto([1, 2, 3, 4], [1, 2, 3, 5], True))
#print(conjunto([1, 2, 3, 4], [1, 2, 3, 5], False))

#MAXIMO COMUN DIVISOR Y MINIMO COMUN MULTIPLO
"""
/*
 * Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra
 * que calcule el mínimo común múltiplo (mcm) de dos números enteros.
 * - No se pueden utilizar operaciones del lenguaje que
 *   lo resuelvan directamente.
 */
"""
def mcd_mcm_final(arr1, arr2):
    resultado_list = []
    for arr_value in arr1:
        if arr2.count(arr_value):
            resultado_list.append(arr_value)
    return resultado_list

def mcd(num1, num2, operation):
    divisor_comun_list1 = []
    divisor_comun_list2 = []

    divisor_comun = []

    for value in range(1, num1):
        if num1 % value == 0:
            divisor_comun_list1.append(value)
    
    for value in range(1, num2):
        if num2 % value == 0:
            divisor_comun_list2.append(value)

    if operation == "mcd":
        if len(divisor_comun_list1) > len(divisor_comun_list2):
            return f"El maximo comun divisor es: {max(mcd_mcm_final(divisor_comun_list1, divisor_comun_list2))}"
        else :
            if len(divisor_comun_list1) < len(divisor_comun_list2):
                return f"El maximo comun divisor es: {max(mcd_mcm_final(divisor_comun_list2, divisor_comun_list1))}"
            else :
                return f"El maximo comun divisor es: {max(mcd_mcm_final(divisor_comun_list1, divisor_comun_list2))}"


#print(mcd(6, 8, "mcd"))

def mcm(num1, num2, operation):
    multiplo_comun_list1 = []
    multiplo_comun_list2 = []

    divisor_comun = []

    for value in range(1, 12):
        multiplo_comun_list1.append(num1 * value)
    
    for value in range(1, 12):
         multiplo_comun_list2.append(num2 * value)

    if operation == "mcm":
        if len(multiplo_comun_list1) > len(multiplo_comun_list2):
            return f"El minimo comun multiplo es: {min(mcd_mcm_final(multiplo_comun_list1, multiplo_comun_list2))}"
        else :
            if len(multiplo_comun_list1) < len(multiplo_comun_list2):
                return f"El minimo comun multiplo es: {min(mcd_mcm_final(multiplo_comun_list2, multiplo_comun_list1))}"
            else :
                return f"El minimo comun multiplo es: {min(mcd_mcm_final(multiplo_comun_list1, multiplo_comun_list2))}"
            
#print(mcm(2, 3, "mcm"))

#Iteration MASTER

"""
/*
 * Quiero contar del 1 al 100 de uno en uno (imprimiendo cada uno).
 * ¿De cuántas maneras eres capaz de hacerlo?
 * Crea el código para cada una de ellas.
 */
"""
for i in range(1, 101):
    i
    #print(i)


#PIEDRA, PAEPL, TIJERA

"""
/*
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "R" (piedra), "P" (papel)
 *   o "S" (tijera).
 * - Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2".
 */
"""

def ganador(arr):
    Player1_count = 0
    Player2_count = 0

    count_num = 0
    
    while(count_num < len(arr)) :
        if arr[count_num][0].count("R") and arr[count_num][1].count("S") :
            Player1_count += 1
        else:
            if arr[count_num][0].count("P") and arr[count_num][1].count("R") :
                Player1_count += 1
            elif arr[count_num][0].count("S") and arr[count_num][1].count("P") :
                Player1_count += 1
            else :
                if arr[count_num][1].count("R") and arr[count_num][0].count("S") :
                    Player2_count += 1
                else:
                    if arr[count_num][1].count("P") and arr[count_num][0].count("R") :
                        Player2_count += 1
                    elif arr[count_num][1].count("S") and arr[count_num][0].count("P") :
                        Player2_count += 1
                    else :
                        count_num += 1
                        continue
        count_num += 1

    if Player1_count > Player2_count :
        return f"Player 1"
    else :
        if Player2_count > Player1_count :
            return f"Player 2"
        else :
            return f"Tie"
        
#print(ganador([("R","S"), ("S","R"), ("P","S")]))
#print(ganador([("R","S"), ("P","R"), ("P","S")]))
#print(ganador([("R","R"), ("P","P"), ("S","S")]))

#Cuadraro y triangulo 2D

"""
    /*
 * Crea un programa que dibuje un cuadrado o un triángulo con asteriscos "*".
 * - Indicaremos el tamaño del lado y si la figura a dibujar es una u otra.
 * - EXTRA: ¿Eres capaz de dibujar más figuras?
 */
"""

def dibujo_2d(valor):
    if valor == "cuadrado":
        for i in range(1, 5):
            for j in range(0, 5):
                print("*", end = " ")
            print("\n")
    elif valor == "triangulo":
        for i in range(1, 5):
            for j in range(0, i):
                print(i * "*")
                break
            
            
#dibujo_2d("triangulo")

#VECTORES ORTOGONALES

"""
/*
 * Crea un programa que determine si dos vectores son ortogonales.
 * - Los dos array deben tener la misma longitud.
 * - Cada vector se podría representar como un array. Ejemplo: [1, -2]
 */
"""

#MAQUINA EXPENDEDORA

"""
/*
 * Simula el funcionamiento de una máquina expendedora creando una operación
 * que reciba dinero (array de monedas) y un número que indique la selección
 * del producto.
 * - El programa retornará el nombre del producto y un array con el dinero
 *   de vuelta (con el menor número de monedas).
 * - Si el dinero es insuficiente o el número de producto no existe,
 *   deberá indicarse con un mensaje y retornar todas las monedas.
 * - Si no hay dinero de vuelta, el array se retornará vacío.
 * - Para que resulte más simple, trabajaremos en céntimos con monedas
 *   de 5, 10, 50, 100 y 200.
 * - Debemos controlar que las monedas enviadas estén dentro de las soportadas.
 */
"""

global producto_dictionary
producto_dictionary = {}

class Maquina_Expendedora:
    def __init__(self, money, *option):
        self.money = money
        self.option = option

    def product(self):
        producto_dictionary = {
            "meat" : 9.95,
            "cheese": 11.50,
            "fish": 7.00,
            "chicken": 8.95,
            "carror": 4.60,
            "banana": 3.70,
            "wine": 8.25,
            "apple": 5.95,
            "milk": 1.30
        }

        self.producto_dictionary = producto_dictionary

    def buy_product(self):
        total = 0

        for pos in range(len(self.producto_dictionary)):
            if pos >= len(self.option):
                    break
            elif self.money < self.producto_dictionary[self.option[pos]] :
                return f"Insufficiente money."
            else :
                if self.option[pos] in self.producto_dictionary:
                    total = self.money - self.producto_dictionary[self.option[pos]]
                    self.money = total
        print(total % 100)
        print(total % 50)
        print(total % 10)
        print(total % 5)
        return total

My_products = Maquina_Expendedora(100, "meat", "cheese", "fish")
My_products.product()
#print(My_products.buy_product())

#ORDENA LA LISTA

"""
/*
 * Crea una función que ordene y retorne una matriz de números.
 * - La función recibirá un listado (por ejemplo [2, 4, 6, 8, 9]) y un parámetro
 *   adicional "Asc" o "Desc" para indicar si debe ordenarse de menor a mayor
 *   o de mayor a menor.
 * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan
 *   automáticamente.
 */
"""
import random
global orden_list

def recursive_min(arr_num, random_num, orden_list):

    for orden in orden_list:
        if orden in arr_num:
            arr_num.remove(orden)

    for num in arr_num:
        if num < random_num :
            random_num = num

    orden_list.append(random_num)
    
    return orden_list

def recursive_max(arr_num, random_num, orden_list):

    for orden in orden_list:
        if orden in arr_num:
            arr_num.remove(orden)

    for num in arr_num:
        if num > random_num :
            random_num = num

    orden_list.append(random_num)
    
    return orden_list

def ordenar(arr_num, tipo_orden):
    orden_list = []
    arr_size = len(arr_num)
    new_arr_num = []
    new_arr_num2 = []

    count_arr = 1
    count_arr2 = 10
    if tipo_orden == "Asc":
        while(count_arr <= arr_size) :
            random_num = random.randrange(count_arr, 10)
            new_arr_num = recursive_min(arr_num, random_num, orden_list)
            count_arr += 1
    elif tipo_orden == "Desc"  :
        while(count_arr2 > 1) :
            random_num = random.randrange(1, count_arr2)
            new_arr_num2 = recursive_max(arr_num, random_num, orden_list)
            count_arr2 -= 1
    return f"Asc: {new_arr_num} - Desc{new_arr_num2}"

def ordenar_lista(arr, tipo_orden):
    if tipo_orden == "Asc" :
        return ordenar(arr, tipo_orden)
    elif tipo_orden == "Desc" :
        return ordenar(arr, tipo_orden)

#print(ordenar_lista([9, 5, 4, 8, 7, 3, 6, 1, 2], "Asc"))
#print(ordenar_lista([9, 5, 4, 8, 7, 3, 6, 1, 2], "Desc"))

#MARCO DE PALABRAS

"""
/*
 * Crea una función que reciba un texto y muestre cada palabra en una línea,
 * formando un marco rectangular de asteriscos.
 * - ¿Qué te parece el reto? Se vería así:
 *   **********
 *   * ¿Qué   *
 *   * te     *
 *   * parece *
 *   * el     *
 *   * reto?  *
 *   **********
 */
"""

def marco(textos):
    
    for texto in textos.split(" ") :
        print(f"* {texto} *")

#marco("¿Qué te parece el reto?")

#Anio Bisiesto

"""
/*
 * Crea una función que imprima los 30 próximos años bisiestos
 * siguientes a uno dado.
 * - Utiliza el menor número de líneas para resolver el ejercicio.
 */
"""

def bisiesto(*years):

    for year in years:
        if year % 400 == 0 :
            print(f"{year} - Bisiesto")
        elif year % 4 == 0 and year % 100 != 0:
            print(f"{year} - Bisiesto")
        else:
            print(f"{year} - No Bisiesto")
        
#bisiesto(2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029)

#El segundo

"""
/*
 * Dado un listado de números, encuentra el SEGUNDO más grande
 */
"""
#print(ordenar_lista([9, 5, 4, 8, 7, 3, 6, 1, 2], "Asc"))

#Ciclo SEXAGENARIO CHINO

"""
/*
 * Crea un función, que dado un año, indique el elemento 
 * y animal correspondiente en el ciclo sexagenario del zodíaco chino.
 * - Info: https://www.travelchinaguide.com/intro/astrology/60year-cycle.htm
 * - El ciclo sexagenario se corresponde con la combinación de los elementos
 *   madera, fuego, tierra, metal, agua y los animales rata, buey, tigre,
 *   conejo, dragón, serpiente, caballo, oveja, mono, gallo, perro, cerdo
 *   (en este orden).
 * - Cada elemento se repite dos años seguidos.
 * - El último ciclo sexagenario comenzó en 1984 (Madera Rata).
 */
"""
import csv

def ciclo_sexagenario():
    fields = []
    rows = []
    path = "Ejercicios Intermedio/ciclo_chino.csv"

    with open(path, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            rows.append(row)

    return rows
    
class Sexagenario_Chino:
    def __init__(self):
        pass
    def __init__(self, Count, Branch, Gregorian_Year, Zodiac_Sign, WuXing):
        self.count = Count
        self.Branch = Branch
        self.GregorianYear = Gregorian_Year
        self.Zodiac_sign = Zodiac_Sign
        self.WuXing = WuXing

    
    def sexagenario_dictionary(self):
        Sexagenario_Chino_dictionary = {
            "Branch" + "_" + self.count: self.Branch,
            "Gregorian_Year" + "_" + self.count: self.GregorianYear,
            "Zodiac_Sign" + "_" + self.count: self.Zodiac_sign,
            "WuXing" + "_" + self.count: self.WuXing
        }

        self.Sexagenario_Chino_dictionary = Sexagenario_Chino_dictionary
        return Sexagenario_Chino_dictionary

    def search_element_animal(self,pos, year_to_search):
        Gregorian_Year = "Gregorian_Year_" + str(pos + 1)
        if self.Sexagenario_Chino_dictionary[Gregorian_Year] == str(year_to_search):
            return self.Sexagenario_Chino_dictionary

year_to_search = 1985
rows_result = ciclo_sexagenario()
"""
my_sexagenario_chino_list = list()
for pos_row in range(len(rows_result)):
    my_sexagenario_chino_list.append(Sexagenario_Chino(rows_result[pos_row][0], rows_result[pos_row][1], rows_result[pos_row][2], rows_result[pos_row][3], rows_result[pos_row][4]))


for obj in my_sexagenario_chino_list:
    obj.sexagenario_dictionary()

for pos in range(len(my_sexagenario_chino_list)):
    dictionary_result = my_sexagenario_chino_list[pos].search_element_animal(pos, 1925)
    if dictionary_result != None:
        print(dictionary_result)
        break 
"""

#LOS NUMEROS PERDIDOS

"""
/*
 * Dado un array de enteros ordenado y sin repetidos,
 * crea una función que calcule y retorne todos los que faltan entre
 * el mayor y el menor.
 * - Lanza un error si el array de entrada no es correcto.
 */
"""

def numeros_perdidos(arr):
    count_num = 1
    new_arr = []

    while count_num <= len(arr):
        if arr.count(count_num) == 0:
            new_arr.append(count_num)
        count_num += 1
    return f"Lost numeros faltantes son: {new_arr}"

#print(numeros_perdidos([1, 3, 5, 6, 7, 8, 9]))

#BATALLA POKEMON

"""
/*
 * Crea un programa que calcule el daño de un ataque durante
 * una batalla Pokémon.
 * - La fórmula será la siguiente: daño = 50 * (ataque / defensa) * efectividad
 * - Efectividad: x2 (súper efectivo), x1 (neutral), x0.5 (no es muy efectivo)
 * - Sólo hay 4 tipos de Pokémon: Agua, Fuego, Planta y Eléctrico 
 *   (buscar su efectividad)
 * - El programa recibe los siguientes parámetros:
 *  - Tipo del Pokémon atacante.
 *  - Tipo del Pokémon defensor.
 *  - Ataque: Entre 1 y 100.
 *  - Defensa: Entre 1 y 100.
 */
"""
from enum import Enum

class Type(Enum):
    fire = 0
    water = 1
    electric = 2
    grass = 3


class Pokemon:
    def __init__(self, type_pokemon_attack, type_pokemon_defense):
        self.type_pokemon_attack = type_pokemon_attack
        self.type_pokemon_defense = type_pokemon_defense

    def damage(self):
        random_attack = random.randrange(1, 100)
        random_defense = random.randrange(1, 100)

        damage = 50 * (random_attack / random_defense) * self.effective

        return f"the damage was of: {round(damage, 2)}"

    def chart_key(self):
        chart_key_matrix = [[0.5, 0.5, 1, 2], [2, 0.5, 1, 0.5], [1, 2, 0.5, 0.5], [0.5, 2, 1, 0.5]]

        if self.type_pokemon_defense == "fire":
            pos_effectivity_defense = Type.fire.value
        elif self.type_pokemon_defense == "water":
            pos_effectivity_defense = Type.water.value
        elif self.type_pokemon_defense == "electric":
            pos_effectivity_defense = Type.electric.value
        elif self.type_pokemon_defense == "grass":
            pos_effectivity_defense = Type.grass.value

        if self.type_pokemon_attack == "fire":
            pos_effectivity_attack = Type.fire.value
        elif self.type_pokemon_attack == "water":
            pos_effectivity_attack = Type.water.value
        elif self.type_pokemon_attack == "electric":
            pos_effectivity_attack = Type.electric.value
        elif self.type_pokemon_attack == "grass":
            pos_effectivity_attack = Type.grass.value

        self.effective = chart_key_matrix[pos_effectivity_defense][pos_effectivity_attack]
            
"""pokemon = Pokemon("fire", "water")
pokemon.chart_key()
print(pokemon.damage())
"""

#LOS ANILLOS DE PODER

"""
/*
 * ¡La Tierra Media está en guerra! En ella lucharán razas leales
 * a Sauron contra otras bondadosas que no quieren que el mal reine
 * sobre sus tierras.
 * Cada raza tiene asociado un "valor" entre 1 y 5:
 * - Razas bondadosas: Pelosos (1), Sureños buenos (2), Enanos (3),
 *   Númenóreanos (4), Elfos (5)
 * - Razas malvadas: Sureños malos (2), Orcos (2), Goblins (2),
 *   Huargos (3), Trolls (5)
 * Crea un programa que calcule el resultado de la batalla entre
 * los 2 tipos de ejércitos:
 * - El resultado puede ser que gane el bien, el mal, o exista un empate.
 *   Dependiendo de la suma del valor del ejército y el número de integrantes.
 * - Cada ejército puede estar compuesto por un número de integrantes variable
 *   de cada raza.
 * - Tienes total libertad para modelar los datos del ejercicio.
 * Ej: 1 Peloso pierde contra 1 Orco
 *     2 Pelosos empatan contra 1 Orco
 *     3 Pelosos ganan a 1 Orco
 */
"""

class Razas_bondadosas(Enum):
    pelosos = 1
    sur_buenos = 2
    enanos = 3
    numeroreanos = 4
    elfos = 5

class Razas_malvadas(Enum):
    sur_malos = 1
    orcos = 2
    goblings = 3
    huargos = 4
    trolls = 5

class Anillos_de_Poder:
    def __init__(self, raza_bondadosa, raza_malvada):
        self.raza_bondadoza = raza_bondadosa
        self.raza_malvada = raza_malvada

    def ganador(self, cant_bueno = 1, cant_malo = 1):
        raza_bondadosa = 1
        raza_malvada = 1

        for raza in Razas_bondadosas:
            if self.raza_bondadoza == raza.name:
                raza_bondadosa = raza.value
                break
        for raza in Razas_malvadas:
            if self.raza_malvada == raza.name:
                raza_malvada = raza.value
                break

        if (cant_bueno * raza_bondadosa) > (cant_malo * raza_malvada):
            return f"{(cant_bueno * raza_bondadosa)} {self.raza_bondadoza} gana contra {cant_malo * raza_malvada} {self.raza_malvada}"
        else:
            if (cant_bueno * raza_bondadosa) < (cant_malo * raza_malvada):
                return f"{(cant_bueno * raza_bondadosa)} {self.raza_bondadoza} pierde contra {cant_malo * raza_malvada} {self.raza_malvada}"
            else:
                return f"{(cant_bueno * raza_bondadosa)} {self.raza_bondadoza} empata contra {cant_malo * raza_malvada} {self.raza_malvada}"

#obj_anillo = Anillos_de_Poder("pelosos", "orcos")

#print(obj_anillo.ganador(1,1))

#Lanzamientos de legend od zelda

"""
/*
 * ¡Han anunciado un nuevo "The Legend of Zelda"!
 * Se llamará "Tears of the Kingdom" y se lanzará el 12 de mayo de 2023.
 * Pero, ¿recuerdas cuánto tiempo ha pasado entre los distintos
 * "The Legend of Zelda" de la historia?
 * Crea un programa que calcule cuántos años y días hay entre 2 juegos de Zelda
 * que tú selecciones.
 * - Debes buscar cada uno de los títulos y su día de lanzamiento 
 *   (si no encuentras el día exacto puedes usar el mes, o incluso inventártelo)
 */
"""

#def quantity_years_days():
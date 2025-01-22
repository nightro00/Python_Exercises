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

print(codigo_morse("El código Morse fue desarrollado para usar el telégrafo, un dispositivo ideado también por Samuel Morse en 1832"))

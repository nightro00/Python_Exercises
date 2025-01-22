
#ANAGRAMA
"""/*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */"""

def anagrama(words1, words2):

    if words1 == words2:
        return False
    
    words_list = [words1[word].lower() for word in range(len(words1))]
    words_list.sort()
 
    words2_list = [words2[word].lower() for word in range(len(words2))]
    words2_list.sort()

    delimiter1 = " "
    delimiter2 = " "
    return delimiter1.join(words_list) == delimiter2.join(words2_list)
        
print(anagrama("Cara", "arca")) 
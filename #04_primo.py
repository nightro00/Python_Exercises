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

            
numero_primos(10)
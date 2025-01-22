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
        

print(decimal_binario(420)[::-1])

# Define a la nueva función divide_string, con entradas de Frase (str)
# y Operacion (int).

def divide_string(frase, operacion):
    if type(frase) != str:  # Determina si la entrada frase NO es de tipo string.
        print("Error: La frase debe ser un string")
        return 42  # Regresa el código de error único 42
    if type(operacion) != int:  # Determina si la entrada operacion NO es de tipo entero.
        print("Error: La operación debe ser un entero")
        return 56  # Regresa el código de error único 56

    if operacion == 1:  # Determina si la operación es de tipo 1, es decir, separa las mayúsculas de las
        # minúsculas del string generando dos strings.
        # Crea a los string de salida mayusculas y minusculas.
        mayusculas = ""
        minusculas = ""

        for caracter in frase:  # Recorre cada uno de los caracteres de la cadena de string frase.
            if caracter.isupper() or caracter.isnumeric():  # Determina si el caracter es mayúscula o es un número.
                mayusculas += caracter   # Agrega el caracter de la cadena que está analizando al string mayusculas.
            elif caracter.islower():  # Determina si el caracter es minúscula.
                minusculas += caracter  # Agrega el caracter de la cadena que está analizando al string minusculas.
            else:
                minusculas += caracter  # Agrega el caracter de la cadena que está analizando al string minusculas.
        return minusculas, mayusculas  # Retorna a los string mayusculas y minusculas.
    if operacion == 2:  # Determina si la operación es de tipo 1, es decir, si divide el string por la mitad.
        mitad = len(frase)//2  # Realiza la división entera del número de caracteres de la frase.
        if (len(frase)) % 2 == 0:  # Determina si la cantidad de caracteres es par.
            parte1 = frase[:mitad]  # Asigna al string parte1 los primeros "mitad" de valores de la cadena
            # de caracteres de frase.
            parte2 = frase[mitad:]  # Asigna al string parte2 los segundos "mitad" de valores de la cadena
            # de caracteres de frase.
        else:  # En caso de ser impar.
            parte1 = frase[:mitad+1]  # Asigna al string parte1 los primeros "mitad+1" de valores de la cadena
            # de caracteres de frase.
            parte2 = frase[mitad+1:]  # Asigna al string parte2 los segundos "mitad+1" de valores de la cadena
            # de caracteres de frase.
        return parte1, parte2  # Retorna a los string parte1 y parte2.


def measure_area(parametro):  # Define a la nueva función measure_area, con entrada de parametro(int).
    if type(parametro) != int:  # Determina si la entrada parametro NO es de tipo entero.
        print("Error: El parámetro debe ser un entero")
        return 33  # Regresa el código de error único 33
    areacuadrado = parametro * parametro  # Determina el valor del área del cuadrado tomando al parametro como los
    # lados del cuadrado.
    areacirculo = parametro * 3.1416  # Determina el valor del área del círculo tomando al parametro como el
    # radio del círculo.

    print(areacuadrado)
    print(areacirculo)
    return areacuadrado, areacirculo  # Retorna a los int areacuadrado y areacirculo.


print(divide_string("12$Prueba_De_Frase34%", 1))

measure_area(4)

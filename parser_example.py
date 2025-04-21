# David Guerrero Aragon A01285837
# Fernando Gael Hernández Salazar A01029264

import sys
import obten_token as scanner  # Asegúrate de que este sea el scanner modificado

# Empata y obtiene el siguiente token
def match(tokenEsperado):
    global token
    if token == tokenEsperado:
        token = scanner.obten_token()
    else:
        error("token equivocado")

# Función principal: implementa el análisis sintáctico
def parser():
    global token
    token = scanner.obten_token()  # inicializa con el primer token
    while token != scanner.END:  # Continúa hasta encontrar el fin de la entrada
        if token == scanner.IDE:
            asi()  # Si es un identificador, trata como asignación
        exp()
    print("Expresión bien construida!!")

# Modulo que reconoce asignaciones y funciones
def asi():
    if token == scanner.IDE:  # Identificador de asignación
        match(scanner.IDE)  # Empareja el identificador
        if token == scanner.ASI:  # Operador de asignación
            match(scanner.ASI)
            exp()  # Expresión aritmética
        elif token == scanner.LRP:
            match(scanner.LRP)
            argumentos()
        else:
            error("Expresión mal terminada")
    
        

# Módulo que reconoce expresiones
def exp():
    if token == scanner.INT or token == scanner.FLT:  # Constantes numéricas
        match(token)
        exp1()  # Expresión adicional
    elif token == scanner.LRP:  # Paréntesis de apertura
        match(scanner.LRP)
        exp()  # Expresión dentro de los paréntesis
        match(scanner.RRP)  # Paréntesis de cierre
        exp1()
    elif token == scanner.IDE:  # Identificadores o llamadas a funciones
        match(scanner.IDE)
        if token == scanner.LRP:  # Llamada a función (paréntesis)
            match(scanner.LRP)
            argumentos()  # Argumentos de la función
            match(scanner.RRP)  # Paréntesis de cierre
        exp1()

# Módulo auxiliar para reconocimiento de expresiones adicionales
def exp1():
    if token == scanner.OPB:  # Operadores binarios
        match(scanner.OPB)  # Empareja el operador
        exp()  # Expresión derecha
        exp1()

# Módulo que reconoce los argumentos de una función
def argumentos():
    if token == scanner.INT or token == scanner.FLT or token == scanner.IDE or token == scanner.LRP:  # Argumentos posibles
        exp()  # Puede ser una constante, un identificador o una expresión entre paréntesis
        while token == scanner.SEP:  # Si hay una coma, seguimos con más argumentos
            match(scanner.SEP)
            exp()

# Termina con un mensaje de error
def error(mensaje):
    print("ERROR:", mensaje)
    sys.exit(1)

    
sys.stdin = open(0)
parser()
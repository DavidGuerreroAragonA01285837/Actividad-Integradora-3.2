import sys
import scanner
import io
global error_help
global errors

def match(tokenEsperado):
    global token
    global lexemas
    global lexema
    if token == tokenEsperado:
        token, lexema = scanner.obten_token()
        lexemas.append(lexema)
    else:
        print(f"Se esperaba {tokenEsperado}, pero se encontró {token}")

def parser():
    global token
    global lexemas
    lexemas = []
    token, lexema = scanner.obten_token()
    lexemas.append(lexema)
    prog()

def const():
    global token, lexema
    if token == scanner.STR:
        match(scanner.STR)
    elif token == scanner.BOOL:
        match(scanner.BOOL)
    elif token == scanner.NUM:
        match(scanner.NUM)
    else:
        print("Error de sintaxis en:" + lexema)
        token, lexema = scanner.obten_token()

def atom():
    if token == scanner.SYMB:
        match(scanner.SYMB)
    else:
        const()

def lista():
    match(scanner.LSP)
    while (True):
        if token != scanner.END:
            exp()
            if token == scanner.RSP:
                match(scanner.RSP)
                break
        else:
            print("Error de sintaxis, se esperaba un ')' ")
            break
            
            

def exp():
    global lexema
    if token == scanner.ERR:
        print("Error de lexico en:" + lexema)
        match(scanner.ERR)
    elif token == scanner.LSP:
        lista()
    else:
        atom()

def prog():
    global lexemas
    while token != scanner.END:
        exp()
    lexemas[len(lexemas)-1] += '$'



expresion = '''atomo 25 #t "hola amigo"
((1 2)(#f #t)) es una lista anidada
(define (prueba x)
(if (equal x 10)
(display (x igual a 10))
(display x diferente de 10)))$'''

sys.stdin = io.StringIO(expresion)
parser()

def imprimir_lexemas():
    # Recorremos los lexemas y los imprimimos, respetando saltos de línea
    line = ""
    for lex in lexemas:
        if lex == "\n":  # Si encontramos un salto de línea en el input, lo respetamos
            print(line.strip())
            line = ""  # Reiniciamos la línea para empezar una nueva
        else:
            line += lex + " "
    
    # Si al final queda algo en la variable `line`, la imprimimos
    if line.strip():
        print(line.strip())

imprimir_lexemas()
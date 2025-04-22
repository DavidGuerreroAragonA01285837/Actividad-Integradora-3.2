import sys

# tokens

SYMB = 100 # Simbolo
NUM = 101  # Numero
BOOL = 102 # Booleano
STR = 103  # String
RSP = 104  # Parentesis derecho
LSP = 105  # Parentesis Izquierdo
END = 106  # Simbolo final
ERR = 200  # Error lexico

# Matriz de transiciones: codificación del AFD
# [renglón, columna] = [estado no final, transición]
# Estados > 99 son finales (ACEPTORES)
# Caso especial: Estado 200 = ERROR
#     a-z,  0-9,  #, (t,f), (,   ),  $ ,  ", esp, ent, caracter inesperado
MT = [[1,    2,   3,   1,  LSP,RSP,END,  5,   0,    0,  7], # Estado inicial
      [1,    7,   7,   1, SYMB,SYMB, 7,  7, SYMB,SYMB,  7], # Estado de construccion de Simbolo
      [7,    2,   7,   7, NUM , NUM, 7,  7, NUM ,NUM ,  7], # Estado de construccion de numero
      [7,    7,   7,   4,  ERR,  ERR,  7,  7,  ERR,  ERR,  7], # Estado de inicio de booleano
      [7,    7,   7,   7, BOOL, BOOL,  7,  7,BOOL,BOOL, 7], # Estado de bool valido
      [5,    5,   7,   5,  ERR, ERR, ERR,  6,  5, ERR, 7], # Estado de construccion de string
      [7,    7,   7,   7, STR,  STR,  7,  7, STR, STR,  7], # Estado de string valido
      [7,    7,   7,   7, ERR,  ERR,  7,  7, ERR, ERR,  7]] # Estado de error

# Filtro de caracteres de entrada
def filtro(c):
    if c in 'abcdeghijklmnopqrsuvwxyz': # letras de la a-z sin t y f
        return 0
    elif c == '0' or c == '1' or c == '2' or \
       c == '3' or c == '4' or c == '5' or \
       c == '6' or c == '7' or c == '8' or c == '9': # dígitos
        return 1
    elif c == "#": # Simbolo # para booleano
        return 2
    elif c == "t" or c == "f": # caracteres t y f
        return 3
    elif c == '(': # delimitador (
        return 4
    elif c == ')': # delimitador )
        return 5
    elif c == '$': # Caracter de finalizacion
        return 6
    elif c == '"':  # Caracter de comillas
        return 7
    elif c == ' ' or ord(c) == 9: # delimitador espacio
        return 8
    elif c == ord(c) == 10 or ord(c) == 13 or c =='\n': # delimitador de salto de linea
        return 9
    else:  # caracteres inesperados
        return 10
    
    
_c = None # Siguiente caracter
_leer = True # Determina si se requiere leer un caracter de la entrada estandar.

def obten_token():
    
    global _c, _leer
    edo = 0
    lexema = ""
    
    while (True):
        while edo < 100:
            if _leer: 
                _c = sys.stdin.read(1)
            else: _leer = True
            edo = MT[edo][filtro(_c)]
            if edo < 100 and edo != 0: lexema += _c
        if edo == SYMB:
            _leer = False
            #print("Simbolo", lexema)
            if _c == '\n':
                lexema += '\n'
            return SYMB, lexema
        elif edo == NUM:
            _leer = False
            #print("Numero", lexema)
            if _c == '\n':
                lexema += '\n'
            return NUM, lexema
        elif edo == BOOL:
            _leer = False
            #print("Booleano", lexema)
            if _c == '\n':
                lexema += '\n'
            return BOOL, lexema
        elif edo == STR:
            _leer = False
            #print("String", lexema)
            if _c == '\n':
                lexema += '\n'
            return STR, lexema
        elif edo == RSP:
            lexema += _c 
            #print("Parentesis", lexema)
            _c = sys.stdin.read(1)
            _leer = False
            if _c == '\n':
                lexema += '\n'
            return RSP, lexema
        elif edo == LSP:
            lexema += _c 
            #print("Parentesis", lexema)
            _c = sys.stdin.read(1)
            _leer = False
            if _c == '\n':
                lexema += '\n'
            return LSP, lexema
        elif edo == END:
            #print("Final", lexema)
            return END, lexema
        elif edo == ERR:
            # Incluir el caracter actual en el lexema
            lexema += _c
            #print("Error léxico:", lexema)
            return ERR, lexema
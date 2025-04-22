import sys
import scanner
import io
global error_help
global errors
global tokens
error_help = []
errors = []
tokens = []

def match(tokenEsperado):
    global tokens
    global token
    global lexemas
    global lexema
    global error_help
    global errors
    if token == tokenEsperado:
        if '\n' in lexema:
            errors.append(", ".join(error_help))
            error_help = []
        token, lexema = scanner.obten_token()
        tokens.append(token)
        lexemas.append(lexema)
    else:
        print(f"Se esperaba {tokenEsperado}, pero se encontró {token}")

def parser():
    global token
    global lexema
    global lexemas
    lexemas = []
    token, lexema = scanner.obten_token()
    tokens.append(token)
    lexemas.append(lexema)
    prog()

def const():
    global token, lexema, errors, error_help
    if token == scanner.STR:
        match(scanner.STR)
    elif token == scanner.BOOL:
        match(scanner.BOOL)
    elif token == scanner.NUM:
        match(scanner.NUM)
    else:
        error_help.append(" Error de sintaxis en " + lexema)
        # print("Error de sintaxis en:" + lexema)
        if '\n' in lexema:
            errors.append(", ".join(error_help))
            error_help = []
        token, lexema = scanner.obten_token()
        tokens.append(token)
        lexemas.append(lexema)

def atom():
    if token == scanner.SYMB:
        match(scanner.SYMB)
    else:
        const()

def lista():
    global error_help
    match(scanner.LSP)
    while (True):
        if token != scanner.END:
            exp()
            if token == scanner.RSP:
                match(scanner.RSP)
                break
        else:
            error_help.append(" Error de sintaxis, se esperaba un ')' ")
            # print("Error de sintaxis, se esperaba un ')' ")
            break
            
            

def exp():
    global error_help
    global lexema
    if token == scanner.ERR:
        error_help.append(" Error de lexico en " + lexema)
        # print("Error de lexico en:" + lexema)
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



#expresion = '''atomo 25 # "hola amigo"
#((1 2)(#f #t)) es una lista anidada
#(define (prueba x)
#(if (equal x 10)
#(display (x igual a 10))
#(display x diferente de 10)))$''' 

#sys.stdin = io.StringIO(expresion)
input()
parser()

def imprimir_lexemas():
    # Abre el archivo HTML para escritura
    with open("analisis_tokens.html", "w") as f:
        # Escribe la estructura básica del HTML
        f.write("""
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Analisis de Tokens</title>
            <link rel="stylesheet" href="styles.css">
        </head>
        <body>
            <h1>Analisis de Tokens</h1>
            <div>
        """)
        
        code_lines = []
        helper = ""
        
        for n,t in zip(lexemas, tokens):
            if '\n' in n:
                if t == scanner.SYMB:
                    helper+= "<span> " + n + " </span>"
                elif t == scanner.NUM:
                    helper+= '<span class="num"> ' + n + " </span>"
                elif t == scanner.BOOL:
                    helper+= '<span class="bool"> ' + n + " </span>"
                elif t == scanner.STR:
                    helper+= '<span class="str"> ' + n + " </span>"
                elif t == scanner.RSP:
                    helper+= '<span class="rsp"> ' + n + " </span>"
                elif t == scanner.LSP:
                    helper+= '<span class="lsp"> ' + n + " </span>"
                elif t == scanner.END:
                    helper+= '<span class="end">' + n + "  </span>"
                elif t == scanner.ERR:
                    helper+= "<span> " + n + " </span>"
                code_lines.append(" " + helper + " ")
                helper = ""
            else:
                
                if t == scanner.SYMB:
                    helper+= "<span> " + n + " </span>"
                elif t == scanner.NUM:
                    helper+= '<span class="num"> ' + n + " </span>"
                elif t == scanner.BOOL:
                    helper+= '<span class="bool"> ' + n + " </span>"
                elif t == scanner.STR:
                    helper+= '<span class="str"> ' + n + " </span>"
                elif t == scanner.RSP:
                    helper+= '<span class="rsp"> ' + n + " </span>"
                elif t == scanner.LSP:
                    helper+= '<span class="lsp"> ' + n + " </span>"
                elif t == scanner.END:
                    helper+= '<span class="end"> ' + n + " </span>"
                elif t == scanner.ERR:
                    helper+= "<span> " + n + " </span>"
                
                
        code_lines.append(" " + helper + " ")
        errors.append(", ".join(error_help))
        
        
        i = 0
        for n in code_lines:
            if errors[i] != '':
                errors[i] = '<span class="err"> ==>' + errors[i] +'</span>'
            temp = " ".join([n[:-1], errors[i],'<br>'])
            
            f.write(temp)
            
            i += 1

        # Finaliza el HTML
        f.write("""
            </div>
        </body>
        </html>
        """)

    print("El análisis se ha guardado en 'analisis_tokens.html'.")

imprimir_lexemas()
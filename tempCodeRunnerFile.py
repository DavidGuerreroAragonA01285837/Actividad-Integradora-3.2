def imprimir_lexemas():
    # Abre el archivo HTML para escritura
    with open("analisis_tokens.html", "w") as f:
        # Escribe la estructura básica del HTML
        f.write("""
        <html>
        <head>
            <title>Analisis de Tokens</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    line-height: 1.6;
                }
                .str { color: gray; }
                .num { color: green; }
                .bool { color: purple; }
                .err { color: red; }
                .lsp { color: red; font-weight: bold; }
                .rsp { color: red; font-weight: bold; }
                .end { color: cyan; font-weight: bold; }
            </style>
        </head>
        <body>
            <h1>Análisis de Tokens</h1>
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
            temp = " ".join([n, errors[i]])
            
            f.write(temp)
            
            i += 1

        # Finaliza el HTML
        f.write("""
            </div>
        </body>
        </html>
        """)

    print("El análisis se ha guardado en 'analisis_tokens.html'.")
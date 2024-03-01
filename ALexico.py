import re

def analizador_lexico(input_string):
    # Definir tokens con expresiones regulares específicas.
    tokens = {
        'NUM_VAR': r'[a-zA-Z]\w*',  # Identificadores y palabras clave
        'ASSIGN': r'=',
        'DIGIT': r'\d+',  # Números
        'DOT': r'\.',  # Punto para números decimales, aunque no se usa en la gramática actual
        'TRUE': r'\btrue\b',  # Booleano true
        'FALSE': r'\bfalse\b',  # Booleano false
        'FUNCTION_DECLARATION': r'\bFn\b',  # Declaración de función
        'PARENTHESIS_OPEN': r'\(',
        'PARENTHESIS_CLOSE': r'\)',
        'COLON': r':',
        'BRACE_OPEN': r'\{',
        'BRACE_CLOSE': r'\}',
        'ASSUMING': r'\bassuming\b',  # Estructura condicional
        'OPERATOR': r'==|=>|<=|!=|>|<',  # Operadores
        'LOOP': r'\bloop\b',  # Bucle
        'OTHERWISE': r'\botherwise\b',  # Clausula otherwise
        'UNKNOWN': r'\S+'  # Cualquier otro carácter no reconocido
    }

    token_regex = '|'.join(f'(?P<{name}>{regex})' for name, regex in tokens.items())

    line_number = 1
    tokens_with_lines = []
    lines = input_string.split('\n')

    for line in lines:
        for match in re.finditer(token_regex, line):
            token_type = match.lastgroup
            lexeme = match.group()
            tokens_with_lines.append([token_type, lexeme, line_number])
        line_number += 1

    return tokens_with_lines

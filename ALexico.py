import re

TOKEN_PATTERNS = [
    ('STRING', r'\".*\"'),  
    ('NUMERO', r'\d+'),  
    ('PALABRAS_RESERVADAS', r'\b(Fn|assuming|loop|true|false|otherwise)\b'), 
    ('ASIGNACION', r'='),  
    ('OPERADORES_COMPARACION', r'(==|=>|<=|!=|>|<)'),  
    ('PARENTESIS', r'(\(|\))'), 
    ('LLAVES', r'(\{|\})'),  
    ('DOS_PUNTOS', r'\:'), 
    ('IDENTIFICADOR', r'[a-zA-Z][a-zA-Z0-9_]*'),  
    ('INCREMENTO', r'(\+\+)'),
    ('DECREMENTO', r'(\-\-)'),
    ('SIGNOS', r'(\+|\-|\*|\&)'),  
    ('PUNTO', r'\.'), 
    ('COMA', r'\,'),  
    ('PUNTO_Y_COMA', r'\;'),  
]

def lexer(code):
    tokens = []
    while code:
        for token_name, pattern in TOKEN_PATTERNS:
            match = re.match(pattern, code)
            if match:
                value = match.group(0)
                tokens.append((token_name, value))
                code = code[len(value):].lstrip()
                break
        else:
            tokens.append(("Simbolo no reconocido", code[0]))
            code = code[1:].lstrip()

    return tokens

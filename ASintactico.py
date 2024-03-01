gramatica = {
    ("S", "LOOP"): ["CI", "S"],
    ("S", "OTHERWISE"): ["I", "S"],
    ("I", "ASSUMING"): ["ASSUMING", "PARENTHESIS_OPEN", "C", "PARENTHESIS_CLOSE", "COLON", "BRACE_OPEN", "CO", "BRACE_CLOSE"],
    ("C", "NUM_VAR"): ["O", "OPERATOR", "O"],
    ("CI", "LOOP"): ["LOOP", "PARENTHESIS_OPEN", "C", "PARENTHESIS_CLOSE", "COLON", "BRACE_OPEN", "CO", "BRACE_CLOSE"],
    
    ("S", "NUM_VAR"): ["A", "S"],
    ("S", "FUNCTION_DECLARATION"): ["IN", "S"],
    ("S", "ASSUMING"): ["I", "S"],
    ("S", "LOOP"): ["CI", "S"],
    ("S", "OTHERWISE"): ["I", "E"],  
    ("S", "$"): ["EPSILON"],
    
    ("A", "NUM_VAR"): ["NUM_VAR", "ASSIGN", "O"],
    ("O", "NUM_VAR"): ["NUM_VAR"],
    ("O", "OPERATOR"): ["OPERATOR"],
    ("O", "DIGIT"): ["DIGIT"],
    ("O", "TRUE"): ["TRUE"],
    ("O", "FALSE"): ["FALSE"],

    ("IN", "FUNCTION_DECLARATION"): ["NUM_VAR", "FUNCTION_DECLARATION", "PARENTHESIS_OPEN", "NUM_VAR", "PARENTHESIS_CLOSE", "COLON", "BRACE_OPEN", "CO", "BRACE_CLOSE"],
    ("CO", "NUM_VAR"): ["A", "CO"],
    ("CO", "ASSUMING"): ["I", "CO"],
    ("CO", "LOOP"): ["CI", "CO"],
    ("CO", "BRACE_CLOSE"): ["EPSILON"],

    ("I", "ASSUMING"): ["ASSUMING", "PARENTHESIS_OPEN", "C", "PARENTHESIS_CLOSE", "COLON", "BRACE_OPEN", "CO", "BRACE_CLOSE"],
    ("C", "NUM_VAR"): ["NUM_VAR", "OPERATOR", "O"],
    ("CI", "LOOP"): ["LOOP", "PARENTHESIS_OPEN", "C", "PARENTHESIS_CLOSE", "COLON", "BRACE_OPEN", "CO", "BRACE_CLOSE"]
}

terminales = [
    'NUM_VAR', 'ASSIGN', 'OPERATOR', 'DIGIT', 'TRUE', 'FALSE', 'FUNCTION_DECLARATION',
    'PARENTHESIS_OPEN', 'PARENTHESIS_CLOSE', 'COLON', 'BRACE_OPEN', 'BRACE_CLOSE',
    'ASSUMING', 'LOOP', 'OTHERWISE'
]


def analizador_sintactico(simbolos):
    stack = ['$', 'S']
    text = str(stack) + '\n'
    index = 0
    simbolos.append(('$', '$', simbolos[-1][2]))
    while True:
        X = stack.pop()
        a = simbolos[index][0]
        if X in terminales:
            if X == a:
                index += 1    
                text += str(stack) + '\n'
                if X == '$':
                    return "No se encontraron errores de sintaxis"
            else:
                return (f'\nError de sintaxis en la linea {simbolos[index][2]}' + 
                f'\n Entrada en conflicto: {simbolos[index][0]} con el valor {simbolos[index][1]}')
        else:
            if (X, a) in gramatica:
                producciones = gramatica[(X, a)]
                if producciones != ['EPSILON']:
                    for produccion in reversed(producciones):
                        stack.append(produccion)
                text += str(stack) + '\n'
            else:
                return (f'\nError de sintaxis en la linea {simbolos[index][2]}' +
                f'\n Entrada en conflicto: {simbolos[index][0]} con el valor {simbolos[index][1]}')
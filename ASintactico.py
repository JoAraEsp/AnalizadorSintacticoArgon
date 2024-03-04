parser_table = {
    "A": {
        "L": ["NV"],  # Identificadores que inician una asignación
        "Fn": ["DF"],  # Inicia una definición de función
        "assuming": ["I"],  # Inicia una estructura de control condicional
        "loop": ["CI"],  # Inicia un bucle
    },
    "NV": {
        "L": ["L", "I", "O"],  # Identificador seguido de '=' y un objeto/valor
    },
    "I": {
        "=": ["=", "O"],  # Igual seguido por un valor
    },
    "O": {
        "L": ["L"],  # Identificador como valor en una asignación
        "D": ["D"],  # Número como valor en una asignación
        "true": ["true"],  # Booleano verdadero
        "false": ["false"],  # Booleano falso
    },
    "DF": {
        "Fn": ["Fn", "L", "PA", "PC", "DP", "LA", "CO", "LC"],  # Estructura para la definición de función
    },
    "I": {
        "assuming": ["assuming", "PA", "L", "K2", "PC", "DP", "LA", "CO", "LC", "O1", "M1"],  # Control condicional
    },
    "CI": {
        "loop": ["loop", "PA", "L", "K2", "PC", "DP", "LA", "CO", "LC"],  # Bucle
    },
    "K2": {
        "==": ["==", "O"], 
        "=>": ["=>", "O"], 
        "<=": ["<=", "O"], 
        "!=": ["!=", "O"], 
        ">": [">", "O"], 
        "<": ["<", "O"]
    },
    "O1": {
        "otherwise": ["otherwise", "DP", "LA", "CO", "LC"]
    },
    "M1": {
        "DP": ["DP", "M2"]
    },
    "M2": {
        "LA": ["LA", "M3"]
    },
    "M3": {
        "CO": ["CO", "LC"]
    },
    "PA": {
        "(": ["("]
    },
    "PC": {
        ")": [")"]
    },
    "DP": {
        ":": [":"]
    },
    "LA": {
        "{": ["{"]
    },
    "LC": {
        "}": ["}"]
    },
    "CO": {
        "Contenido": ["Contenido"]
    },
}


terminales = {
    "=", "(", ")", ":", "{", "}", "true", "false", 
    "Fn", "assuming", "loop", "otherwise", 
    "==", "=>", "<=", "!=", ">", "<",
    "Contenido"
}

def es_terminal(token: str):
    return token in terminales

def analizar_sintaxis(lista_input: list):
    historial = ""
    lista_input.append("$")
    pila = ["$", "A"]

    while len(pila) > 0:
        a_str = lista_input[0]
        X_str = pila[-1]
        historial += f"Pila: {pila} | Entrada: {a_str}\n"
        if es_terminal(X_str):
            if X_str == a_str:
                pila.pop()
                lista_input.pop(0)
            else:
                return {
                    "success": False,
                    "message": f"Error en el caracter {a_str} en la posicion {len(lista_input) - 1}. Se esperaba {X_str}",
                    "historial": historial,
                }
        else:
            try:
                if a_str in parser_table[X_str]:
                    pila.pop()
                    for symbol in reversed(parser_table[X_str][a_str]):
                        if symbol != 'ε':
                            pila.append(symbol)
                else:
                    return {
                        "success": False,
                        "message": f"Error en el caracter {a_str} en la posicion {len(lista_input) - 1}. No se encuentra una regla adecuada para {X_str} con {a_str}",
                        "historial": historial,
                    }
            except KeyError:
                return {
                    "success": False,
                    "message": f"No se encuentra {X_str} en la tabla de análisis para {a_str}",
                    "historial": historial,
                }

    return {"success": True, "message": "Gramatica correcta", "historial": historial}

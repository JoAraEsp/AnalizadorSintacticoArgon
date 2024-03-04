def separar_elementos(input_string):
    elements = ["=", "(", ")", ":", "{", "}", "true", "false", "Fn", 
                "assuming", "==", "=>", "<=", "!=", ">", "<", "loop", 
                "otherwise", "Contenido"]

    output_list = []
    current_word = ""

    for char in input_string:
        if char.isspace():
            if current_word:
                # Comprobar si es un elemento reservado o un identificador/número.
                output_list.append(current_word)
                current_word = ""
        elif char.isalnum() or char == '_':
            current_word += char
        else:
            if current_word:
                output_list.append(current_word)
                current_word = ""
            if char in elements:
                output_list.append(char)

    if current_word:
        output_list.append(current_word)

    return output_list

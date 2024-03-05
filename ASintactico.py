from lark import Lark,logger
from file import load_content_from_file
import logging

logger.setLevel(logging.DEBUG)

def syntactic_analyzer(input: str):
    try:
        grammar = load_content_from_file('argon.lark')

        parser = Lark(grammar, start='start', parser='lalr', debug=True)
        parser.parse(input)
        return {'status': 'success', 'message': 'La entrada es valida.'}
    except Exception as e:

        return {'status': 'error', 'message': str(e)}
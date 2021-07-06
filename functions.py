import os
from datetime import datetime


def do_ping(arg):
    return f'Pong, {arg}'


def do_ls(arg):
    return '\n'.join(os.listdir(arg))


def do_print(string):
    try:
        text = f'INFO: {string}. - Time {str(datetime.now())}'
        return text.encode('utf-8')
    except Exception as error:
        return f'ERROR: funcion {do_print.__name__} -> error -> {str(error)}'
import os


def do_ping(arg):
    return f'Pong, {arg}'


def do_ls(arg):
    return '\n'.join(os.listdir(arg))
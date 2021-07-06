from config import *
from functions import *


def process_network_command(command, arg):
    print(pipelines[command](arg))


def console_log(command, arg):
    print(another_pipeline[command](arg))


if __name__ == "__main__":
    process_network_command('ping', '0.0.0.0')
    console_log('logger', 'Another brick in the wall')
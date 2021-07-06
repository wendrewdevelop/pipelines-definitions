from config import *
from functions import *


def process_network_command(command, arg):
    print(pipelines[command](arg))


if __name__ == "__main__":
    process_network_command('ping', '0.0.0.0')
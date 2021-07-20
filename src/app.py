# pytohn imports
import random
# project imports
from config import *
from functions import *



def request_api(command, arg):
    return pipeline[command](arg)


if __name__ == "__main__":
    words = [
        'github',
        'd&d',
        'eva'
    ]
    console_log('Gerando Pipeline')
    try:
        if random.choice(words) == 'github':
            request_api("github", 'https://api.github.com/users/wendrewdevelop')
            console_log('Pipeline gerado (github)')
        if random.choice(words) == 'd&d':
            request_api("d&d", 'https://www.dnd5eapi.co/api/classes/')
            console_log('Pipeline gerado (d&d)')
        if random.choice(words) == 'eva':
            request_api("eva", 'https://api.eva.pingutil.com/email?email=wendrewdevelop@gmail.com')
            console_log('Pipeline gerado (eva)')
        
        console_log('Processo finalizado com sucesso')
    except Exception as error:
        console_log(f'{error}')
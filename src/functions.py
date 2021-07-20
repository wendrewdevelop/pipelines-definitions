# python imports
import os
import io
from datetime import datetime
# thirdy imports
import requests
import pandas as pd


def console_log(string):
    try:
        text = f'INFO: {string}. - Time {str(datetime.now())}'
        print(text.encode('utf-8'))
    except Exception as error:
        print(f'ERROR: funcion {console_log.__name__} -> error -> {str(error)}')


def github_requests(url: str):
    """
        get github content.

        https://api.github.com/users/wendrewdevelop
    """

    try:
        response = requests.get(url).json()

        df = pd.json_normalize(response)
        df.to_csv('users.csv', index=False)
    except Exception as error:
        print(error)


def email_verifier_requests(url: str):
    """
        get e-mail verifier json.

        https://api.eva.pingutil.com/email?email=wendrewdevelop@gmail.com
    """

    try:
        response = requests.get(url).json()

        df = pd.json_normalize(response)
        df.to_csv('email_verifier.csv', index=False)
    except Exception as error:
        print(error)


def dungeons_dragons_requests(url: str):
    """
        get d&d classes.

        https://www.dnd5eapi.co/api/classes/
    """
    x = []

    try:
        response = requests.get(url).json()
        for r in response['results']:
            df = pd.json_normalize(r)
            x.append(df)
        csv = pd.concat(x, ignore_index=True)
        csv.to_csv('d&d_classes.csv', index=False)
    except Exception as error:
        print(error)
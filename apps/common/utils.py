import requests


def get_coins_list():
    data = requests.get('https://api.coingecko.com/api/v3/coins/list')
    return data.json()


def get_coin_by_id(coin_id):
    data = requests.get(f'https://api.coingecko.com/api/v3/coins/{coin_id}')
    return data.json()

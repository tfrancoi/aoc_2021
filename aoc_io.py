import requests


def get_input(day):
    cookies = {
        'session': 'Monster'
    }
    response = requests.get(f"https://adventofcode.com/2021/day/{day}/input", cookies=cookies)
    return list(filter(lambda i: i.strip() != '', response.text.split('\n')))

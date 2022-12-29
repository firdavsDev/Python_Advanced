from concurrent.futures import ThreadPoolExecutor

import requests

from timer_decorator import timer 

URL = 'https://httpbin.org/uuid'


def fetch(session, url):
    with session.get(url) as response:
        print(response.json()['uuid'])


@timer(1, 2)
def main():
    with ThreadPoolExecutor(max_workers=100) as executor:
        with requests.Session() as session:
            executor.map(fetch, [session] * 80, [URL] * 80)
            executor.shutdown(wait=True)
# 12 sec

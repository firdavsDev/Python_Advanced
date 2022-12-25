import requests


from timer_decorator import timer 

URL = 'https://httpbin.org/uuid'


def fetch(session, url):
    with session.get(url) as response:
        print(response.json()['uuid'])


@timer(1, 2)
def main():
    with requests.Session() as session:
        for _ in range(80):
            fetch(session, URL)

# 22.57041470799959

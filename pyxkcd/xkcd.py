import random
import click
import requests

API_URL = "https://xkcd.com/"


def fetch_latest() -> dict:
    url = API_URL.rstrip("/") + "/info.0.json"
    res = requests.get(url)

    return dict(res.json())


def fetch_specific(number: int) -> dict:
    url = API_URL.rstrip("/") + "/" + str(number) + "/info.0.json"
    res = requests.get(url)

    return dict(res.json())


def fetch_random() -> dict:
    latest = fetch_latest()
    randnum = random.randint(1, latest["num"])

    return fetch_specific(randnum)

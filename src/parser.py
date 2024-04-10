from typing import Any
import requests
from loguru import logger
from requests import Response

URL = "https://min-api.cryptocompare.com/data/price?fsym=TONCOIN&tsyms=USD"


@logger.catch()
def update_info() -> str:
    response: Response = requests.get(url=URL)

    if response.status_code != 200:
        logger.critical(f"Status code is {response.status_code}")
        return f"NoData!"

    course: Any = response.text
    chars_to_remove: list = ["{", "}", '"']

    for char in chars_to_remove:
        course = course.replace(char, "")

    course = course.split(":")
    course[1] = round(float(course[1]), 2)

    return course[0] + ": " + str(course[1])


# Test
if __name__ == "__main__":
    print(update_info())

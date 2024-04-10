import requests
from loguru import logger

URL = "https://min-api.cryptocompare.com/data/price?fsym=TONCOIN&tsyms=USD"


@logger.catch()
def update_info() -> str:
    response = requests.get(url=URL)

    if response.status_code != 200:
        return f"Status code {response.status_code}"

    course = response.text
    chars_to_remove = ["{", "}", '"']

    for char in chars_to_remove:
        course = course.replace(char, "")

    course = course.split(":")
    course[1] = round(float(course[1]), 2)

    return course[0] + ": " + str(course[1])


if __name__ == "__main__":
    print(update_info())

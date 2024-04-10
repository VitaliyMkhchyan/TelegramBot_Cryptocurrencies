from dotenv import load_dotenv
from os import getenv

load_dotenv()

TOKEN: str = getenv("TOKEN")
TIME_UPDATE_USER: int = 900  # секунд
TIME_UPDATE_DB: int = 300  # секунд
NAME_DB: str = "course_toncoin.db"
LOG_FILE: str = "./data/debug.log"

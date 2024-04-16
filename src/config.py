from dotenv import load_dotenv
from os import getenv

load_dotenv()

TOKEN: str = getenv("TOKEN")
TIME_UPDATE_USER: int = 900  # секунд
TIME_UPDATE_DB: int = 300  # секунд
LOG_FILE: str = "../data/debug.log"

NAME_DB: str = "course_toncoin.db"
DB_FILE: str = f"../data/{NAME_DB}"
DB_CREATE_FILE: str = "../src/create_db.sql"
DB_SAVING_DATA: str = "../src/saving_data.sql"

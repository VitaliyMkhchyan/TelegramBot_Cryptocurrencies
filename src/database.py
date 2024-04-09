import sqlite3
from config import NAME_DB
from loguru import logger


class Database:
    def __init__(self, course: str, update_course: str):
        self.course = course
        self.update_course = update_course

        self.connect = sqlite3.connect(f"./data/{NAME_DB}")
        self.cursor = self.connect.cursor()

    @logger.catch()
    def save_data(self):
        logger.info("Saving data...")
        sql: str

        with open("./src/saving_data.sql") as file:
            sql = file.read()

        data: tuple = (self.course, self.update_course)
        self.cursor.execute(sql, data)
        self.connect.commit()
        self.connect.close()
        logger.info("The data is saved!")

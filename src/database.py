import sqlite3
from sqlite3 import Connection
from config import NAME_DB
from loguru import logger


class Database:
    def __init__(self, course: str, update_course: str):
        self.course: str = course
        self.update_course: str = update_course

        self.connect: Connection = sqlite3.connect(f"./data/{NAME_DB}")
        self.cursor = self.connect.cursor()

    @logger.catch()
    def save_data(self):
        logger.info("Saving data...")
        sql: str

        with open("./src/saving_data.sql") as file:
            sql = file.read()

        data: tuple = (self.course, self.update_course)
        try:
            self.cursor.execute(sql, data)
            self.connect.commit()
        except sqlite3.Error as e:
            logger.error(e)
        finally:
            self.connect.close()

        logger.info("The data is saved!")


# Test
if __name__ == '__main__':
    Database("Test course", "Test date").save_data()

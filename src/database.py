import sqlite3
from sqlite3 import Connection, Cursor
from config import DB_FILE, DB_CREATE_FILE, DB_SAVING_DATA
from loguru import logger
from typing import NoReturn


class Database:
    def __init__(self, course: str, update_course: str) -> NoReturn:
        self.course: str = course
        self.update_course: str = update_course

        try:
            self.connect: Connection = sqlite3.connect(DB_FILE)
        except sqlite3.OperationalError:
            logger.critical("Не удается открыть файл базы данных!")

        self.cursor = self.connect.cursor()

    @logger.catch()
    def save_data(self) -> NoReturn:
        logger.info("Saving data...")

        with open(DB_SAVING_DATA) as file:
            sql: str = file.read()

        data: tuple = (self.course, self.update_course)
        try:
            self.cursor.execute(sql, data)
            self.connect.commit()
            logger.info("The data is saved!")
        except sqlite3.Error as e:
            logger.error("The data has not been saved! " + str(e))
        finally:
            self.connect.close()


def _create_db() -> NoReturn:
    """ Метод для создания бд"""
    conn: Connection = sqlite3.connect(DB_FILE)
    cursor: Cursor = conn.cursor()

    with open(DB_CREATE_FILE) as file:
        sql: str = file.read()
    cursor.execute(sql)
    conn.commit()
    conn.close()


# Test
if __name__ == '__main__':
    Database("Test course", "Test date").save_data()

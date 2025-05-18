import csv
import sqlite3

from src.package_wielkate.main.commons.constants import (DATABASE_NAME,
                                                         COLORS_CSV,
                                                         SQL_CREATE_COLORS_TABLE,
                                                         SQL_INSERT_INTO_COLORS_TABLE
                                                         )


def __get_colors_from_csv__():
    file = open(file=COLORS_CSV, mode='r', encoding='utf-8')
    return [
        [row[0], int(row[1]), int(row[2]), int(row[3])]
        for row in csv.reader(file, delimiter=',')
    ]


def __save_to_database__(data: list):
    with sqlite3.connect(DATABASE_NAME) as connection:
        connection.execute(SQL_CREATE_COLORS_TABLE)
        connection.executemany(SQL_INSERT_INTO_COLORS_TABLE, data)
        connection.commit()
    print(f"Save {len(data)} colors to database")


# main
__save_to_database__(__get_colors_from_csv__())

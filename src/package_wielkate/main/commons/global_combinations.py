import sqlite3

from src.package_wielkate.main.models.Combination import Combination
from src.package_wielkate.main.commons.constants import DATABASE_NAME, SQL_GET_ALL_COMBINATIONS


def __load_combinations__():
    with sqlite3.connect(DATABASE_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute(SQL_GET_ALL_COMBINATIONS)
        combinations = cursor.fetchall()

    print(f'Load {len(combinations)} combinations from database')
    return [Combination(combination) for combination in combinations]


global_combinations = __load_combinations__()

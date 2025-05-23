import logging
import sqlite3

from commons.constants import DATABASE_NAME, SQL_GET_ALL_COMBINATIONS
from models.Combination import Combination

logger = logging.getLogger(__name__)


def __load_combinations__():
    with sqlite3.connect(DATABASE_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute(SQL_GET_ALL_COMBINATIONS)
        combinations = cursor.fetchall()

    logging.info(f'Load {len(combinations)} combinations from database')
    return [Combination(combination) for combination in combinations]


global_combinations = __load_combinations__()

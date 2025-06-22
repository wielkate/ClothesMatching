import logging
import sqlite3
from collections import defaultdict

from src.package_wielkate.main.commons.constants import DATABASE_NAME, SQL_GET_COMBINATIONS_BY_MODE
from src.package_wielkate.main.models.Mode import Mode

logger = logging.getLogger(__name__)


def __load_combinations__(mode):
    with sqlite3.connect(DATABASE_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute(SQL_GET_COMBINATIONS_BY_MODE, (mode,))

        grouped = defaultdict(list)
        for id, base_color, related_color, mode in cursor.fetchall():
            grouped[base_color].append(related_color)

    logging.info(f'Load {len(grouped)} {mode.lower()} combinations from database')
    return grouped


global_monochrome = __load_combinations__(Mode.MONOCHROME.value)
global_complementary = __load_combinations__(Mode.COMPLEMENTARY.value)
global_analogous = __load_combinations__(Mode.ANALOGOUS.value)
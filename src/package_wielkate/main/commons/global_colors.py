import logging
import sqlite3

from src.package_wielkate.main.commons.constants import DATABASE_NAME, SQL_GET_ALL_COLORS
from src.package_wielkate.main.models.Color import Color

logger = logging.getLogger(__name__)


def __load_colors__():
    with sqlite3.connect(DATABASE_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute(SQL_GET_ALL_COLORS)
        colors = cursor.fetchall()

    logger.info(f'Load {len(colors)} colors from database')
    return [Color(color) for color in colors]


global_colors = __load_colors__()

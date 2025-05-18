import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_NAME = os.path.abspath(os.path.join(BASE_DIR, '..', 'database', 'database.db'))

IMAGES_DIRECTORY = 'images/'
COLORS_CSV = '../resources/Colors.csv'

SQL_CREATE_COLORS_TABLE = """
            CREATE TABLE IF NOT EXISTS colors (
                color TEXT PRIMARY KEY,
                r INTEGER NOT NULL,
                g INTEGER NOT NULL,
                b INTEGER NOT NULL 
            )
        """
SQL_CREATE_COMBINATIONS_TABLE = """
            CREATE TABLE IF NOT EXISTS combinations (
                color TEXT PRIMARY KEY,
                monochrome TEXT,
                analogous TEXT,
                complementary TEXT
            )
        """
SQL_CREATE_CLOTHES_TABLE = """
                            CREATE TABLE IF NOT EXISTS clothes (
                                filename TEXT PRIMARY KEY,
                                color TEXT NOT NULL
                            )
                       """

SQL_INSERT_INTO_COLORS_TABLE = """
                INSERT INTO colors 
                (color, r, g, b) 
                VALUES (?, ?, ?, ?)
                """
SQL_INSERT_INTO_COMBINATIONS_TABLE = """
                INSERT INTO combinations
                (color, monochrome, analogous, complementary)
                VALUES (?, ?, ?, ?)
             """
SQL_INSERT_INTO_CLOTHES_TABLE = """
                        INSERT OR REPLACE 
                        INTO clothes (filename, color) 
                        VALUES (?, ?)
                        """

SQL_GET_ALL_COLORS = 'SELECT * FROM colors'
SQL_GET_ALL_COMBINATIONS = 'SELECT * FROM combinations'
SQL_GET_ALL_CLOTHES_ITEMS = 'SELECT * FROM clothes'

SQL_UPDATE_CLOTHES_TABLE = 'UPDATE clothes SET color = ? WHERE filename = ?'

SQL_DELETE_FROM_CLOTHES_TABLE = 'DELETE FROM clothes WHERE filename = ?'

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATABASE_NAME = BASE_DIR.parent / 'database' / 'database.db'
COLORS_CSV = BASE_DIR.parent / 'resources' / 'Colors.csv'

REMOVE_BG_API = 'https://api.pixian.ai/api/v2/remove-background'
CLOTHES_MATCHING_API = 'https://clothes-matching-api.onrender.com'

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
                id INTEGER PRIMARY KEY,
                color TEXT NOT NULL,
                related_color TEXT,
                mode TEXT CHECK (mode IN ('Monochrome', 'Analogous', 'Complementary'))
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
                (color, related_color, mode)
                VALUES (?, ?, ?)
             """
SQL_INSERT_INTO_CLOTHES_TABLE = """
                        INSERT OR REPLACE 
                        INTO clothes (filename, color) 
                        VALUES (?, ?)
                        """

SQL_GET_ALL_COLORS = 'SELECT * FROM colors'
SQL_GET_COMBINATIONS_BY_MODE = """
                                SELECT * FROM combinations
                                WHERE mode = ?
                                """
SQL_GET_ALL_CLOTHES_ITEMS = 'SELECT * FROM clothes'

SQL_UPDATE_CLOTHES_TABLE = 'UPDATE clothes SET color = ? WHERE filename = ?'

SQL_DELETE_FROM_CLOTHES_TABLE = 'DELETE FROM clothes WHERE filename = ?'
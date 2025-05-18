import sqlite3

from src.package_wielkate.main.commons.constants import (DATABASE_NAME,
                                                         SQL_CREATE_CLOTHES_TABLE,
                                                         SQL_GET_ALL_CLOTHES_ITEMS,
                                                         SQL_INSERT_INTO_CLOTHES_TABLE,
                                                         SQL_UPDATE_CLOTHES_TABLE,
                                                         SQL_DELETE_FROM_CLOTHES_TABLE
                                                         )

class Clothes:
    def __init__(self):
        self.database_name = DATABASE_NAME
        self.__init_database__()
        
    def __connect__(self):
        return sqlite3.connect(self.database_name)
    
    def __init_database__(self) -> None:
        with self.__connect__() as connection:
            connection.execute(SQL_CREATE_CLOTHES_TABLE)
            connection.commit()
        print(f'Connect to database {self.database_name}')

    def load_clothes(self) -> list[tuple[str, str]]:
        with self.__connect__() as connection:
            cursor = connection.cursor()
            cursor.execute(SQL_GET_ALL_CLOTHES_ITEMS)
            records = cursor.fetchall()
        print(f'Load {len(records)} clothes items from database')
        return records

    def add(self, filename: str, dominant_color: str) -> None:
        with self.__connect__() as connection:
            connection.execute(SQL_INSERT_INTO_CLOTHES_TABLE,
                               (filename, dominant_color)
                               )
            connection.commit()
        print(f'Add new file {filename} with color {dominant_color} to database')

    def edit(self, filename: str, new_color_name: str) -> None:
        with self.__connect__() as connection:
            connection.execute(SQL_UPDATE_CLOTHES_TABLE,
                               (new_color_name, filename)
                               )
            connection.commit()
        print(f'Edit file\'s {filename} color to {new_color_name} in database')

    def delete(self, filename: str) -> None:
        with self.__connect__() as connection:
            connection.execute(SQL_DELETE_FROM_CLOTHES_TABLE,
                               (filename,)
                               )
            connection.commit()
        print(f'Delete file {filename} from database')

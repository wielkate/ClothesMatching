import json
import os


class Clothes:
    def __init__(self):
        self.filename = 'Clothes.json'
        self.list = self.__load_clothes__()

    def __load_clothes__(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return []
        return []

    def __save__(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(self.list, file, ensure_ascii=False, indent=4)

    def add(self, id, dominant_color) -> None:
        new_item = {'id': id, 'color': dominant_color}
        self.list.append(new_item)
        self.__save__()

    def edit(self, id: str, new_color_name: str) -> None:
        item = next((item for item in self.list if item['id'] == id), None)
        if item:
            item['color'] = new_color_name
            self.__save__()

    def delete(self, id: str) -> None:
        self.list = [item for item in self.list if item['id'] != id]
        self.__save__()

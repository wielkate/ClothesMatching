from flet.core.column import Column
from flet.core.types import ScrollMode

from commons.global_combinations import global_monochrome, global_complementary, global_analogous
from endpoints.endpoints import load_clothes, add_clothing_item, edit_clothing_item, delete_clothing_item
from ui.MatchCard import MatchCard


class MatchCards(Column):
    def __init__(self):
        super().__init__(
            scroll=ScrollMode.HIDDEN,
        )
        self.list = self.load_clothes_from_memory()

    def load_clothes_from_memory(self):
        return [MatchCard(item[0], item[1]) for item in load_clothes()]

    def get_related_colors(self, related_colors, filename, color_name):
        return [item for item in self.list if
                item.color_name in related_colors[color_name] and item.filename != filename]

    def add(self, filename, color_name):
        add_clothing_item(filename, color_name)
        self.list.insert(0, MatchCard(filename, color_name))

    def edit(self, filename, color_name):
        edit_clothing_item(filename, color_name)
        self.list = [
            MatchCard(card.filename, color_name)
            if card.filename == filename
            else MatchCard(card.filename, card.color_name)
            for card in self.list
        ]

    def delete(self, filename):
        delete_clothing_item(filename)
        self.list = [l for l in self.list if l.filename != filename]

    def get_monochrome_for(self, filename, color_name):
        return self.get_related_colors(global_monochrome, filename, color_name)

    def get_analogous_colors_for(self, filename, color_name):
        return self.get_related_colors(global_analogous, filename, color_name)

    def get_complementary_colors_for(self, filename, color_name):
        return self.get_related_colors(global_complementary, filename, color_name)

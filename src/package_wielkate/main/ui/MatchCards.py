from flet.core.column import Column
from flet.core.types import ScrollMode

from src.package_wielkate.main.commons.global_combinations import global_monochrome, global_complementary, global_analogous
from src.package_wielkate.main.models.Clothes import Clothes
from src.package_wielkate.main.ui.MatchCard import MatchCard


class MatchCards(Column):
    def __init__(self):
        super().__init__(
            scroll=ScrollMode.HIDDEN,
        )
        self.clothes = Clothes()
        self.list = self._load_clothes_from_memory()

    def _load_clothes_from_memory(self):
        return [MatchCard(item[0], item[1]) for item in self.clothes.load_clothes()]

    def _get_related_colors(self, related_colors, filename, color_name):
        return [item for item in self.list if
                item.color_name in related_colors[color_name] and item.filename != filename]

    def add(self, filename, color_name):
        self.clothes.add(filename, color_name)
        self.list.insert(0, MatchCard(filename, color_name))

    def edit(self, filename, color_name):
        self.clothes.edit(filename, color_name)
        self.list = [
            MatchCard(card.filename, color_name)
            if card.filename == filename
            else MatchCard(card.filename, card.color_name)
            for card in self.list
        ]

    def delete(self, filename):
        self.clothes.delete(filename)
        self.list = [l for l in self.list if l.filename != filename]

    def get_monochrome_for(self, filename, color_name):
        return self._get_related_colors(global_monochrome, filename, color_name)

    def get_analogous_colors_for(self, filename, color_name):
        return self._get_related_colors(global_analogous, filename, color_name)

    def get_complementary_colors_for(self, filename, color_name):
        return self._get_related_colors(global_complementary, filename, color_name)
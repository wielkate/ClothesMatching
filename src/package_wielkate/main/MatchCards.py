from flet.core.column import Column
from flet.core.types import ScrollMode

from Clothes import Clothes
from MatchCard import MatchCard
from src.package_wielkate.main.Mode import Mode
from src.package_wielkate.main.commons.global_combinations import global_combinations


class MatchCards(Column):
    def __init__(self):
        super().__init__(
            scroll=ScrollMode.HIDDEN,
        )
        self.clothes = Clothes()
        self.list = self._load_clothes_from_memory()

    def _load_clothes_from_memory(self):
        return [MatchCard(item['id'], item['color']) for item in self.clothes.list]

    def _get_related_colors(self, mode, filename, color_name):
        combinations_for_color = [combination for combination in global_combinations
                                  if combination.color_name == color_name][0]

        related_colors = getattr(combinations_for_color, mode.lower(), [])
        return [item for item in self.list if item.color_name in related_colors and item.filename != filename]

    def add(self, filename, color_name):
        self.clothes.add(filename, color_name)
        self.list.insert(0, MatchCard(filename, color_name))

    def edit(self, filename, color_name):
        self.clothes.edit(filename, color_name)

    def delete(self, filename):
        self.clothes.delete(filename)
        self.list = [l for l in self.list if l.filename != filename]

    def get_monochrome_for(self, filename, color_name):
        return self._get_related_colors(Mode.MONOCHROME.value, filename, color_name)

    def get_analogous_colors_for(self, filename, color_name):
        return self._get_related_colors(Mode.ANALOGOUS.value, filename, color_name)

    def get_complementary_colors_for(self, filename, color_name):
        return self._get_related_colors(Mode.COMPLEMENTARY.value, filename, color_name)

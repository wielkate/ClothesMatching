from flet.core.row import Row
from flet.core.types import MainAxisAlignment, ScrollMode

from Clothes import Clothes
from MatchCard import MatchCard
from commons import global_combinations


class MatchCards(Row):
    def __init__(self):
        super().__init__(
            alignment=MainAxisAlignment.SPACE_AROUND,
            scroll=ScrollMode.HIDDEN,
        )
        self.clothes = Clothes()
        self.controls = self._load_clothes_from_memory()

    def _load_clothes_from_memory(self):
        return [MatchCard(item['id'], item['color']) for item in self.clothes.list]

    def add(self, filename, color_name):
        self.clothes.add(filename, color_name)
        self.controls.insert(0, MatchCard(filename, color_name))

    def edit(self, filename, color_name):
        self.clothes.edit(filename, color_name)

    def delete(self, filename):
        self.clothes.delete(filename)
        self.controls = [l for l in self.controls if l.filename != filename]

    def return_monochrome_for(self, color_name):
        combinations_for_color = [combination for combination in global_combinations
                                  if combination.color_name == color_name][0]
        monochrome_colors = combinations_for_color.monochrome
        return [item for item in self.controls if item.color_name in monochrome_colors]
from flet.core.animation import AnimationCurve
from flet.core.row import Row
from flet.core.types import MainAxisAlignment, ScrollMode

from commons.global_clothes import global_clothes
from ui.DisplayCard import DisplayCard


class DisplayCards(Row):
    def __init__(self, delete_card_action, edit_card_action, return_clothes_action):
        super().__init__(
            alignment=MainAxisAlignment.SPACE_AROUND,
            scroll=ScrollMode.HIDDEN,
        )
        self.delete_card_action = delete_card_action
        self.edit_card_action = edit_card_action
        self.return_clothes_action = return_clothes_action
        self.controls = self._load_clothes_from_memory()

    def _load_clothes_from_memory(self):
        return [DisplayCard(self.delete_card_action,
                            self.edit_card_action,
                            self.return_clothes_action,
                            item.filename,
                            item.color_name
                            )
                for item in global_clothes.list][::-1]

    def add_card(self, filename, color_name):
        self.controls.insert(0, DisplayCard(self.delete_card_action,
                                            self.edit_card_action,
                                            self.return_clothes_action,
                                            filename,
                                            color_name
                                            )
                             )
        self.scroll_to(offset=0, duration=2000, curve=AnimationCurve.EASE_IN_OUT)

    def delete_card(self, card):
        self.controls.remove(card)

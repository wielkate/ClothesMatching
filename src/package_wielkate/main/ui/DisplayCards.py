import asyncio

from flet.core.animation import AnimationCurve
from flet.core.row import Row
from flet.core.types import MainAxisAlignment, ScrollMode

from endpoints.endpoints import load_clothes
from ui.DisplayCard import DisplayCard


class DisplayCards(Row):
    def __init__(self, delete_card_action, edit_card_action, return_clothes_action, initial_clothes):
        super().__init__(
            alignment=MainAxisAlignment.SPACE_AROUND,
            scroll=ScrollMode.HIDDEN,
        )
        self.delete_card_action = delete_card_action
        self.edit_card_action = edit_card_action
        self.return_clothes_action = return_clothes_action

    async def load_initial(self):
        clothes = await asyncio.to_thread(load_clothes)
        for filename, color_name in clothes:
            self.add_card(filename, color_name)
        self.update()

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

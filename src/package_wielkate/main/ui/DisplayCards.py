import asyncio

from flet.core.animation import AnimationCurve
from flet.core.row import Row
from flet.core.types import MainAxisAlignment, ScrollMode

from endpoints.endpoints import load_clothes
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

    async def load_initial(self):
        try:
            clothes = await asyncio.to_thread(load_clothes)
            for filename, color_name, tag in clothes:
                self.add_card(filename, color_name, tag)
            self.update()
        except Exception as e:
            print(f"Error loading initial clothes: {e}")

    def add_card(self, filename, color_name, tag):
        self.controls.insert(0, DisplayCard(self.delete_card_action,
                                            self.edit_card_action,
                                            self.return_clothes_action,
                                            filename,
                                            color_name,
                                            tag
                                            )
                             )
        self.scroll_to(offset=0, duration=2000, curve=AnimationCurve.EASE_IN_OUT)

    def delete_card(self, card):
        self.controls.remove(card)

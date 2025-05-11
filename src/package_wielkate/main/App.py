from flet import *
from Card import Card
from Clothes import Clothes


class App(Column):
    # application's root control is a Column containing all other controls
    def __init__(self):
        super().__init__()

        self.scroll = ScrollMode.HIDDEN
        self.expand = True
        self.alignment = MainAxisAlignment.START
        self.cards = self.load_clothes_from_memory()
        self.spacing = 15
        self.controls = [
            Row(
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    Text("Choose item", size=18, weight=FontWeight.NORMAL, color=Colors.WHITE),
                    IconButton(
                        Icons.ADD_CIRCLE_ROUNDED,
                        icon_size=30,
                        on_click=self.add_clicked
                    )
                ]
            ),
            Divider(),
            Row(
                alignment =MainAxisAlignment.SPACE_AROUND,
                scroll=ScrollMode.HIDDEN,
                controls=[
                    self.cards,
                ],
            ),
        ]

    def add_clicked(self, e):
        card = Card(self.card_delete, "", "")
        self.cards.controls.append(card)
        self.update()

    def card_delete(self, card):
        self.cards.controls.remove(card)
        self.update()

    def card_edit(self, e):
        self.update()

    def load_clothes_from_memory(self):
        cards = Row()
        for item in Clothes().list:
            card = Card(self.card_delete, item['id'], item['color'])
            cards.controls.append(card)
        return cards

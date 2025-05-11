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
        self.clothes = Clothes()
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
        card = Card(self.delete_card, self.edit_card, "", "")
        self.cards.controls.append(card)
        self.update()

    def delete_card(self, card):
        self.cards.controls.remove(card)
        self.clothes.delete(card.filename)
        self.update()

    def edit_card(self, card):
        self.clothes.edit(card.filename, card.color_name)
        self.update()

    def load_clothes_from_memory(self):
        cards = Row()
        for item in self.clothes.list:
            card = Card(self.delete_card, self.edit_card, item['id'], item['color'])
            cards.controls.append(card)
        return cards

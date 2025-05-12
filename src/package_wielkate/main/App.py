from flet.core.colors import Colors
from flet.core.column import Column
from flet.core.divider import Divider
from flet.core.icon_button import IconButton
from flet.core.icons import Icons
from flet.core.row import Row
from flet.core.text import Text
from flet.core.types import MainAxisAlignment, ScrollMode, FontWeight

from commons import global_clothes
from Card import Card
from FileUploader import FileUploader


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
                    Text("Choose item or add new", size=18, weight=FontWeight.NORMAL, color=Colors.WHITE),
                    IconButton(
                        Icons.ADD_CIRCLE_ROUNDED,
                        tooltip="Add file",
                        icon_size=30,
                        on_click=self.add_clicked
                    )
                ]
            ),
            Divider(),
            Row(
                alignment=MainAxisAlignment.SPACE_AROUND,
                scroll=ScrollMode.HIDDEN,
                controls=[
                    self.cards,
                ],
            ),
        ]
        self.file_uploader = FileUploader(self.handle_file_processed)

    def add_clicked(self, e):
        self.file_uploader.upload_files()

    def delete_card(self, card):
        global_clothes.delete(card.filename)
        self.cards.controls.remove(card)
        self.update()

    def edit_card(self, card):
        global_clothes.edit(card.filename, card.color_name)
        self.update()

    def load_clothes_from_memory(self):
        cards = Row()
        for item in global_clothes.list:
            card = Card(self.delete_card, self.edit_card, item['id'], item['color'])
            cards.controls.insert(0, card)
        return cards

    def did_mount(self):
        self.file_uploader.attach_to_page(self.page)

    def handle_file_processed(self, filename, color_name):
        global_clothes.add(filename, color_name)
        card = Card(self.delete_card, self.edit_card, filename, color_name)
        self.cards.controls.insert(0, card)
        self.update()

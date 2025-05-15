from flet.core.colors import Colors
from flet.core.column import Column
from flet.core.divider import Divider
from flet.core.icon_button import IconButton
from flet.core.icons import Icons
from flet.core.row import Row
from flet.core.text import Text
from flet.core.types import MainAxisAlignment, ScrollMode, FontWeight

from DisplayCards import DisplayCards
from FileUploader import FileUploader
from to_import import global_clothes


class App(Column):
    # application's root control is a Column containing all other controls
    def __init__(self):
        super().__init__(
            scroll=ScrollMode.HIDDEN,
            expand=True,
            alignment=MainAxisAlignment.START,
            spacing=15
        )
        self.file_uploader = FileUploader(self._add_new_item)
        self.display_cards = DisplayCards(self._delete_card_action, self._edit_card_action)
        self.controls = [
            self._create_header(),
            Divider(),
            self.display_cards,
        ]

    def _create_header(self):
        return Row(
            alignment=MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                Text("Choose item or add new", size=18, weight=FontWeight.NORMAL, color=Colors.WHITE),
                IconButton(
                    Icons.ADD_CIRCLE_ROUNDED,
                    tooltip="Add file",
                    icon_size=30,
                    on_click=self._add_clicked
                )
            ]
        )

    def _add_clicked(self, e):
        self.file_uploader.upload_files()

    def _add_new_item(self, filename, color_name):
        global_clothes.add(filename, color_name)
        self.display_cards.add_card(filename, color_name)
        self.update()

    def _delete_card_action(self, card):
        global_clothes.delete(card.filename)
        self.file_uploader.delete_file(card.filename)
        self.display_cards.delete_card(card)
        self.update()

    def _edit_card_action(self, card):
        global_clothes.edit(card.filename, card.color_name)
        self.update()

    def did_mount(self):
        self.file_uploader.attach_to_page(self.page)

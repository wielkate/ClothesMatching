from flet.core import alignment, padding
from flet.core.border import BorderSide, Border
from flet.core.colors import Colors
from flet.core.column import Column
from flet.core.container import Container
from flet.core.gradients import LinearGradient
from flet.core.icon_button import IconButton
from flet.core.icons import Icons
from flet.core.image import Image
from flet.core.list_tile import ListTile
from flet.core.row import Row
from flet.core.search_bar import SearchBar
from flet.core.stack import Stack
from flet.core.text import Text
from flet.core.types import ClipBehavior, ImageFit, MainAxisAlignment, CrossAxisAlignment, FontWeight, TextAlign

from commons import global_colors, IMAGES_DIRECTORY
from Mode import Mode


class Card(Column):
    def __init__(self, delete_card_action, edit_card_action, filename, color_name):
        super().__init__()
        self.mode = None
        self.filename = filename
        self.color_name = color_name

        self.color_options = self.create_color_options()
        self.mode_options = self.create_mode_options()

        self.delete_card_action = delete_card_action
        self.edit_card_action = edit_card_action

        self.display_card = self.create_display_card()

        self.controls = [self.display_card, self.color_options, self.mode_options]

    def create_display_card(self):
        return Container(
            width=324,
            height=636,
            border_radius=10,
            clip_behavior=ClipBehavior.HARD_EDGE,
            border=Border(
                top=BorderSide(
                    width=1,
                    color=Colors.WHITE,
                ),
                left=BorderSide(
                    width=1,
                    color=Colors.WHITE,
                )
            ),
            content=Stack(
                [
                    # Background image
                    Container(
                        content=Image(
                            src=IMAGES_DIRECTORY + self.filename,
                            fit=ImageFit.COVER,
                            width=324,
                            height=576
                        ),
                    ),
                    # With gradient
                    Container(
                        gradient=LinearGradient(colors=[
                            Colors.TRANSPARENT,
                            Colors.BLACK12,
                            Colors.BLACK
                        ],
                            begin=alignment.top_center,
                            end=alignment.bottom_center,
                            stops=[0.0, 0.5, 0.8]
                        ),
                    ),
                    # Text and icons on top of the gradient
                    Container(
                        padding=padding.only(left=20, right=20, bottom=25),
                        content=
                        Column(
                            alignment=MainAxisAlignment.END,
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            spacing=10,
                            controls=[
                                Text(
                                    self.color_name,
                                    color=Colors.WHITE,
                                    text_align=TextAlign.CENTER,
                                    size=20,
                                    weight=FontWeight.W_900,
                                ),
                                Row(
                                    alignment=MainAxisAlignment.SPACE_AROUND,
                                    controls=[
                                        IconButton(
                                            icon=Icons.CREATE_OUTLINED,
                                            tooltip="Edit color name",
                                            on_click=self.edit_clicked,
                                        ),
                                        IconButton(
                                            icon=Icons.DONE_OUTLINED,
                                            tooltip="Choose",
                                            on_click=self.choose_clicked,
                                        ),
                                        IconButton(
                                            icon=Icons.DELETE_OUTLINE,
                                            tooltip="Delete",
                                            on_click=self.delete_clicked,
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    )
                ]
            ),
        )

    def create_color_options(self):
        return SearchBar(
            visible=False,
            view_leading=IconButton(
                icon=Icons.ARROW_BACK,
                tooltip="Back",
                on_click=self.colors_back_clicked
            ),
            controls=[
                ListTile(title=Text(
                    value=color.name,
                    text_align=TextAlign.CENTER,
                ),
                    on_click=self.select_color,
                    data=color.name,
                )
                for color in global_colors
            ],
        )

    def create_mode_options(self):
        return SearchBar(
            visible=False,
            view_leading=IconButton(
                icon=Icons.ARROW_BACK,
                tooltip="Back",
                on_click=self.modes_back_clicked
            ),
            controls=[
                ListTile(title=Text(
                    value=mode.value,
                    text_align=TextAlign.CENTER,
                ),
                    on_click=self.select_mode,
                    data=mode.value,
                )
                for mode in Mode
            ],
        )

    def edit_clicked(self, e):
        self.color_options.visible = True
        self.color_options.open_view()
        self.update()

    def choose_clicked(self, e):
        self.mode_options.visible = True
        self.mode_options.open_view()
        self.update()

    def select_color(self, e):
        selected_color = e.control.data
        self.display_card.content.controls[2].content.controls[0].value = selected_color
        self.color_name = selected_color
        self.color_options.close_view(selected_color)
        self.color_options.visible = False
        self.edit_card_action(self)
        self.update()

    def select_mode(self, e):
        selected_mode = e.control.data
        self.mode = selected_mode
        self.mode_options.close_view(selected_mode)
        self.mode_options.visible = False
        self.update()

    def colors_back_clicked(self, e):
        self.color_options.close_view()
        self.color_options.visible = False
        self.update()

    def modes_back_clicked(self, e):
        self.mode_options.close_view()
        self.mode_options.visible = False
        self.update()

    def delete_clicked(self, e):
        self.delete_card_action(self)

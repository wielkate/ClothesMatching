import requests
from flet.core import alignment, padding
from flet.core.border import BorderSide, Border
from flet.core.colors import Colors
from flet.core.column import Column
from flet.core.container import Container
from flet.core.gradients import LinearGradient
from flet.core.icon_button import IconButton
from flet.core.icons import Icons
from flet.core.image import Image
from flet.core.row import Row
from flet.core.stack import Stack
from flet.core.text import Text
from flet.core.types import (ClipBehavior,
                             ImageFit,
                             MainAxisAlignment,
                             CrossAxisAlignment,
                             FontWeight,
                             TextAlign,
                             ScrollMode)

from src.package_wielkate.main.commons.constants import CLOTHES_MATCHING_API
from src.package_wielkate.main.commons.global_clothes import global_clothes
from src.package_wielkate.main.models.Mode import Mode
from src.package_wielkate.main.resources.auth import BUCKET_URL
from src.package_wielkate.main.ui.OptionsList import OptionsList


def load_color_names():
    response = requests.get(f'{CLOTHES_MATCHING_API}/get_color_names')
    return [row["color"] for row in response.json()]


class DisplayCard(Column):
    def __init__(self, delete_card_action, edit_card_action, return_clothes_action, filename, color_name):
        super().__init__(
            scroll=ScrollMode.HIDDEN
        )
        self.filename = filename
        self.color_name = color_name
        self.delete_card_action = delete_card_action
        self.edit_card_action = edit_card_action
        self.return_clothes_action = return_clothes_action

        self.color_options = OptionsList(
            items=load_color_names(),
            on_select=self._select_color,
            on_back=lambda e: self._close_options(self.color_options)
        )
        self.mode_options = OptionsList(
            items=[mode.value for mode in Mode],
            on_select=self._select_mode,
            on_back=lambda e: self._close_options(self.mode_options)
        )
        self.display_card = self._create_display_card()
        self.controls = [
            Stack(
                controls=[
                    self.display_card,
                    self.color_options,
                    self.mode_options
                ]
            )
        ]

    def _create_display_card(self):
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
                            src=BUCKET_URL + self.filename + '?',
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
                                            icon=Icons.CREATE_ROUNDED,
                                            tooltip="Edit color name",
                                            on_click=lambda e: self._open_options(self.color_options),
                                        ),
                                        IconButton(
                                            icon=Icons.DONE_ROUNDED,
                                            tooltip="Choose item",
                                            on_click=lambda e: self._open_options(self.mode_options)
                                        ),
                                        IconButton(
                                            icon=Icons.DELETE_OUTLINE_ROUNDED,
                                            tooltip="Delete item",
                                            on_click=self._delete_clicked,
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    )
                ]
            ),
        )

    def _open_options(self, options_list):
        options_list.visible = True
        self.update()

    def _close_options(self, options_list):
        options_list.visible = False
        self.update()

    def _get_matched_items_by(self, mode):
        match mode:
            case Mode.MONOCHROME.value:
                return global_clothes.get_monochrome_for(self.filename, self.color_name)
            case Mode.ANALOGOUS.value:
                return global_clothes.get_analogous_colors_for(self.filename, self.color_name)
            case Mode.COMPLEMENTARY.value:
                return global_clothes.get_complementary_colors_for(self.filename, self.color_name)
            case _:
                return []

    def _select_color(self, e):
        selected_color = e.control.data
        self.color_name = selected_color
        self.display_card.content.controls[2].content.controls[0].value = selected_color
        self._close_options(self.color_options)
        self.edit_card_action(self)
        self.update()

    def _select_mode(self, e):
        selected_mode = e.control.data
        self._close_options(self.mode_options)
        self.return_clothes_action(self._get_matched_items_by(selected_mode))
        self.update()

    def _delete_clicked(self, e):
        self.delete_card_action(self)

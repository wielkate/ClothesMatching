from flet.core import border
from flet.core.colors import Colors
from flet.core.column import Column
from flet.core.container import Container
from flet.core.icon_button import IconButton
from flet.core.icons import Icons
from flet.core.list_tile import ListTile
from flet.core.text import Text
from flet.core.types import ClipBehavior, ScrollMode, TextAlign


class OptionsList(Container):
    def __init__(self, on_select, on_back):
        self.items_column = Column(scroll=ScrollMode.AUTO)
        self.on_select = on_select
        super().__init__(
            visible=False,
            expand=True,
            width=342,
            height=668,
            border_radius=10,
            padding=10,
            clip_behavior=ClipBehavior.HARD_EDGE,
            border=border.all(
                width=1,
                color=Colors.WHITE
            ),
            bgcolor=Colors.BLACK,
            content=Column(
                controls=[
                    IconButton(
                        icon=Icons.ARROW_BACK_ROUNDED,
                        tooltip="Back",
                        on_click=on_back
                    ),
                    # Scrollable list area
                    Container(
                        expand=True,
                        content=self.items_column
                    )
                ],
                expand=True
            )
        )

    def show_items(self, items):
        self.items_column.controls = [
            *[
                ListTile(
                    title=Text(item, text_align=TextAlign.CENTER),
                    data=item,
                    on_click=self.on_select
                )
                for item in items
            ]
        ]
        self.items_column.update()

from flet import Page, Container, Theme, Colors, CrossAxisAlignment, ClipBehavior, app
from flet.core import padding, border
from flet.core.box import BoxConstraints
from flet.core.text_style import TextStyle
from flet.core.theme import IconButtonTheme, IconTheme, DividerTheme, ListTileTheme, SearchBarTheme, SearchViewTheme
from flet.core.types import FontWeight

from App import App


def setup(page):
    font = 'Comfortaa'
    page.fonts = {font: "/fonts/Comfortaa.ttf"}
    page.theme = Theme(font_family=font,
                       icon_button_theme=IconButtonTheme(foreground_color=Colors.WHITE,
                                                         icon_size=30,
                                                         hover_color=Colors.GREY_800
                                                         ),
                       divider_theme=DividerTheme(color=Colors.WHITE30,
                                                  thickness=1),
                       list_tile_theme=ListTileTheme(title_text_style=TextStyle(
                           color=Colors.WHITE,
                           size=20,
                           weight=FontWeight.W_900,
                           font_family=font,
                       )
                       ),
                       # search_bar_theme=SearchBarTheme(
                       #     bgcolor=Colors.BLACK,
                       #     elevation=4,
                       #     text_style=TextStyle(
                       #         color=Colors.WHITE,
                       #         size=20,
                       #         weight=FontWeight.W_900,
                       #     ),
                       #     hint_style=TextStyle(
                       #         color=Colors.WHITE,
                       #         size=20,
                       #         weight=FontWeight.W_900,
                       #     ),
                       #     size_constraints=BoxConstraints(min_width=324, max_width=324, max_height=324)
                       # ),
                       # search_view_theme=SearchViewTheme(
                       #     bgcolor=Colors.BLACK,
                       #     elevation=4,
                       #     header_hint_text_style=TextStyle(
                       #         color=Colors.WHITE,
                       #         size=20,
                       #         weight=FontWeight.W_900,
                       #     ),
                       #     header_text_style=TextStyle(
                       #         color=Colors.WHITE,
                       #         size=20,
                       #         weight=FontWeight.W_900,
                       #     ),
                       #     size_constraints=BoxConstraints(min_width=324, max_width=324)
                       # )
                       )
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.vertical_alignment = CrossAxisAlignment.CENTER
    page.bgcolor = Colors.BLUE_GREY_900


def create_mobile_container():
    return Container(
        width=360,
        height=800,
        bgcolor=Colors.BLACK,
        border_radius=40,
        border=border.all(0.5, Colors.WHITE),
        padding=padding.only(top=35, left=18, right=18, bottom=35),
        clip_behavior=ClipBehavior.HARD_EDGE,
        content=App()
    )


def main(page: Page):
    setup(page)
    page.add(create_mobile_container())
    page.update()


if __name__ == '__main__':
    app(target=main, assets_dir="assets")

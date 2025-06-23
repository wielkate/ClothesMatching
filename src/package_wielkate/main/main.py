from flet import Page, Theme, Colors, CrossAxisAlignment, app
from flet.core.text_style import TextStyle
from flet.core.theme import (IconButtonTheme,
                             DividerTheme,
                             ListTileTheme,
                             TextButtonTheme
                             )
from flet.core.types import FontWeight

from src.package_wielkate.main.ui.MobileApp import MobileApp


def setup(page):
    font = 'Comfortaa'
    page.fonts = {font: "/fonts/Comfortaa.ttf"}
    page.theme = Theme(font_family=font,
                       icon_button_theme=IconButtonTheme(foreground_color=Colors.WHITE,
                                                         icon_size=30,
                                                         hover_color=Colors.GREY_800
                                                         ),
                       text_button_theme=TextButtonTheme(foreground_color=Colors.BLACK,
                                                         text_style=TextStyle(
                                                             weight=FontWeight.W_900,
                                                             font_family=font)
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
                       )
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.vertical_alignment = CrossAxisAlignment.CENTER
    page.bgcolor = Colors.BLUE_GREY_900


def main(page: Page):
    setup(page)
    page.add(MobileApp(page))
    page.update()


if __name__ == '__main__':
    app(target=main, assets_dir="assets")

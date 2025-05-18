from flet import Page, Theme, Colors, CrossAxisAlignment, app
from flet.core.border import BorderSide
from flet.core.box import BoxConstraints
from flet.core.buttons import RoundedRectangleBorder
from flet.core.text_style import TextStyle
from flet.core.theme import IconButtonTheme, DividerTheme, ListTileTheme, SearchViewTheme, SearchBarTheme, \
    TextButtonTheme
from flet.core.types import FontWeight

from MobileApp import MobileApp


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
                       search_bar_theme=SearchBarTheme(
                           bgcolor=Colors.TRANSPARENT,
                       ),
                       search_view_theme=SearchViewTheme(
                           bgcolor=Colors.BLACK,
                           header_hint_text_style=TextStyle(
                               color=Colors.WHITE,
                               size=20,
                               weight=FontWeight.W_900,
                           ),
                           header_text_style=TextStyle(
                               color=Colors.WHITE,
                               size=20,
                               weight=FontWeight.W_900,
                           ),

                           size_constraints=BoxConstraints(min_width=324, max_width=324, min_height=660,
                                                           max_height=660),
                           border_side=BorderSide(
                               width=1,
                               color=Colors.WHITE,
                           ),
                           shape=RoundedRectangleBorder(radius=10)
                       )
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

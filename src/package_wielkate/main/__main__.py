from flet import *

from TodoApp import TodoApp


def main(page: Page):
    font = 'Comfortaa'
    page.fonts = {font: "/fonts/Comfortaa.ttf"}
    page.theme = Theme(font_family=font)
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.vertical_alignment = CrossAxisAlignment.CENTER
    page.bgcolor = Colors.BLUE_GREY_900

    mobile_container = Container(
        width=360,
        height=800,
        bgcolor=Colors.BLACK,
        border_radius=40,
        border=border.all(0.5, Colors.WHITE),
        padding=padding.only(top=35, left=18, right=18, bottom=35),
        clip_behavior=ClipBehavior.HARD_EDGE,
        content=TodoApp()
    )

    page.add(mobile_container)
    page.update()


if __name__ == '__main__':
    app(target=main, assets_dir="assets")
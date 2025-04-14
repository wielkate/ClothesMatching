from flet import *


def main(page: Page):
    t = Text(value="Hello, World!", color="pink", size=60)
    page.controls.append(t)
    page.update()

app(target=main, assets_dir="assets")

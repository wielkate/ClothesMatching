import asyncio
import random

from flet import Container, Colors, ClipBehavior
from flet.core import padding, border
from flet.core.animation import AnimationCurve, Animation
from flet.core.page import Page
from flet.core.stack import Stack

from src.package_wielkate.main.ui.App import App

WELCOME_LETTER_MAP = [
    # W
    (3, 45), (3, 46), (3, 47), (3, 48), (3, 49), (3, 50), (3, 51), (4, 51), (5, 50), (6, 49),
    (7, 50), (8, 51), (9, 51), (9, 50), (9, 49), (9, 48), (9, 47), (9, 46), (9, 45),
    # E
    (11, 45), (11, 46), (11, 47), (11, 48), (11, 49), (11, 50), (11, 51), (12, 45), (13, 45), (14, 45),
    (12, 48), (13, 48), (14, 48), (12, 51), (13, 51), (14, 51),
    # L
    (16, 45), (16, 46), (16, 47), (16, 48), (16, 49), (16, 50), (16, 51), (17, 51), (18, 51), (19, 51),
    # C
    (21, 45), (21, 46), (21, 47), (21, 48), (21, 49), (21, 50), (21, 51), (22, 45), (23, 45), (24, 45),
    (22, 51), (23, 51), (24, 51),
    # O
    (26, 45), (26, 46), (26, 47), (26, 48), (26, 49), (26, 50), (26, 51), (27, 45), (28, 45), (29, 45),
    (27, 51), (28, 51), (29, 51), (30, 45), (30, 46), (30, 47), (30, 48), (30, 49), (30, 50), (30, 51),
    # M
    (32, 45), (32, 46), (32, 47), (32, 48), (32, 49), (32, 50), (32, 51), (33, 46), (34, 47), (35, 46),
    (36, 45), (36, 46), (36, 47), (36, 48), (36, 49), (36, 50), (36, 51),
    # E
    (38, 45), (38, 46), (38, 47), (38, 48), (38, 49), (38, 50), (38, 51), (39, 45), (40, 45), (41, 45),
    (39, 48), (40, 48), (41, 48), (39, 51), (40, 51), (41, 51),
]
SQUARE_SIZE = 7
SPACING = 1


def create_mobile_container(content=None):
    return Container(
        width=360,
        height=800,
        bgcolor=Colors.BLACK,
        border_radius=40,
        border=border.all(0.5, Colors.WHITE),
        padding=padding.only(top=35, left=18, right=18, bottom=35),
        clip_behavior=ClipBehavior.HARD_EDGE,
        content=content,
    )


def create_animated_square():
    return Container(
        width=SQUARE_SIZE,
        height=SQUARE_SIZE,
        bgcolor=Colors.WHITE,
        border_radius=2,
        left=random.randint(10, 330),
        top=random.randint(10, 700),
        animate_position=Animation(2000, curve=AnimationCurve.EASE_IN_OUT),
        animate_opacity=1000
    )


def created_animated_squares():
    return [create_animated_square() for _, _ in WELCOME_LETTER_MAP]


class MobileApp(Stack):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        self.app = create_mobile_container(App(self.page))
        self.squares = created_animated_squares()
        self.controls = [create_mobile_container(), *self.squares]

    def did_mount(self):
        self.page.run_task(self.start_app)

    async def start_app(self):
        await asyncio.sleep(0.5)
        self.show_welcome_animation()
        await asyncio.sleep(4)
        self.fade_out_squares()
        await asyncio.sleep(0.1)
        await self.fade_in_app()

    def show_welcome_animation(self):
        for i, square in enumerate(self.squares):
            target_x, target_y = WELCOME_LETTER_MAP[i]
            square.left = target_x * (SQUARE_SIZE + SPACING)
            square.top = target_y * (SQUARE_SIZE + SPACING)
            square.update()

    def fade_out_squares(self):
        for square in self.squares:
            square.opacity = 0
            square.update()

    async def fade_in_app(self):
        self.controls.append(self.app)
        self.update()
        await asyncio.sleep(0.1)
        self.app.content.opacity = 1.0
        self.app.update()

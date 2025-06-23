import asyncio
import random

from flet import Container, Colors, ClipBehavior
from flet.core import padding
from flet.core.animation import AnimationCurve, Animation
from flet.core.page import Page
from flet.core.stack import Stack

from ui.App import App

WELCOME_LETTER_MAP = [
    # W
    (3, 40), (3, 41), (3, 42), (3, 43), (3, 44), (3, 45), (3, 46), (4, 46), (5, 45), (6, 44),
    (7, 45), (8, 46), (9, 46), (9, 45), (9, 44), (9, 43), (9, 42), (9, 41), (9, 40),
    # E
    (11, 40), (11, 41), (11, 42), (11, 43), (11, 44), (11, 45), (11, 46), (12, 40), (13, 40), (14, 40),
    (12, 43), (13, 43), (14, 43), (12, 46), (13, 46), (14, 46),
    # L
    (16, 40), (16, 41), (16, 42), (16, 43), (16, 44), (16, 45), (16, 46), (17, 46), (18, 46), (19, 46),
    # C
    (21, 40), (21, 41), (21, 42), (21, 43), (21, 44), (21, 45), (21, 46), (22, 40), (23, 40), (24, 40),
    (22, 46), (23, 46), (24, 46),
    # O
    (26, 40), (26, 41), (26, 42), (26, 43), (26, 44), (26, 45), (26, 46), (27, 40), (28, 40), (29, 40),
    (27, 46), (28, 46), (29, 46), (30, 40), (30, 41), (30, 42), (30, 43), (30, 44), (30, 45), (30, 46),
    # M
    (32, 40), (32, 41), (32, 42), (32, 43), (32, 44), (32, 45), (32, 46), (33, 41), (34, 42), (35, 41),
    (36, 40), (36, 41), (36, 42), (36, 43), (36, 44), (36, 45), (36, 46),
    # E
    (38, 40), (38, 41), (38, 42), (38, 43), (38, 44), (38, 45), (38, 46), (39, 40), (40, 40), (41, 40),
    (39, 43), (40, 43), (41, 43), (39, 46), (40, 46), (41, 46),
]
SQUARE_SIZE = 7
SPACING = 2


def create_mobile_container(content=None):
    return Container(
        expand=True,
        padding=padding.only(top=45, left=18, right=18, bottom=25),
        clip_behavior=ClipBehavior.HARD_EDGE,
        content=content,
    )


def create_animated_square():
    return Container(
        width=SQUARE_SIZE,
        height=SQUARE_SIZE,
        bgcolor=Colors.WHITE,
        border_radius=2,
        left=random.randint(10, 430),
        top=random.randint(10, 800),
        animate_position=Animation(2000, curve=AnimationCurve.EASE_IN_OUT),
        animate_opacity=1000
    )


def created_animated_squares():
    return [create_animated_square() for _ in WELCOME_LETTER_MAP]


class MobileApp(Stack):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        self.app = create_mobile_container(App(self.page))
        self.squares = created_animated_squares()
        self.controls = [create_mobile_container(), *self.squares]
        self.expand = True

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
        self.controls = [self.app]
        self.update()
        await asyncio.sleep(0.1)
        self.app.content.opacity = 1.0
        self.app.update()

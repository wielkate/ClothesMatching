from flet.core.border import BorderSide, Border
from flet.core.box import DecorationImage
from flet.core.colors import Colors
from flet.core.column import Column
from flet.core.container import Container
from flet.core.types import ClipBehavior, ImageFit

from constants import IMAGES_DIRECTORY


class MatchCard(Column):
    def __init__(self, filename, color_name):
        super().__init__()
        self.filename = filename
        self.color_name = color_name
        self.card = self.create_card()

    def create_card(self):
        return Container(
            width=324,
            height=576,
            border_radius=10,
            clip_behavior=ClipBehavior.HARD_EDGE,
            image=DecorationImage(
                            src=IMAGES_DIRECTORY + self.filename,
                            fit=ImageFit.COVER,
                        ),
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
        )

from flet.core.border import BorderSide, Border
from flet.core.box import DecorationImage
from flet.core.colors import Colors
from flet.core.container import Container
from flet.core.types import ClipBehavior, ImageFit

from resources.auth import BUCKET_URL


class MatchCard(Container):
    def __init__(self, filename, color_name):
        super().__init__(
            width=342,
            height=608,
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

        )
        self.filename = filename
        self.color_name = color_name
        self.image = DecorationImage(
            src=BUCKET_URL + self.filename,
            fit=ImageFit.COVER,
        )

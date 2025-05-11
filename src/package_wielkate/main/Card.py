from flet import *


class Card(Column):
    def __init__(self, delete_card, filename, color_name):
        super().__init__()

        self.filename = filename
        self.original_color_name = color_name
        self.edit_color_name = TextField(
            border=InputBorder.UNDERLINE,
            color=Colors.WHITE)

        self.delete_card = delete_card
        self.display_card = self.create_card_with_name(self.original_color_name)

        self.display_view = Row(
            alignment=MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=CrossAxisAlignment.CENTER,
            controls=[
                self.display_card
            ],
        )

        self.edit_view = Row(
            visible=False,
            alignment=MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=CrossAxisAlignment.CENTER,
            controls=[
                self.edit_color_name,
                IconButton(
                    icon=Icons.DONE_OUTLINE_OUTLINED,
                    icon_color=Colors.GREEN,
                    tooltip="Save",
                    on_click=self.save_color_name_clicked,
                ),
            ],
        )
        self.controls = [self.display_view, self.edit_view]

    def create_card_with_name(self, color_name):
        return Container(
            width=324,
            height=636,
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
            content=Stack(
                [
                    # Background image
                    Container(
                        content=Image(
                            src="images/" + self.filename,
                            fit=ImageFit.COVER,
                            width=324,
                            height=576
                        ),
                    ),
                    # With gradient
                    Container(
                        gradient=LinearGradient(colors=[
                            Colors.TRANSPARENT,
                            Colors.BLACK12,
                            Colors.BLACK
                        ],
                            begin=alignment.top_center,
                            end=alignment.bottom_center,
                            stops=[0.0, 0.5, 0.8]
                        ),
                    ),
                    # Text and icons on top of the gradient
                    Container(
                        padding=padding.only(left=20, right=20, bottom=25),
                        content=
                        Column(
                            alignment=MainAxisAlignment.END,
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            spacing=10,
                            controls=[
                                Text(
                                    color_name,
                                    color=Colors.WHITE,
                                    text_align=TextAlign.CENTER,
                                    size=20,
                                    weight=FontWeight.W_900,
                                ),
                                Row(
                                    alignment=MainAxisAlignment.SPACE_AROUND,
                                    controls=[
                                        IconButton(
                                            icon=Icons.CREATE_OUTLINED,
                                            tooltip="Edit color name",
                                            on_click=self.edit_clicked,
                                        ),
                                        IconButton(
                                            icon=Icons.DONE_OUTLINED,
                                            tooltip="Choose",
                                            # on_click=self,
                                        ),
                                        IconButton(
                                            icon=Icons.DELETE_OUTLINE,
                                            tooltip="Delete",
                                            on_click=self.delete_clicked,
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    )
                ]
            ),
        )

    def edit_clicked(self, e):
        self.edit_color_name.value = self.display_card.content.controls[2].content.controls[0].value
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    def save_color_name_clicked(self, e):
        self.display_card.content.controls[2].content.controls[0].value = self.edit_color_name.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()

    def delete_clicked(self, e):
        self.delete_card(self)

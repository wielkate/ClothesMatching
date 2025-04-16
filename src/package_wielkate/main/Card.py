from flet import *

def get_card(filename, colorname):
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
                # Background image with gradient
                Container(
                    content=Image(
                        src="images/" + filename,
                        fit=ImageFit.COVER,
                        width=324,
                        height=576
                    ),
                ),
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
                                colorname,
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
                                        tooltip="Edit To-Do",
                                        on_click=Task.edit_clicked,
                                    ),
                                    IconButton(
                                        Icons.DELETE_OUTLINE,
                                        tooltip="Delete To-Do",
                                        on_click=Task.delete_clicked,
                                    ),
                                    Icon(Icons.ADD, color="0xFFFFFFFF"),
                                ],
                            ),
                        ],
                    ),
                )
            ]
        ),
    )


class Task(Column):
    def __init__(self, task_name, task_delete, filename, color_name):
        super().__init__()
        self.task_name = task_name
        self.task_delete = task_delete
        self.display_task = Checkbox(value=False, label=self.task_name)
        self.edit_name = TextField(expand=1)

        self.display_view = Row(
            alignment=MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=CrossAxisAlignment.CENTER,
            controls=[
                get_card(filename, color_name)
            ],
        )

        self.edit_view = Row(
            visible=False,
            alignment=MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=CrossAxisAlignment.CENTER,
            controls=[
                self.edit_name,
                IconButton(
                    icon=Icons.DONE_OUTLINE_OUTLINED,
                    icon_color=Colors.GREEN,
                    tooltip="Update To-Do",
                    on_click=self.save_clicked,
                ),
            ],
        )
        self.controls = [self.display_view, self.edit_view]

    def edit_clicked(self, e):
        self.edit_name.value = self.display_task.label
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    def save_clicked(self, e):
        self.display_task.label = self.edit_name.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()

    def delete_clicked(self, e):
        self.task_delete(self)


from flet import *
from Card import Task
from Clothes import Clothes


class TodoApp(Column):
    # application's root control is a Column containing all other controls
    def __init__(self):
        super().__init__()

        self.scroll = ScrollMode.HIDDEN
        self.expand = True
        self.alignment = MainAxisAlignment.START
        self.tasks = self.load_tasks()
        self.spacing = 15
        self.controls = [
            Row(
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    Text("Choose item", size=18, weight=FontWeight.NORMAL, color=Colors.WHITE),
                    IconButton(
                        Icons.ADD_CIRCLE_ROUNDED,
                        icon_size=30,
                        icon_color=Colors.WHITE,
                        on_click=self.add_clicked
                    )
                ]
            ),
            Divider(height=8, color=Colors.WHITE30),
            Row(
                alignment =MainAxisAlignment.SPACE_AROUND,
                scroll=ScrollMode.HIDDEN,
                controls=[
                    self.tasks,
                ],
            ),
        ]

    def add_clicked(self, e):
        task = Task("", self.task_delete)
        self.tasks.controls.append(task)
        self.update()

    def task_delete(self, task):
        self.tasks.controls.remove(task)
        self.update()

    def tabs_changed(self, e):
        self.update()

    def load_tasks(self):
        tasks = Row()
        for item in Clothes().list:
            task = Task("", self.task_delete, item['id'], item['color'])
            tasks.controls.append(task)
        return tasks

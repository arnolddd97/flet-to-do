import flet as ft

#felhasználói vezérlés elszigetelt komponensek újrafelhazsnálható
class Todo(ft.UserControl):
    #self maga az komponens és annak tudsz adni elemeket
    def build(self):
        self.new_task = ft.TextField(hint_text="Mit csináljunk?", expand=True)
        self.tasks = ft.Column()

        return ft.Column(
            width=600,
            controls=[
                ft.Row(
                    controls=[
                        self.new_task,
                        ft.FloatingActionButton(icon=ft.icons.ADD, on_click=self.add_clicked),
                    ],
                ),
                self.tasks,
            ],
        )

    def add_clicked(self, e):
        self.tasks.controls.append(ft.Checkbox(label=self.new_task.value))
        self.new_task.value = ""
        self.update()

def main(page : ft.Page):
    page.title = "To-do alkalmazás"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    todo = Todo()
    todo2 = Todo()

    page.add(todo)
    page.add(todo2)



ft.app(target=main)
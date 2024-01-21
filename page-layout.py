import flet as ft

def pageLayout(page : ft.Page):
    def add_clicked(e):
        tasks_view.controls.append(ft.Checkbox(label=new_task.value))
        new_task.value = "Mit csináljunk?"
        view.update()

#input mező
    #expand kitölti a teret max width
    new_task = ft.TextField(hint_text="Mit csináljunk?", expand=True)

    #view ami column, column tulajdonsága, hogy egymás alá rakja a dolgokat.
    tasks_view = ft.Column()
    #view, ami ami szintén column bárnmiut hozá adunk egymás alá pakolja
    view = ft.Column(
        # sazélesség
        width=600,
        # view, ami ami szintén column
        controls=[
            #HOZZÁ ADJUK 1 SORT + TASK VIEW, COLUMN AZ TARTALMATHAT COLUMN MÉG +-BA, meg rowot Column és Row controls-ban adjuk meg
            ft.Row(
                controls=[
                    new_task,
                    ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_clicked),
                ],
            ),
            ft.Text("Csak egy sima szöveg"),
            tasks_view,

        ],
    )
    #oldal középre van rendezve
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(view)

ft.app(target=pageLayout)
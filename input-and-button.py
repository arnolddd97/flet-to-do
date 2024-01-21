import flet as ft
def main(page : ft.Page):
    #action mi történjen
    def add_clicked(e):
        page.add(ft.Checkbox(label=input.value))
        input.value=""
        page.update() #frissítés



    input = ft.TextField(hint_text="Mit csináljunk?")

    #FloatingActionButton lebegő gomb, aminek van iconja + action
    page.add(input, ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_clicked))

ft.app(target=main)
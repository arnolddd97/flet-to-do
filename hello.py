#első project

import flet as ft
#flet import


#Main függvény
def main(page: ft.Page):
    #page-nek adni egy flet Text objektumot
    page.add(ft.Text(value="Hello, world!"))

#tartget átadni a maint
ft.app(target=main)


#flet -r hello.py
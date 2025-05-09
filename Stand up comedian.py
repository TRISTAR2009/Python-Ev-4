import flet as ft
import random

def main(page: ft.Page):
    jokes = [
        "Why don't skeletons fight each other? Because they don't have the guts",
        "Why did the math book look sad? Because it had too many problems",
        "Why can’t you give Elsa a balloon? Because she will let it go",
        "How do you organize a space party? You planet",
        "What do you call fake spaghetti? An impasta",
        "Why did the golfer bring two pants? In case he got a hole in one",
        "Why was the broom late? It swept in",
        "What do you call a bear with no teeth? A gummy bear",
        "What kind of tree fits in your hand? A palm tree",
        "Why did the scarecrow win an award? Because he was outstanding in his field",
    ]

    joke_text = ft.Text(value="", size=20, text_align=ft.TextAlign.CENTER)

    def close(e):
        sheet.open = False
        page.update()

    close_btn = ft.TextButton("Close", on_click=close)

    sheet = ft.BottomSheet(ft.Container(content=ft.Column([
                    joke_text,
                    close_btn,
                ],
                tight=True,
            ),
        ),
        open=False,
    )

    sheet = ft.BottomSheet(
        ft.Container(
            content=ft.Column([
                    joke_text,
                    close_btn,
                ],
                tight=True,
            ),
            padding=20,
        ),
        open=False,
    )

    page.overlay.append(sheet)

    def tell_joke(e):
        joke = random.choice(jokes)
        joke_text.value = joke
        sheet.open = True
        page.update()

    joke = ft.ElevatedButton(text="Tell me a joke", on_click=tell_joke)

    page.add(
        ft.Column(
            controls=[joke],
            expand=True,
        )
    )

ft.app(target=main)

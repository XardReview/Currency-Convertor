import flet as ft
from conversion import *

previous_exchange_rates = {}


def main(page: ft.Page):
    page.title = "Конвертор валют"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_icon = "Icons/Currency_Exchange.ico"

    def convert(e):
        currency = currency_input.value
        try:
            amount = float(amount_input.value)
        except ValueError:
            result_text.value = "Введите корректное число."
            page.update()
            return

        if direction_input.value == "To RUB":
            if currency == "USD":
                rub_amount = usd_to_rub(amount)
            elif currency == "EUR":
                rub_amount = eur_to_rub(amount)
            elif currency == "UZS":
                rub_amount = uzs_to_rub(amount)
            elif currency == "CNY":
                rub_amount = cny_to_rub(amount)
            elif currency == "INR":
                rub_amount = inr_to_rub(amount)
            elif currency == "KZT":
                rub_amount = kzt_to_rub(amount)
            else:
                rub_amount = None

            if rub_amount is not None:
                if currency == "USD":
                    result_text.value = f"{amount} Долларов США = {round(rub_amount, 2)} рублей"
                elif currency == "EUR":
                    result_text.value = f"{amount} Евро = {round(rub_amount, 2)} рублей"
                elif currency == "UZS":
                    result_text.value = f"{amount} Узбекских сум = {round(rub_amount, 2)} рублей"
                elif currency == "CNY":
                    result_text.value = f"{amount} Китайских юаней = {round(rub_amount, 2)} рублей"
                elif currency == "INR":
                    result_text.value = f"{amount} Индийских рупий = {round(rub_amount, 2)} рублей"
                elif currency == "KZT":
                    result_text.value = f"{amount} Казахских тенге = {round(rub_amount, 2)} рублей"
            else:
                result_text.value = "Не удалось получить актуальный курс обмена. Проверьте соединение с Интернетом или корректность ввода."
        else:
            if currency == "USD":
                foreign_amount = rub_to_usd(amount)
            elif currency == "EUR":
                foreign_amount = rub_to_eur(amount)
            elif currency == "UZS":
                foreign_amount = rub_to_uzs(amount)
            elif currency == "CNY":
                foreign_amount = rub_to_cny(amount)
            elif currency == "INR":
                foreign_amount = rub_to_inr(amount)
            elif currency == "KZT":
                foreign_amount = rub_to_kzt(amount)
            else:
                foreign_amount = None

            if foreign_amount is not None:
                if currency == "USD":
                    result_text.value = f"{amount} рублей = {round(foreign_amount, 2)} Долларов США"
                if currency == "EUR":
                    result_text.value = f"{amount} рублей = {round(foreign_amount, 2)} Евро"
                if currency == "UZS":
                    result_text.value = f"{amount} рублей = {round(foreign_amount, 2)} Узбекских сум"
                if currency == "CNY":
                    result_text.value = f"{amount} рублей = {round(foreign_amount, 2)} Китайских юаней"
                if currency == "INR":
                    result_text.value = f"{amount} рублей = {round(foreign_amount, 2)} Индийских рупий"
                if currency == "KZT":
                    result_text.value = f"{amount} рублей = {round(foreign_amount, 2)} Казахских тенге"
            else:
                result_text.value = "Не удалось получить актуальный курс обмена. Проверьте соединение с Интернетом или корректность ввода."

        page.update()

    def restart(e):
        direction_input.value = ""
        currency_input.value = ""
        amount_input.value = ""
        result_text.value = ""
        update_exchange_rates()
        page.update()

    def update_exchange_rates():
        global previous_exchange_rates

        def get_rate_and_icon(currency_code):
            new_rate = get_exchange_rate(currency_code)
            previous_rate = previous_exchange_rates.get(currency_code, new_rate)
            if new_rate > previous_rate:
                icon_path = "Sort Up.png"
            elif new_rate < previous_rate:
                icon_path = "Sort Down.png"
            else:
                icon_path = "Minus.png"  # Add a neutral icon if needed
            previous_exchange_rates[currency_code] = new_rate
            return new_rate, icon_path

        usd_rate, usd_icon = get_rate_and_icon('USD')
        eur_rate, eur_icon = get_rate_and_icon('EUR')
        uzs_rate, uzs_icon = get_rate_and_icon('UZS')
        cny_rate, cny_icon = get_rate_and_icon('CNY')
        inr_rate, inr_icon = get_rate_and_icon('INR')
        kzt_rate, kzt_icon = get_rate_and_icon('KZT')

        usd_exchange_rate_text.value = f"Доллар США = {round(usd_rate, 2)}"
        usd_exchange_rate_icon.src = usd_icon

        eur_exchange_rate_text.value = f"Евро = {round(eur_rate, 2)}"
        eur_exchange_rate_icon.src = eur_icon

        uzs_exchange_rate_text.value = f"Узбекские сумы = {round(uzs_rate, 2)}"
        uzs_exchange_rate_icon.src = uzs_icon

        cny_exchange_rate_text.value = f"Китайские юани = {round(cny_rate, 2)}"
        cny_exchange_rate_icon.src = cny_icon

        inr_exchange_rate_text.value = f"Индийские рупии = {round(inr_rate, 2)}"
        inr_exchange_rate_icon.src = inr_icon

        kzt_exchange_rate_text.value = f"Казахские тенге = {round(kzt_rate, 2)}"
        kzt_exchange_rate_icon.src = kzt_icon

        page.update()

    currency_input = ft.Dropdown(
        label="Валюта",
        options=[
            ft.dropdown.Option(key="USD", text="Доллары США"),
            ft.dropdown.Option(key="EUR", text="Евро"),
            ft.dropdown.Option(key="UZS", text="Узбекские сумы"),
            ft.dropdown.Option(key="CNY", text="Китайские юани"),
            ft.dropdown.Option(key="INR", text="Индийские рупии"),
            ft.dropdown.Option(key="KZT", text="Казахские тенге")
        ],
        width=200
    )
    direction_input = ft.Dropdown(
        label="Направление конвертации",
        options=[
            ft.dropdown.Option(key="To RUB", text="В рубли"),
            ft.dropdown.Option(key="From RUB", text="Из рублей")
        ],
        width=200
    )
    amount_input = ft.TextField(label="Сумма", width=200)
    convert_button = ft.ElevatedButton(text="Конвертировать", on_click=convert)
    restart_button = ft.ElevatedButton(text="Перезапуск", on_click=restart)
    result_text = ft.Text(style=ft.TextStyle(font_family="Arial", size=16))

    usd_exchange_rate_text = ft.Text(style=ft.TextStyle(font_family="Arial", size=16))
    usd_exchange_rate_icon = ft.Image(src="Minus.png", width=20, height=20)

    eur_exchange_rate_text = ft.Text(style=ft.TextStyle(font_family="Arial", size=16))
    eur_exchange_rate_icon = ft.Image(src="Minus.png", width=20, height=20)

    uzs_exchange_rate_text = ft.Text(style=ft.TextStyle(font_family="Arial", size=16))
    uzs_exchange_rate_icon = ft.Image(src="Minus.png", width=20, height=20)

    cny_exchange_rate_text = ft.Text(style=ft.TextStyle(font_family="Arial", size=16))
    cny_exchange_rate_icon = ft.Image(src="Minus.png", width=20, height=20)

    inr_exchange_rate_text = ft.Text(style=ft.TextStyle(font_family="Arial", size=16))
    inr_exchange_rate_icon = ft.Image(src="Minus.png", width=20, height=20)

    kzt_exchange_rate_text = ft.Text(style=ft.TextStyle(font_family="Arial", size=16))
    kzt_exchange_rate_icon = ft.Image(src="Minus.png", width=20, height=20)

    update_exchange_rates()

    page.add(
        ft.Row(
            [
                ft.Column(
                    [
                        ft.Container(direction_input, alignment=ft.alignment.center),
                        ft.Container(currency_input, alignment=ft.alignment.center),
                        ft.Container(amount_input, alignment=ft.alignment.center),
                        ft.Container(convert_button, alignment=ft.alignment.center),
                        ft.Container(restart_button, alignment=ft.alignment.center),
                        ft.Container(result_text, alignment=ft.alignment.center),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=10,
                    expand=True
                ),
                ft.Container(
                    ft.Column(
                        [
                            ft.Row([usd_exchange_rate_text, usd_exchange_rate_icon], alignment=ft.MainAxisAlignment.CENTER, spacing=5),
                            ft.Row([eur_exchange_rate_text, eur_exchange_rate_icon], alignment=ft.MainAxisAlignment.CENTER, spacing=5),
                            ft.Row([uzs_exchange_rate_text, uzs_exchange_rate_icon], alignment=ft.MainAxisAlignment.CENTER, spacing=5),
                            ft.Row([cny_exchange_rate_text, cny_exchange_rate_icon], alignment=ft.MainAxisAlignment.CENTER, spacing=5),
                            ft.Row([inr_exchange_rate_text, inr_exchange_rate_icon], alignment=ft.MainAxisAlignment.CENTER, spacing=5),
                            ft.Row([kzt_exchange_rate_text, kzt_exchange_rate_icon], alignment=ft.MainAxisAlignment.CENTER, spacing=5),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=10,
                    ),
                    alignment=ft.alignment.center_right,
                    expand=True
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            expand=True
        )
    )


ft.app(target=main)

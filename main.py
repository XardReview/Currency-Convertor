import flet as ft
from conversion import *


def main(page: ft.Page):
    page.title = "Currency Converter"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
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
        usd_exchange_rate_text.value = f"Доллар США = {round(get_exchange_rate('USD'), 2)}"
        eur_exchange_rate_text.value = f"Евро = {round(get_exchange_rate('EUR'), 2)}"
        uzs_exchange_rate_text.value = f"Узбекские сумы = {round(get_exchange_rate('UZS'), 2)}"
        cny_exchange_rate_text.value = f"Китайские юани = {round(get_exchange_rate('CNY'), 2)}"
        inr_exchange_rate_text.value = f"Индийские рупии = {round(get_exchange_rate('INR'), 2)}"
        kzt_exchange_rate_text.value = f"Казахские тенге = {round(get_exchange_rate('KZT'), 2)}"
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
    eur_exchange_rate_text = ft.Text(style=ft.TextStyle(font_family="Arial", size=16))
    uzs_exchange_rate_text = ft.Text(style=ft.TextStyle(font_family="Arial", size=16))
    cny_exchange_rate_text = ft.Text(style=ft.TextStyle(font_family="Arial", size=16))
    inr_exchange_rate_text = ft.Text(style=ft.TextStyle(font_family="Arial", size=16))
    kzt_exchange_rate_text = ft.Text(style=ft.TextStyle(font_family="Arial", size=16))

    update_exchange_rates()

    page.add(
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
        )
    )

    page.add(
        ft.Container(
            ft.Row(
                [
                    usd_exchange_rate_text,
                    eur_exchange_rate_text,
                    uzs_exchange_rate_text,
                    cny_exchange_rate_text,
                    inr_exchange_rate_text,
                    kzt_exchange_rate_text
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10
            ),
            alignment=ft.alignment.bottom_center
        )
    )


ft.app(target=main)

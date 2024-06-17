from exchange_rates import *
def run_currency_conversion():
    print("Доступные к конвертации валюты (Вся конвертация происходит из валют в рубли):")
    print("Нажмите '1', чтобы конвертировать Доллар США")
    print("Нажмите '2', чтобы конвертировать Евро")
    print("Нажмите '3', чтобы конвертировать Узбекские сумы")
    print("Нажмите '4', чтобы конвертировать Китайские юани")
    currency = int(input())
    if currency == 1:
        usd_amount = float(input("Введите сумму в долларах США: "))
        rub_amount = usd_to_rub(usd_amount)

        if rub_amount is not None:
            print(f"{usd_amount} долларов США = {round(rub_amount, 2)} рублей")
        else:
            print("Не удалось получить актуальный курс обмена с Центрального банка России, проверьте соединение с Интернетом.")
    elif currency == 2:
        eur_amount = float(input("Введите сумму в евро: "))
        rub_amount = eur_to_rub(eur_amount)

        if rub_amount is not None:
            print(f"{eur_amount} евро = {round(rub_amount, 2)} рублей")
        else:
            print("Не удалось получить актуальный курс обмена с Центрального банка России, проверьте соединение с Интернетом.")
    if currency == 3:
        uzs_amount = float(input("Введите сумму в узбекских сумах: "))

        rub_amount = uzs_to_rub(uzs_amount)

        if rub_amount is not None:
            print(f"{uzs_amount} узбекских сумов = {round(rub_amount, 2)} рублей")
        else:
            print("Не удалось получить актуальный курс обмена с Центрального банка России, проверьте соединение с Интернетом.")
    if currency == 4:
        cny_amount = float(input("Введите сумму в китайских юанях: "))
        rub_amount = cny_to_rub(cny_amount)

        if rub_amount is not None:
            print(f"{cny_amount} узбекских сум = {round(rub_amount, 2)} рублей")
        else:
            print("Не удалось получить актуальный курс обмена с Центрального банка России, проверьте соединение с Интернетом.")
def check_restart():
    while True:
        print("Напечатайте '+', если хотите повторить операцию, '-', если хотите закрыть приложение.")
        user_input = input()
        if user_input == '-':
            print("Программа завершена.")
            return False
        elif user_input == '+':
            print("Перезапуск программы...")
            return True
        else:
            print("Неверная команда. Попробуйте снова.")

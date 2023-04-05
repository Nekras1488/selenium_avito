import json
import random
from notifiers import get_notifier
import time
from index import get_func

token = "6256920799:AAELDHUaXK3bI8D4yME3kQ87DF1dMuxPWN8"


def func():
    url_russian = "https://www.avito.ru/bryansk/avtomobili/vaz_lada-ASgCAQICAUDgtg0Uxpko?cd=1&f=ASgCAQECAkDgtg0Uxpko4rYN9BjWmijYmijamijcmijemijgmii6nCjwpijCqCiKqSiqrSjCsyjEsyj0tCj2tCji8jKO8zKcyTaeyTaO0zmQ0znuyz~gkky0iJQBAUXGmgwVeyJmcm9tIjowLCJ0byI6ODAwMDB9&p=1&radius=200&s=104&searchRadius=200"
    url_inomarki = "https://www.avito.ru/bryansk/avtomobili?cd=1&f=ASgBAQECAUTyCrKKAQFA4LYNFKSKNAFFxpoMG3siZnJvbSI6MTAwMDAwLCJ0byI6MzAwMDAwfQ&radius=200&s=104&searchRadius=200"
    count = 1
    while True:
        if count % 2 == 0:
            filik = "ssilki.txt"
            get_func(url_russian, filik)
        else:
            filik = "ssilki_inom.txt"
            get_func(url_inomarki, filik)
        with open("new_car.json", "r", encoding="utf-8") as file:
            opa = json.load(file)
        for i in opa:
            telegram = get_notifier("telegram")
            telegram.notify(token=token, chat_id="786013248",
                            message=f"Цена: {i['Цена']}\nНазвание: {i['Название']}\n{i['Ссылка']}\n{'Бебруха'}")
            telegram.notify(token=token, chat_id="1185052543",
                            message=f"Цена: {i['Цена']}\nНазвание: {i['Название']}\n{i['Ссылка']}")
            time.sleep(5)
        time.sleep(random.randint(30, 60))
        count += 1


def main():
    func()


if __name__ == "__main__":
    main()

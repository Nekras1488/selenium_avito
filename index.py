import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup


def get_func(url, filik):
    json_data = []
    with open(filik, "r", encoding="utf-8") as gg:
        spis = gg.readlines()
    s = Service("chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--headless")

    driver = webdriver.Chrome(
        service=s,
        options=options
    )
    try:
        driver.get(url)
        time.sleep(3)
        with open(f"russian_car.html", "w", encoding="utf-8") as file:
            file.write(driver.page_source)
        with open(f"russian_car.html", "r", encoding="utf-8") as f:
            src = f.read()
        soup = BeautifulSoup(src, "lxml")
        items = soup.find_all("div", class_="iva-item-content-rejJg")
        for j in items[:10]:
            ssilka = "https://www.avito.ru" + j.find("a").get("href") + "\n"
            if ssilka not in spis:
                with open(filik, "a+", encoding="utf-8") as bebra:
                    bebra.write(ssilka)
                try:
                    name = j.find("div", class_="iva-item-titleStep-pdebR").text
                except:
                    name = "Ваааай, это же ракета"
                try:
                    price = j.find("span", class_="price-text-_YGDY text-text-LurtD text-size-s-BxGpL").text
                except:
                    price = "Цена космическая "
                json_data.append({
                    "Ссылка": ssilka,
                    "Название": name,
                    "Цена": price
                })
            else:
                continue
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

    with open("new_car.json", "w", encoding="utf-8") as opa:
        json.dump(json_data, opa, indent=2, ensure_ascii=False)


def main():
    url = "https://www.avito.ru/bryansk/avtomobili/vaz_lada-ASgCAQICAUDgtg0Uxpko?cd=1&f=ASgCAQECAkDgtg0Uxpko4rYN9BjWmijYmijamijcmijemijgmii6nCjwpijCqCiKqSiqrSjCsyjEsyj0tCj2tCji8jKO8zKcyTaeyTaO0zmQ0znuyz~gkky0iJQBAUXGmgwVeyJmcm9tIjowLCJ0byI6ODAwMDB9&p=1&radius=200&s=104&searchRadius=200"
    get_func(url, "ssilki.txt")


if __name__ == "__main__":
    main()

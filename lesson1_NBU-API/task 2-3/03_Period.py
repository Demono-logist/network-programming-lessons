import requests
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Функция для получения курсов валют за период
def get_exchange_rates(start_date, end_date, valcodes, sort='exchangedate', order='asc', format_type='json'):
    base_url = "https://bank.gov.ua/NBU_Exchange/exchange_site"
    data = {}
    for valcode in valcodes:
        params = {
            'start': start_date,
            'end': end_date,
            'valcode': valcode,
            'sort': sort,
            'order': order,
            'json': format_type
        }
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data[valcode] = response.json()
        else:
            print(f"Ошибка для валюты {valcode}: {response.status_code}")
    return data

# Основной код
if __name__ == "__main__":
    # Задаем параметры
    start_date = "20241111"
    end_date = "20241117"
    valcodes = ["USD", "EUR"]  # Список валют
    sort = "exchangedate"
    order = "asc"
    format_type = "json"
    
    # Получаем данные
    exchange_data = get_exchange_rates(start_date, end_date, valcodes, sort, order, format_type)
    
    # Построение графика
    plt.figure(figsize=(10, 6))
    for valcode, rates in exchange_data.items():
        dates = [rate["exchangedate"] for rate in rates]
        values = [rate["rate"] for rate in rates]
        plt.plot(dates, values, marker='o', label=valcode)

    # Настройка графика
    plt.title("Изменение курса валют за неделю")
    plt.xlabel("Дата")
    plt.ylabel("Курс")
    plt.xticks(rotation=45)
    plt.legend(title="Валюты")
    plt.grid()
    plt.tight_layout()
    plt.show()

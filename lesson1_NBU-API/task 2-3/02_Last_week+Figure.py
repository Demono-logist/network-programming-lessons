import requests
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Функція для отримання курсів валют за дату
def get_exchange_rates(date):
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date={date}&valcode=usd&json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Отримання даних за останній тиждень
today = datetime.today()
rates_by_day = {}
for i in range(7):
    date = (today - timedelta(days=i)).strftime('%Y%m%d')
    rates = get_exchange_rates(date)
    rates_by_day[date] = rates

# Виведення отриманих курсів
for date, rates in rates_by_day.items():
    print(f"Курси валют за {date}:")
    for rate in rates:
        print(f"{rate['cc']}: {rate['rate']}")


# Вибираємо конкретну валюту (наприклад, USD)
currency_code = 'USD'

# Підготовка даних для графіка
dates = list(rates_by_day.keys())
rates = [
    next((rate['rate'] for rate in rates_by_day[date] if rate['cc'] == currency_code), None)
    for date in dates
]

# Побудова графіка
plt.figure(figsize=(10, 5))
plt.plot(dates, rates, marker='o', linestyle='-', color='b', label=f'{currency_code} Rate')
plt.xlabel('Дата')
plt.ylabel('Курс')
plt.title(f'Зміна курсу {currency_code} за останній тиждень')
plt.xticks(rotation=45)
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

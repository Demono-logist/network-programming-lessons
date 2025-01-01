import requests
from datetime import datetime, timedelta

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

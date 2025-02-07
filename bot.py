import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time

while(True):
  now = datetime.now()
  current_time = now.strftime("%H:%M")
  print(f'At time : {current_time} Local Time')
  
  url = 'https://finance.yahoo.com/markets/crypto/all/'
  response = requests.get(url)
  text = response.text
  html_data = BeautifulSoup(text, 'html.parser')

  headings = html_data.find_all('tr')[0]
  headings_list = []

  for h in headings:
    headings_list.append(h.text)
  headings_list = headings_list[:2] + headings_list[3:6]

  print('Headings are: ')
  for column in headings_list:
    print(column)

  data = []

  for x in range(1,6):
    row = html_data.find_all('tr')[x]
    column_value = row.find_all('td')
    coin_data = {}

    coin_data['Symbol'] = column_value[0].text.strip()
    coin_data['Name'] = column_value[1].text.strip()
    coin_data['Price'] = column_value[3].text.split()[0]
    coin_data['Change'] = column_value[4].text.strip()
    coin_data['Change %'] = column_value[5].text.strip()

    data.append(coin_data)

  for coin in data:
    print('----------')
    for key, value in coin.items():
      print(f'{key}: {value}')
    print('----------')
    print('')

  time.sleep(600)

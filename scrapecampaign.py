import codecs
from bs4 import BeautifulSoup
with codecs.open('data/01-raw/investments-neptune-click00085.html', 
  mode='r', encoding="utf-8") as f:
  content = f.read()
soup = BeautifulSoup(content)
rows = list()
for html_row in soup.find_all('div', class_='i-funder-row'):
  try:
    investor_link = html_row.find_all('a')[0]
    investor = investor_link.string.strip()
    investor_id = investor_link['href']
    profile_available = True
  except IndexError:
    investor = html_row.find('div', class_='i-name').string.strip()
    investor_id = None
    profile_available = False
  time_ago = html_row.find_all('div', class_='i-note')[0].string
  time_ago_value = time_ago.split(' ')[0]
  time_ago_unit = time_ago.split(' ')[1]
  # print days_ago.split(' ')[0]
  # print html_row.find_all('span', class_='currency')
  try:
    amount = html_row.find_all('span', 
      class_='currency')[0].find('span').string[1:].replace(',','')
    amount_disclosed = True
  except IndexError:
    amount_disclosed = False
    amount = None
  # # print row
  row = [profile_available,investor_id,investor,time_ago, 
    time_ago_value,time_ago_unit,amount_disclosed,amount]
  rows.append(row)

import pandas as pd 
sheet = pd.DataFrame(rows,columns=['profile_available','investor_id', 
  'investor','time_ago','time_ago_value','time_ago_unit','amount_disclosed',
  'amount'])
sheet.to_csv('data/02-refined/investments-neptune.csv',encoding='utf-8')

















import pandas as pd
import numpy as np
from bs4 import BeautifulSoup, Comment
import requests

url = "https://fbref.com/en/comps/9/2018-2019/possession/2018-2019-Premier-League-Stats"
html = requests.get(url).text
df = BeautifulSoup(html, 'html.parser')

comments = df.find_all(string = lambda text: isinstance(text, Comment))

#print(df)
tables = []
for each in comments:
    if 'table' in str(each):
        try:
            tables.append(pd.read_html(str(each), attrs = {'id': 'stats_possession'})[0])
            break
        except:
            continue
print(tables[-1])
tables[-1].to_csv('possession.csv')
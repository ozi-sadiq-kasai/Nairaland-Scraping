import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://www.nairaland.com/7383021/obi-labour-party-release-updated'
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
summary = doc.find_all('tr')
list_text= [x.get_text()for x in summary]


df = pd.DataFrame(list_text)

df.to_csv("obi_press.csv")





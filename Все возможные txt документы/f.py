from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
 
f = ("http://wiki.stat.ucla.edu/socr/index.php/SOCR_Data_Dinov_020108_HeightsWeights")

r = requests.get(f)

html_content = r.text

soup = BeautifulSoup(html_content, "html.parser")

for tr in soup.find_all('tr')[2]:
    tds = tr.find_all('td')
    print("values:%s, value 2:%s, value3:%s" \
          (tds[0].text,tds[1].test,tds[2].text))

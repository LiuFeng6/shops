import requests
import re
from bs4 import BeautifulSoup

url = 'http://value500.com/pe.asp'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
}
response = requests.get(url, headers=headers).text    #

bb=BeautifulSoup(response,'html.parser')
print(bb)

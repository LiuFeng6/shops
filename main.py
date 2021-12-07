import requests
import re
from bs4 import BeautifulSoup


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
}
url = 'http://value500.com/pe.asp'
response = requests.get(url, headers=headers).text  #

treeak = BeautifulSoup(response, 'html.parser').find("body").find_all("tr", align="center")[1]
PE_Ratio_shanghai = treeak.find_all("td")[1].text
PE_Ratio_shenzheng = treeak.find_all("td")[2].text
print(PE_Ratio_shanghai,PE_Ratio_shenzheng)

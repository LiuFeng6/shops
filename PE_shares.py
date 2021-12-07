import json

import requests
from bs4 import BeautifulSoup
import re
def pe_one_shares(stock_code_list):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
    }
    url = "https://gu.qq.com/"+stock_code_list+"/gp"
    response = requests.get(url, headers=headers).text  #
    treeak = BeautifulSoup(response, 'html.parser').find("div").find_all("span",class_="col-2-4 bl")[-1].text
    return treeak

def pe_ttm_all(stock_code_list):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
    }
    url = "https://xueqiu.com/S/" + stock_code_list
    response = requests.get(url, headers=headers).text
    response = BeautifulSoup(response, 'html.parser').find("body").find("stock-operate").attrs[':quote']  #41.48
    response = json.loads(response)
    pe_ttm = response["pe_ttm"]
    response = response["tableHtml"]
    response = BeautifulSoup(response, 'html.parser')

    # print(response.find("table").find_all("span")) # 观察数据

    pe_static = response.find("table").find_all("span")[14].text            # 市盈率(静)
    pe_activity = response.find("table").find_all("span")[10].text          # 市盈率(动)
    dividend_rate = response.find("table").find_all("span")[21].text        # 股息率(TTM)

    pe_ttm = float(pe_ttm)
    # pe_static = float(pe_static)
    pe_activity = float(pe_activity)
    dividend_rate = float(dividend_rate.strip('%'))

    return pe_ttm, pe_activity, dividend_rate #pe_ttm, pe_static, pe_activity,


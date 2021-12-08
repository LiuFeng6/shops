import json

import requests
from bs4 import BeautifulSoup
import re

def pe_one_shares(stock_code_list):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
    }
    url = "https://gu.qq.com/"+stock_code_list+"/gp"
    response = requests.get(url, headers=headers, verify=False).text  #
    treeak = BeautifulSoup(response, 'html.parser').find("div").find_all("span",class_="col-2-4 bl")[-1].text
    return treeak

def pe_ttm_all(stock_code_list):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
    }
    url = "https://xueqiu.com/S/" + stock_code_list
    response = requests.get(url, headers=headers, verify=False).text
    response = BeautifulSoup(response, 'html.parser').find("body").find("stock-operate").attrs[':quote'].encode('utf-8').decode()  #41.48
    # print(response)
    # 正则表达的应用
    ex_pe_ttm = r'市盈率\(TTM\)：<span>(.*?)</span>'
    pe_ttm = re.findall(ex_pe_ttm, response, re.S)

    ex_dividend_rate = r'股息率\(TTM\)：<span>(.*?)</span>'
    dividend_rate = re.findall(ex_dividend_rate, response, re.S)

    # 将list转str
    pe_ttm = ','.join(pe_ttm)
    dividend_rate = ','.join(dividend_rate)
    # print(type(pe_ttm), type(dividend_rate))

    # 将str转float
    pe_ttm = float(pe_ttm)
    dividend_rate = float(dividend_rate.strip('%'))
    # print(type(pe_ttm), type(dividend_rate))
    return pe_ttm, dividend_rate
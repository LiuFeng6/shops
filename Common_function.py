import requests
from bs4 import BeautifulSoup

def PE_Ratio():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
    }
    url = 'http://value500.com/pe.asp'
    response = requests.get(url, headers=headers).text  #
    treeak = BeautifulSoup(response, 'html.parser').find("body").find_all("tr", align="center")[1]

    PE_Ratio_shanghai = treeak.find_all("td")[1].text
    PE_Ratio_shenzheng = treeak.find_all("td")[2].text
    return PE_Ratio_shanghai, PE_Ratio_shenzheng

def china_10_year_bond_yield():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
    }
    # url = 'https://cn.investing.com/rates-bonds/china-10-year-bond-yield?__cf_chl_jschl_tk__=FAl1tnF7Y6nQ7Y7FzlOPvf5md4RPpqGwueDZwJJSWCU-1638859732-0-gaNycGzNDFE'
    url = 'https://cn.investing.com/rates-bonds/china-10-year-bond-yield'


    response = requests.get(url, headers=headers).text
    china_10_year_bond = BeautifulSoup(response, 'html.parser').find("span", id="fl_header_pair_lst").text
    return float(china_10_year_bond)

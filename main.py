from Common_function import *
from PE_shares import *

PE_Ratio_shanghai, PE_Ratio_shenzheng = PE_Ratio()
china_10_year_bond = 2.8 #china_10_year_bond_yield()
stock_code_list = ['sh600000',  'sz300124', 'sh600276', 'sz002952']

for i in stock_code_list:

    pe_ttm, dividend_rate = pe_ttm_all(i)
    print(i,"市盈率:",pe_ttm," ", "15")                         # 市盈率(TTM)： 是否小于15
    print("深圳市盈率:",PE_Ratio_shenzheng," ", "20")            # 深圳市盈率(TTM)： 是否小于20

    print("股息率(TTM):",dividend_rate, china_10_year_bond)     # 股息率(TTM)是否大于十年国债
    
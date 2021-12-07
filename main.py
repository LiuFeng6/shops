from Common_function import *
from PE_shares import *

PE_Ratio_shanghai, PE_Ratio_shenzheng = PE_Ratio()
china_10_year_bond = china_10_year_bond_yield()
# stock_code_list = ['sh000300', 'sh600000', 'sz000002', 'sh600002', 'sz000003', 'sz300124', 'sh600276', 'sz002952']

stock_code_list = ['sz300124','sz002952','sh600276']

# print(china_10_year_bond)

# print(PE_RatioRatio_shanghai, PE_Ratio_shenzheng)
# print(china_10_year_bond)

for i in stock_code_list:
    pe_ttm = pe_one_shares(i)               # 市盈率(TTM)：
    # print(pe_one_shares1)
    cc = pe_ttm_all(i)
    pe_activity = cc[1]
    dividend_rate = cc[2]                   # 股息率(TTM)是大于十年国债
    # pe_ttm, pe_static, pe_activity, dividend_rate = pe_ttm_all(i)
    print(100*"*")
    print(i)
    print(pe_ttm," ", "15")                 # 市盈率(TTM)： 是否小于15
    print(dividend_rate, china_10_year_bond)



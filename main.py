from PE_Ratio import *
from Ten_year_Treasury_yield import *


PE_Ratio_shanghai, PE_Ratio_shenzheng = PE_Ratio()
china_10_year_bond = china_10_year_bond_yield()

print(PE_Ratio_shanghai, PE_Ratio_shenzheng)
print(china_10_year_bond)
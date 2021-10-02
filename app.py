from Database.DB import *
import re

if not bool(re.match('^(\d{4})[/.-](\d{1,2})[/.-](\d{1,2})$',"2021/03/20")):
    print("please enter valid date, format : YYYY/MM/DD")




print(fetchInitData("OBJECTID"))




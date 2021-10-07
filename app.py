from Database.DB import *
import re

if not bool(re.match('^(\d{4})[/](\d{1,2})[/](\d{1,2})$',"1999/2/3")):
    print("please enter valid date, format : YYYY/MM/DD")

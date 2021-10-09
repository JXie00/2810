import re

def dateValidation(date:str):
   return bool(re.match('^(\d{4})[/](\d{1,2})[/](\d{1,2})$',date))
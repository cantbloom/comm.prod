import re

"""
Returns a list of commprods if any
are found in the query, otherise 
returns None
"""
def parseProd(query):
    btb_regex = '((a btb)|(btb)|(abtb))'
    prod_regex = '((comm.prod)$|(comm prod)$|(commprod)$)'
    regex = btb_regex + '(?P<comm_prod>.+?)' + prod_regex + "+"
    pattern = re.compile(regex, re.I|re.M)
    match = pattern.search(query)
    prods = []
    if match:
        for m in pattern.finditer(query):
            m = strip_quotes(m.group('comm_prod'))
            prods.append(m)
        return prods

    return None
    
def strip_quotes(string):
    string = string.strip()
    if (string.startswith('"') or string.startswith("'")):
        string = string[1:]
    if (string.endswith('"') or string.endswith("'")):
        string = string[:-1]
    return string


## Test cases
content = """

a btb 'parse this' comm.prod

or

abtb "parse that" commprod

and

btb "then this" comm prod

BTB "comm" commprod

ABTB  COMMPROD

a btb "a btb in the middle comm prod" comm.prod

a btb "a btb 'in the middle' comm prod" comm.prod

"""
prod = ["parse this", "parse that", "then this", "comm", "",
         "a btb in the middle comm prod",
         "a btb 'in the middle' comm prod"]

#assert(parseProd(content)== prod)
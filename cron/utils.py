"""
Remove leading or trailing quotes from a string
"""
def strip_quotes(string):
    string = string.strip()
    if (string.startswith('"') or string.startswith("'")):
        string = string[1:]
    if (string.endswith('"') or string.endswith("'")):
        string = string[:-1]
    return string

"""
shitty hack
"""
def stripOld(query):
    strip_params = [ "---------- Forwarded message ----------",
        "-----Original message-----",
        "wrote:",
        "________________________________________",
        'Quoting',
        '\r\n>',
        '\n>',
        'From:'
        ]
    if query != None:
        for param in strip_params:
            query = query.split(param)[0]
        query+="\n" ## if there is not newline at the end, add it to pick up the commprod
        return query

def clean_content(query, type):
    if type == "email":
        query = query.replace('=\r\n', '\n')
    elif type == "commprod":
        query = query.replace('=\r\n', '')
    query = query.replace('=92', '\'')
    query = query.replace('=93', '"')
    query = query.replace('=94', '"')
    query = query.replace('=20', '')
    return query
                             
"""
Helper to read message content
"""
def get_first_text_block(msg):
    for part in msg.walk():
        if part.get_content_type() == 'text/plain':
            return part.get_payload()
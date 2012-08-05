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
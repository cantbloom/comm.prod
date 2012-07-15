from django import template
from django.utils.html import urlize

import re 

register = template.Library()


"""
Finds and replaces urls in the commprod content
with a standard <a> tag or embeds a youtube video in the page
"""
def urlize_commprod(commprod):
    result = re.findall(r"\b(?:(?:https?|ftp|file)://|www\.|ftp\.)[-A-Z0-9+&@#/%=~_|$?!:,.]*[A-Z0-9+&@#/%=~_|$]", commprod)
    print result

from django import template
from django.template.defaultfilters import stringfilter
from HTMLParser import HTMLParser

import re 

register = template.Library()

url_regex = "(?P<url>https?://[^\s]+)"

"""
Finds and replaces urls in the commprod content
with a standard <a> tag or embeds a youtube video in the page
"""
@register.filter
def urlize_commprod(commprod):
    commprod = clean_prod(commprod)
    commprod = strip_tags(commprod)
    pattern = re.compile(url_regex, re.I)
    match = pattern.search(commprod)
    if match:
        for m in pattern.finditer(commprod):
            url_match = m.group('url')
            if 'youtube' in url_match:
                commprod = commprod.replace(url_match, youtube_tag(url_match))
            else:
                commprod = commprod.replace(url_match, a_tag(url_match))
    return commprod

"""
Does some cleanup to remove '<' and '>' characters from a link to account for weirdness with URL embedding. Commprod is then run through strip_tags to removed embedded tags.
"""
def clean_prod(commprod):
    pattern = re.compile(url_regex, re.I)
    match = pattern.search(commprod)
    strip_chars = ['<', '>']
    prod_list = list(commprod)
    if match:
        for m in pattern.finditer(commprod):
            group = 'url'
            start = max(m.start(group) - 1, 0)
            end = min(m.end(group) + 1, len(prod_list)-1)
            if prod_list[start] in strip_chars:
                prod_list[start] = ""
            elif prod_list[end] in strip_chars:
                prod_list[end] = ""
    return "".join(prod_list)

"""
Wraps the given text in an <a> tag.
"""
def a_tag(url_match):
    return "<a target='_blank' href='%s'>%s</a>" % (url_match, url_match)


"""
Tries to extract the video id and return an iFrame. 
If this fails it returns a <a> tag wrapped string.
"""
def youtube_tag(url_match):
    try:
        v = url_match[url_match.index('v=')+2:]
        v = v.split('/')[0]
    except ValueError:
        return a_tag(url_match) # couldn't extract the value return just a link.
    
    return '<br><br><iframe id="ytplayer" type="text/html" width="320" height="195" src="http://www.youtube.com/embed/%s" frameborder="0"></iframe><br><br>' % v

"""
Helper to remove anchor tags
"""
class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

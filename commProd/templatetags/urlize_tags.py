from django import template
from django.template.defaultfilters import stringfilter
from HTMLParser import HTMLParser
from cron.parseprod_cron import strip_quotes
import re, requests

register = template.Library()

url_regex = "(?P<url>https?://[^\s][^>;]+)"
group = 'url'
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
        previous_matches = {}
        for m in pattern.finditer(commprod):
            url_match = strip_quotes(m.group(group))
            
            if url_match not in previous_matches:
                if 'youtube' in url_match:
                    commprod = commprod.replace(url_match, youtube_tag(url_match))
                else:
                    tag = img_or_url(url_match)
                    commprod = commprod.replace(url_match, tag)
            
                previous_matches[url_match] = url_match

    return commprod

"""
Does some cleanup to remove '<' and '>' characters from a link to account for weirdness with URL embedding. Commprod is then run through strip_tags to removed embedded tags.
"""
def clean_prod(commprod):
    pattern = re.compile(url_regex, re.I)
    match = pattern.search(commprod)
    prod_list = list(str(commprod))
    invalid = ["<", ">"]
    if match:
        for m in pattern.finditer(commprod):
            start = max(m.start(group), 0)
            end = min(m.end(group), len(prod_list)-1)
            start_minus = max(start-1, 0)
            end_plus = min(end+1, len(prod_list)-1)
            locations = [start, start_minus, end, end_plus]
                                                                                                                                                                                                                                                                                                                                                         
            for loc in locations:
                if prod_list[loc] in invalid:
                    prod_list[loc] = ""
    return "".join(prod_list)

"""
Tries to determine if the url is an image and returns either an anchor tag or img tag
"""
def img_or_url(url_match):
    try:
        r = requests.get(url_match,timeout=1)
        content_type  = r.headers['content-type']
        if 'image' in content_type:
            return img_tag(url_match)
    except:
        print 'timeout', url_match
        pass

    return a_tag(url_match)


"""
Wraps the given url in a <img> tag
"""
def img_tag(url_match):
    dim = '50%' #string format is dumb
    tag = "<br><br><img src='%s' width='%s' height='%s'><br><br>"% (url_match, dim, dim)
    return a_tag(url_match, tag)

"""
Wraps the given text in an <a> tag.
"""
def a_tag(url_match, text=None):
    if not text:
        text = url_match
    return "<a target='_blank' href='%s'>%s</a>" % (url_match, text)


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
    
    return '<br><br><iframe id="ytplayer" type="text/html" width="265px" height="195px" src="http://www.youtube.com/embed/%s" frameborder="0"></iframe><br><br>' % v

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

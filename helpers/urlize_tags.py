from common.constants import REGEX

import requests
import re

url_regex = REGEX['url_regex']
group = 'url'

def urlize_text(text):
    """
        Finds and replaces urls in the text content
        with a standard <a> tag or embeds a 
        youtube video in the page
    """
    pattern = re.compile(url_regex, re.I)
    match = pattern.search(text)
    if match:
        previous_matches = {}
        for m in pattern.finditer(text):
            url_match = m.group(group)
            if url_match not in previous_matches:
                if 'youtube' in url_match:
                    text = text.replace(url_match, 
                        youtube_tag(url_match))
                else:
                    tag = img_or_url(url_match)
                    text = text.replace(url_match, tag)
            
                previous_matches[url_match] = url_match

    return text

def img_or_url(url_match):
    """
        Tries to determine if the url is an image
        and returns either an anchor tag or img tag
    """
    try:
        r = requests.get(url_match, timeout=1)
        content_type  = r.headers['content-type']
        if 'image' in content_type:
            return img_tag(url_match)
    except:
        print 'timeout', url_match
        pass

    return a_tag(url_match)

def img_tag(url_match):
    """
        Wraps the given url in a <img> tag
    """
    dim = '50%'
    tag = """<br><br><img src='%(url_match)s' width='%(dim)s'
     height='%(dim)s'><br><br>""" % {
        'url_match' : url_match,
        'dim' :  dim,
    }
    return a_tag(url_match, tag)

def a_tag(url_match, text=None):
    """
        Wraps the given text in an <a> tag.
    """
    if not text:
        text = url_match
    return "<a target='_blank' href='%(url_match)s'>%(text)s</a>" % {
        'url_match' : url_match,
        'text' :  text,
    }

def youtube_tag(url_match):
    """
        Tries to extract the video id and return an iFrame. 
        If this fails it returns a <a> tag wrapped string.
    """
    try:
        vid_url = url_match[url_match.index('v=') + 2:]
        vid_url = vid_url.split('/')[0]
    except ValueError:
        # couldn't extract the value return just a link.
        return a_tag(url_match) 
    
    return """<br><br><iframe id='ytplayer' 
        type='text/html' width='265px' 
        height='195px' 
        src='http://www.youtube.com/embed/%s' 
        frameborder='0'></iframe><br><br>""" % vid_url

def commprod_contains_media(commprod_content):
    """
        Detect if a commprod content has media
         (url, img, youtube video)
    """
    pattern = re.compile(url_regex, re.I)
    match = pattern.search(commprod_content)
    return bool(match)

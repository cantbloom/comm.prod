from django import template
import string

from django.conf import settings

register = template.Library()

@register.simple_tag
def include_script(script_name,
                   load_minified=(not settings.DEBUG),
                   overload=settings.DEBUG):

    # clean up the script name
    script_name = script_name.replace(".min.js", "")
    script_name = script_name.replace(".js", "")

    # make the script path
    path_prefix = "/public/js/"
    path_suffix = ".js"

    script_path = path_prefix + script_name + path_suffix

    return """<script type="text/javascript" src="%s"></script>""" % script_path

@register.simple_tag
def include_style(style_name):
    style_name = style_name.replace('.css', '')
    path_prefix = "/public/css/"
    path_suffix = ".css"

    style_path = path_prefix + style_name + path_suffix

    return """<link rel="stylesheet" href="%s" />""" % style_path
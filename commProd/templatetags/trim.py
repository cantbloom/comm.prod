from django import template
register = template.Library()


TRIM_VAL = 300


@register.filter
def trim(value, max_length=TRIM_VAL):
    if len(value) > max_length:
        truncd_val = value[:max_length]
        if not len(value) == max_length + 1 and \
                value[max_length + 1] != " ":
            truncd_val = truncd_val[:truncd_val.rfind(" ")]
        return truncd_val + "..."
    return value

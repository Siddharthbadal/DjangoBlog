from django import template

register = template.Library()

@register.filter()
def mytextsplit(value, sep = ". "):
    parts = value.split(sep)
    return (parts[0]+".",)
